###检查字符串是否IP###
"""
def is_ip(ip):
    num_list = ip.split('.')
    for num in num_list:
        if not num.isdigit() or not 0 <= int(num) <= 255:
            return False
    return True


print(is_ip('101.1.0.201'))

###使用map函数

def check_ipv4(str):
    ip = str.strip().split(".")
    return False if len(ip) != 4 or False in map(lambda x: True if x.isdigit() and 0 <= int(x) <= 255 else False,
                                                 ip) else True
print(check_ipv4('101.1.0.201'))
"""

# import xlrd
#
# wb = xlrd.open_workbook('test_user_data.xlsx')
#
# sh = wb.sheet_by_name('TestUserLogin')
#
# print(sh.nrows)  # 有效数据行数
#
# print(sh.ncols)  # 有效数据列数
#
# print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
#
# print(sh.row_values(0))  # 输出第1行的所有值（列表格式）
#
# # 将数据和标题组装成字典
# print(dict(zip(sh.row_values(0), sh.row_values(1))))
#
# # 遍历excel,打印所有的数据
# for i in range(sh.nrows):
#     print(sh.row_values(i))


