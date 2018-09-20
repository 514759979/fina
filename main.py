# -*- coding:utf-8 -*-

import xlrd
import xlwt
import os
import sys
import json
import logging
import traceback
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QTranslator

from mainwindow import Ui_MainWindow
CONFIG = 'settings.json'
LOG_NAME = 'filter.log'
FORMAT = '%(asctime)s : %(levelname)-5.5s [%(lineno)s] %(message)s'

def load_config(path):
    with open(path, 'r', encoding='utf-8') as fp:
        f = fp.read()
        config = json.loads(f)

    return config


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename=LOG_NAME)
        global CONFIG
        self.config = load_config(CONFIG)
        self.FIELDS = self.config['fields']
        self.RANKS = self.config['ranks']

        logging.info(u'fields:{0}'.format(self.FIELDS))
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(u"南丁格尔工具箱 v0.4")

        self.file_path = None
        self.sheet_index = None
        self.column = None
        
        self.ui.start_ptn.clicked.connect(self.clicked_start)
        self.ui.choose_ptn.clicked.connect(self.clicked_open_file)

    def echo(self, value):
        QMessageBox.information(self, u"返回值", value, QMessageBox.Ok)

    def clicked_open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, u"选取文件", "./", "ALL Files (*);;xlsx Files (*.xlsx)")
        if os.path.exists(file_name):
            self.ui.input_file_path.setText(file_name)

    def clicked_start(self):
        f = self.ui.input_file_path.text()
        i = self.ui.input_index.text()
        c = self.ui.imput_col.text()
        if i and c:
            try:
                i = int(i) - 1
                c = int(c) - 1
                if i < 0 or c < 0:
                    self.echo(u"请输入正确的数字！")
            except ValueError:
                self.echo(u"请输入正确的数字！")
        
        if f and isinstance(i, int) and isinstance(c, int):
            self.start_process(f, i, c)
        else:
            pass

    def find_keys(self, keys, order):
        key = r'|'.join(keys)
        patt = re.compile(key)
        result = re.findall(patt, order)
        return result

    def get_rank(self, size):
        max_len = len(self.RANKS)
        if size > max_len:
            logging.info('keys size more than ranks size:{}'.format(size))
            size = max_len

        return self.RANKS[:size]

    def start_process(self, path, index, col_num):
        logging.info(u'path:{0} index:{1} col:{2}'.format(path, index, col_num))
        try:
            data = xlrd.open_workbook(path)
            rs = data.sheet_by_index(index)
            col_values = []
            col_values.extend(rs.col_values(col_num))

            wb = xlwt.Workbook()
            ws = wb.add_sheet('result')

            for i, v in enumerate(col_values):
                if not isinstance(v, str):
                    logging.error('line:{0} V:{1}'.format(i+1, v))
                else:
                    res = self.find_keys(self.FIELDS, v)
                    rk = self.get_rank(len(res))
                    
                    ws.write(i, 0, ' '.join(res))
                    ws.write(i, 1, '、'.join(rk))

            wb.save('result.xlsx')
            self.echo(u"完成")
        except Exception:
            self.echo(u'发现错误，请检查log！')
            logging.error(traceback.format_exc(limit=5))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    