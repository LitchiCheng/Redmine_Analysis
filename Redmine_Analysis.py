from redminelib import Redmine
import arrow

def isLeapYear(years):
    '''
    通过判断闰年，获取年份years下一年的总天数
    :param years: 年份，int
    :return:days_sum，一年的总天数
    '''
    # 断言：年份不为整数时，抛出异常。
    assert isinstance(years, int), "请输入整数年，如 2018"
 
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365
        return days_sum

def getAllDayPerYear(years):
    '''
    获取一年的所有日期
    :param years:年份
    :return:全部日期列表
    '''
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    # print(all_date_list)
    return all_date_list

def generateAllDayDict(years):
    start_date = '%s-1-1' % years
    a = 0
    all_date_dict = {}
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_dict[b] = 0
    return all_date_dict

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
        self.date_dict = generateAllDayDict("2020")
        self.all_issues = self.getAllIssues()
        for i in self.all_issues:
            try:
                key = str(i.start_date)
                if key in self.date_dict:
                    value = self.date_dict[key]
                    self.date_dict[key] = value + 1
                else:
                    self.date_dict[key] = 0
            except Exception as e:
                print(e)
        return self.date_dict

test = RedMineAnalysis('https://xxxx', "xxx", "xxx")
dict_result = test.sumIssuesNumByDate()
print(dict_result)

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.Point import Point

win = pg.GraphicsWindow()
win.setWindowTitle('canopenGui')

xdict = dict(enumerate(list(dict_result.keys())))
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([xdict.items()])
p1 = win.addPlot(axisItems={'bottom': stringaxis})
p1.plot(x = list(xdict.keys()), y = list(dict_result.values()), pen="y", symbolBrush=(255,0,0), symbolPen='w')

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

