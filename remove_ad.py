# -*- coding:utf-8 -*-

import xlrd
import xlwt
import os
import sys
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QTranslator

from mainwindow import Ui_MainWindow
CONFIG = 'settings.json'

def load_config(path):
    with open(path, 'r', encoding='utf-8') as fp:
        f = fp.read()
        config = json.loads(f)

    return config

#FIELDS = [u'服装', u'教育', u'蜂蜜', u'海参', u'减肥', u'补肾', u'皮肤病', u'糖尿病', u'祛斑', u'小说', u'胃病', u'酵素', u'白酒', u'生发', u'失眠', u'面膜', u'情感进线']


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        global CONFIG
        self.config = load_config(CONFIG)
        print(self.config)
        self.FIELDS = self.config['fields']
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(u"南丁格尔-过滤器 v0.1")

        self.file_path = None
        self.sheet_index = None
        self.column = None
        
        self.ui.start_ptn.clicked.connect(self.clicked_start)
        self.ui.choose_ptn.clicked.connect(self.clicked_open_file)

    def echo(self, value):
        QMessageBox.information(self, u"返回值", value, QMessageBox.Ok)

    def clicked_open_file(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, u"选取文件", "./", "ALL Files (*);;xlsx Files (*.xlsx)")
        #print(file_name)
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

    def start_process(self, path, index, col_num):
        data = xlrd.open_workbook(path)
        rs = data.sheets()[index]
        col_values = []
        col_values.extend(rs.col_values(col_num))

        wb = xlwt.Workbook()
        ws = wb.add_sheet('result')

        for i, v in enumerate(col_values):
            write_list = []
            for field in self.FIELDS:
                if field in v:
                    write_list.append(field)
            write_value = ' '.join(write_list)
            ws.write(i, 0, write_value)

        wb.save('result.xlsx')
        self.echo(u"完成")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    