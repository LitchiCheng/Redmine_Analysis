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

    def getAllUser(self):
        return self.redmine.user.all()

    def sumIssuesNumByDate(self):
        self.date_dict = du.generateAllDayDict("2020")
        self.all_issues = self.getAllIssues()
        self.date_list = []
        self.num_list = []
        for item in self.all_issues:
            try:
                key = str(item.start_date)
                self.date_list.append(key)
                time = str(item.created_on)
                project_id = int(item.project.id)
                if key in self.date_dict and (str(time[0:4]) == "2020") and project_id != 40 and project_id != 38 and project_id != 46:
                    value = self.date_dict[key]
                    self.date_dict[key] = value + 1
            except Exception as e:
                print(e)
        last_value = 0
        for k in self.date_dict.keys():
            # self.date_dict[k] = self.date_dict[k] + last_value    # 叠加效果
            self.num_list.append(self.date_dict[k])
            last_value = self.date_dict[k]
        print(du.generateAllMonthList('2020')) # 每月为节点的全年天数列表
        print(self.num_list)
        return self.date_dict
    
    def sumIssuesCreater(self):
        self.all_issues = self.getAllIssues()
        self.username_list = []
        self.num_list = []
        self.username_dict = {}
        self.username_num_list = []
        for user in self.getAllUser():
            user_name = str(user.lastname) + str(user.firstname)
            self.username_dict[user_name] = 0
            self.username_list.append(user_name)
            self.username_num_list.append([user_name,0])
            print(user_name)
        for item in self.all_issues:
            try:
                key = str(item.author.name)  #
                time = str(item.created_on)
                project_id = int(item.project.id)
                if key in self.username_dict and (str(time[0:4]) == "2020") and (project_id != 40) and (project_id != 38):
                    value = self.username_dict[key]
                    self.username_dict[key] = value + 1
                    for ii in self.username_num_list:
                        if ii[0] == key:
                            ii[1] = value + 1
            except Exception as e:
                print(e)
        for k in self.username_dict.keys():
            self.num_list.append(self.username_dict[k])
        print(self.username_list) # 所有用户
        print(self.num_list)
        print(self.username_num_list)
        return self.username_dict

    def sumIssuesNumByTime(self):
        self.hours_dict = du.generateAllHoursDict()
        self.all_issues = self.getAllIssues()
        self.hours_list = du.generateAllHoursList()
        self.num_list = []
        for item in self.all_issues:
            try:
                key = str(item.created_on)  # 2019-12-18 05:42:23
                item_hour = du.transformTimeZone(0,8,int(key[11:13]))
                project_id = int(item.project.id)
                if item_hour in self.hours_dict and (str(key[0:4]) == "2020") and project_id != 40 and project_id != 38 and project_id != 46:
                    value = self.hours_dict[item_hour]
                    self.hours_dict[item_hour] = value + 1
            except Exception as e:
                print(e)
        # last_value = 0
        for k in self.hours_dict.keys():
            # self.hours_dict[k] = self.hours_dict[k] + last_value    # 叠加效果
            self.num_list.append(self.hours_dict[k])
            last_value = self.hours_dict[k]
        print(self.hours_list) # 每月为节点的全年天数列表
        print(self.num_list)
        return self.hours_dict

    def sumIssuesNumUpdatedByTime(self):
        self.hours_dict = du.generateAllHoursDict()
        self.all_issues = self.getAllIssues()
        self.hours_list = du.generateAllHoursList()
        self.num_list = []
        for item in self.all_issues:
            try:
                key = str(item.updated_on)  # 2019-12-18 05:42:23
                item_hour = du.transformTimeZone(0,8,int(key[11:13]))
                project_id = int(item.project.id)
                if item_hour in self.hours_dict and (str(key[0:4]) == "2020") and project_id != 40 and project_id != 38 and project_id != 46:
                    value = self.hours_dict[item_hour]
                    self.hours_dict[item_hour] = value + 1
            except Exception as e:
                print(e)
        # last_value = 0
        for k in self.hours_dict.keys():
            # self.hours_dict[k] = self.hours_dict[k] + last_value    # 叠加效果
            self.num_list.append(self.hours_dict[k])
            last_value = self.hours_dict[k]
        print(self.hours_list) # 每月为节点的全年天数列表
        print(self.num_list)
        return self.hours_dict
    
    def sumIssuesWatchers(self):
        self.all_issues = self.getAllIssues()
        self.num_list = []
        self.id_list = []
        self.id_watch_num_dict = {}
        for item in self.all_issues:
            try:
                time = str(item.created_on)  # 2019-12-18 05:42:23
                key = str(item.id)  # 2019-12-18 05:42:23
                
                project_id = int(item.project.id)
                if(str(time[0:4]) == "2020") and project_id != 40 and project_id != 38 and project_id != 46:
                    self.id_list.append(key)
                    self.id_watch_num_dict[key] = len(item.watchers)
            except Exception as e:
                print(e)
        # last_value = 0
        for k in self.id_watch_num_dict.keys():
            # self.hours_dict[k] = self.hours_dict[k] + last_value    # 叠加效果
            self.num_list.append(self.id_watch_num_dict[k])
            last_value = self.id_watch_num_dict[k]
        print(self.id_list)
        print(self.num_list)
        return self.id_watch_num_dict

test = RedMineAnalysis('xx', "xx", "3.xxx")
dict_result = test.sumIssuesWatchers()
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

