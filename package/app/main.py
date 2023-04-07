import requests
from package.app.design import Ui_bistMain
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QValidator
import time
import sys
import threading
import datetime
import PyQt5.QtWidgets
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
import json
from PyQt5.QtWidgets import QApplication, QWidget
from package.function.getdata import dataThread
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QMainWindow,QThread):

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        super().__init__(parent)
        self.ui = Ui_bistMain()
        self.ui.setupUi(self)





        self.datathread = dataThread(self)
        self.datathread.dataChanged.connect(self.set)
        self.datathread.start()

        self.webEngineView = QWebEngineView()
        self.url = QUrl.fromUserInput("https://bigpara.hurriyet.com.tr/borsa/haber/")
        self.webEngineView.load(self.url)
        self.ui.layout_news.addWidget(self.webEngineView)
        self.ui.btn_Refresh.clicked.connect(self.btn_refresh_clicked)
        self.ui.btn_Back.clicked.connect(self.btn_back_clicked)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            threadCount = QThreadPool.globalInstance().maxThreadCount()
            pool = QThreadPool.globalInstance()
            for i in range(threadCount):
                # 2. Instantiate the subclass of QRunnable
                runnable = Runnable(i)
                # 3. Call start()
                pool.start(runnable)
            event.accept()
            print('Window closed')
        else:
            event.ignore()


    def btn_refresh_clicked(self):
        self.webEngineView.reload()

    def btn_back_clicked(self):
        self.webEngineView.back()

    def set(self,value_dollar_buying,value_dollar_selling,value_euro_buying,value_euro_selling,value_gbp_buying,value_gbp_selling,
            value_btc_buying,value_btc_selling,value_eth_buying,value_eth_selling,value_xu100_buying,value_xu100_selling,
            value_dollar_change,value_euro_change, value_gbp_change, value_btc_change, value_eth_change, value_xu100_change
            ):

            now = datetime.datetime.now()

            second = now.second
            minute = now.minute
            hour = now.hour
            day = now.day
            month = now.month
            year = now.year

            value_time = (f'{hour}:{minute}:{second}')
            value_date = (f'{day}.{month}.{year}')

            choosenValue = self.ui.combox_value.currentIndex()

            if choosenValue==0:
                self.ui.val_special_name.setText('USD/TRY')
                self.ui.val_special_buying.setText(value_dollar_buying)
                self.ui.val_special_selling.setText(value_dollar_selling)
                self.ui.val_special_change.setText(f"% {value_dollar_change}")
            elif choosenValue==1:
                self.ui.val_special_name.setText('EUR/TRY')
                self.ui.val_special_buying.setText(value_euro_buying)
                self.ui.val_special_selling.setText(value_euro_selling)
                self.ui.val_special_change.setText(f"% {value_euro_change}")
            elif choosenValue == 2:
                self.ui.val_special_name.setText('GBP/TRY')
                self.ui.val_special_buying.setText(value_gbp_buying)
                self.ui.val_special_selling.setText(value_gbp_selling)
                self.ui.val_special_change.setText(f"% {value_gbp_change}")
            elif choosenValue == 3:
                self.ui.val_special_name.setText('BTC/TRY')
                self.ui.val_special_buying.setText(value_btc_buying)
                self.ui.val_special_selling.setText(value_btc_selling)
                self.ui.val_special_change.setText(f"% {value_btc_change}")
            elif choosenValue == 4:
                self.ui.val_special_name.setText('ETH/TRY')
                self.ui.val_special_buying.setText(value_eth_buying)
                self.ui.val_special_selling.setText(value_eth_selling)
                self.ui.val_special_change.setText(f"% {value_eth_change}")
            elif choosenValue == 5:
                self.ui.val_special_name.setText('XU100/TRY')
                self.ui.val_special_buying.setText(value_xu100_buying)
                self.ui.val_special_selling.setText(value_xu100_selling)
                self.ui.val_special_change.setText(f"% {value_xu100_change}")


            self.ui.val_buying_usd.setText(value_dollar_buying)
            self.ui.val_selling_usd.setText(value_dollar_selling)
            self.ui.val_change_usd.setText(f"% {value_dollar_change}")
            self.ui.val_buying_euro.setText(value_euro_buying)
            self.ui.val_selling_euro.setText(value_euro_selling)
            self.ui.val_change_euro.setText(f"% {value_euro_change}")
            self.ui.val_buying_gbp.setText(value_gbp_buying)
            self.ui.val_selling_gbp.setText(value_gbp_selling)
            self.ui.val_change_gbp.setText(f"% {value_gbp_change}")
            self.ui.val_buying_btc.setText(value_btc_buying)
            self.ui.val_selling_btc.setText(value_btc_selling)
            self.ui.val_change_btc.setText(f"% {value_btc_change}")
            self.ui.val_buying_eth.setText(value_eth_buying)
            self.ui.val_selling_eth.setText(value_eth_selling)
            self.ui.val_change_eth.setText(f"% {value_eth_change}")
            self.ui.val_buying_xu100.setText(value_xu100_buying)
            self.ui.val_selling_xu100.setText(value_xu100_selling)
            self.ui.val_change_xu100.setText(f"% {value_xu100_change}")

            self.ui.val_time.setText(value_time)
            self.ui.val_date.setText(value_date)





if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())







