from redminelib import Redmine
import date_util as du

class RedMineAnalysis:
    def __init__(self):
        pass

    def __init__(self, url, username, password):
        self.username = username
        self.url = url
        self.password = password
        self.redmine = Redmine(self.url, username = self.username, password = self.password)
    
    def connect(self):
        self.redmine = Redmine(self.url, username = self.username, password = self.password)

    def connect(self, url, username, password):
        self.username = username
        self.url = url
        self.password = password
        self.redmine = Redmine(self.url, username = self.username, password = self.password)

    def getIssuesSum(self):
        return len(self.redmine.issue.all())

    def getAllIssues(self):
        return self.redmine.issue.all()

    def sumIssuesNumByDate(self):
        self.date_dict = du.generateAllDayDict("2020")
        self.all_issues = self.getAllIssues()
        for item in self.all_issues:
            try:
                key = str(item.created_on)
                print(key)
                if key in self.date_dict:
                    value = self.date_dict[key]
                    self.date_dict[key] = value + 1
                else:
                    self.date_dict[key] = 0
            except Exception as e:
                print(e)
        last_value = 0
        for k in self.date_dict.keys():
            self.date_dict[k] = self.date_dict[k] + last_value
            last_value = self.date_dict[k]
        return self.date_dict

test = RedMineAnalysis('https://xxm', "xxx", "3.xxxx")
dict_result = test.sumIssuesNumByDate()
print(dict_result)

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

win = pg.GraphicsWindow()
win.setWindowTitle('issues-sum')

xdict = dict(enumerate(list(dict_result.keys())))
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([xdict.items()])
plot = win.addPlot(axisItems={'bottom': stringaxis})
plot.plot(x = list(xdict.keys()), y = list(dict_result.values()),pen=(200,200,200),symbolBrush=(255,0,0), symbolPen='b')
plot.setLabel(axis='left',text='数量')
plot.setLabel(axis='bottom',text='日期')
plot.showGrid(x=True,y=True)
if __name__ == "__main__":
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

# dd = {}
# key = 9
# if key in dd:
#     print("fsadfas")
# else:
#     dd[key] = 10
# print(dd.values())

