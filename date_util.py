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

def generateAllDayList(years):
    start_date = '%s-1-1' % years
    a = 0
    all_date_dict = []
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_dict.append(b)
    return all_date_dict

def generateAllMonthList(years):
    start_date = '%s-1-1' % years
    a = 0
    all_date_dict = []
    days_sum = isLeapYear(int(years))
    month_record = "01"
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        if str(b[5:7]) != month_record:
            all_date_dict.append(b)
        else:
            all_date_dict.append("")
        month_record = b[5:7]
    return all_date_dict

def generateAllHoursList():
    start_hour = 00
    all_hour_list = []
    all_hour_list.append("00:00:00")
    hours_sum = 24
    step = 1
    while step < hours_sum:
        step += 1
        start_hour += 1
        hour_str = ""
        if start_hour < 10:
            hour_str += ('0'+str(start_hour) + ":00:00")
        else:
            hour_str += (str(start_hour) + ":00:00")
        all_hour_list.append(hour_str)
        hour_str = ""
    return all_hour_list

def generateAllHoursDict():
    start_hour = 00
    all_hour_dict = {}
    all_hour_dict[start_hour] = 0
    hours_sum = 24
    step = 1
    while step < hours_sum:
        step += 1
        start_hour += 1
        all_hour_dict[start_hour] = 0
    return all_hour_dict

def transformTimeZone(o, n, time):
    t_temp = time
    time_zone_step = n - o
    if time_zone_step > 0:
        if (t_temp + time_zone_step) > 23:
            t_temp += 8
            t_temp -= 24
        else:
            t_temp += 8
    return t_temp


# print(generateAllHoursList())
# print(generateAllHoursDict())
# print(transformTimeZone(0,8,2))

from redminelib import Redmine
redmine = Redmine("https://dev.seer-group.com", username = "darboy", password = "3.14159265758ch")
users = redmine.user.all()
issues = redmine.issue.all()
# print(dir(users[0])) 
#['admin', 'created_on', 'firstname', 'groups', 'id', 'issues', 'last_login_on', 'lastname', 'login', 'mail', 'memberships', 'time_entries']
# print(dir(issues[0])) 
#['assigned_to', 'attachments', 'author', 'changesets', 'children', 'closed_on', 
# 'created_on', 'custom_fields', 'description', 'done_ratio', 'due_date', 'estimated_hours', 'id', 
# 'is_private', 'journals', 'priority', 'project', 'relations', 'start_date', 'status', 'subject', 'time_entries', 'tracker', 'updated_on', 'watchers']
# print(dir(issues[0].author)) #['groups', 'id', 'issues', 'memberships', 'name', 'time_entries']
# print((users[22].lastname + users[22].firstname)) 
print(dir(issues[0].journals))
# user_list = redmine.user.all()
# print(len(user_list))
# print((issues[0].author.name)) #['groups', 'id', 'issues', 'memberships', 'name', 'time_entries']
# print((issues[0].project.name)) #['enabled_modules', 'files', 'id', 'issue_categories', 'issues', 'memberships', 'name', 'news', 'time_entries', 'time_entry_activities', 'trackers', 'versions', 'wiki_pages']

# projects = redmine.project.all()
# # print(dir(projects[0]))
# # ['created_on', 'description', 'enabled_modules', 'files', 'id', 'identifier', 'is_public', 'issue_categories', 'issues', 'memberships', 'name', 'news', 'status', 'time_entries', 'time_entry_activities', 'trackers', 'updated_on', 'versions', 'wiki_pages']
# sum = 0
# for item in projects:
#     try:
#         print(len(item.issues))
#         if item.id != 38 and item.id != 40:
#             sum = sum + len(item.issues)
#     except Exception as e:
#         print(item.name)
    
#     # # print("name is %s, id is %s" % (item.name, item.id))
# print(sum)