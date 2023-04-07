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

class dataThread(QThread):

    dataChanged = pyqtSignal(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,
                             str,str,str)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        while True:
            exchageRequests = requests.get("https://api.genelpara.com/embed/borsa.json")
            exchangeText = exchangeRequests.json()

            value_dollar_buying = exchangeText['USD']['alis']
            value_dollar_selling = exchangeText['USD']['satis']
            value_dollar_change = exchangeText['USD']['degisim']


            value_euro_buying = exchangeText['EUR']['alis']
            value_euro_selling = exchangeText['EUR']['satis']
            value_euro_change =  exchangeText['EUR']['degisim']

            value_gbp_buying = exchangeText['GBP']['alis']
            value_gbp_selling = exchangeText['GBP']['satis']
            value_gbp_change  = exchangeText['GBP']['degisim']

            value_btc_buying = exchangeText['BTC']['alis']
            value_btc_selling = exchangeText['BTC']['satis']
            value_btc_change  = exchangeText['BTC']['degisim']

            value_eth_buying = exchangeText['ETH']['alis']
            value_eth_selling = exchangeText['ETH']['satis']
            value_eth_change  = exchangeText['ETH']['degisim']

            value_xu100_buying = exchangeText['XU100']['alis']
            value_xu100_selling = exchangeText['XU100']['satis']
            value_xu100_change = exchangeText['XU100']['degisim']
            print(exchangeText)

            self.dataChanged.emit(value_dollar_buying,value_dollar_selling,value_euro_buying,value_euro_selling,value_gbp_buying,value_gbp_selling,
            value_btc_buying,value_btc_selling,value_eth_buying,value_eth_selling,value_xu100_buying,value_xu100_selling,value_dollar_change,
                                  value_euro_change,value_gbp_change,value_btc_change,value_eth_change,value_xu100_change)

            time.sleep(1)


