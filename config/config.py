import logging
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(prj_path, 'data')
test_path = os.path.join(prj_path, 'test')

log_file = os.path.join(prj_path, 'log', 'log.txt')
report_file = os.path.join(prj_path, 'report', 'report.html')

# log 配置
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', # log格式
    datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
    filename=log_file, # 日志输出文件
    filemode='a' # 追加模式
)

# 数据库配置
db_host = '127.0.0.1'
db_port = 1433
db_user = 'sa'
db_password = '123'
db = 'cmp'

# 邮件配置
from_addr = 'zjk@bsw.com.cn'
password = 'SUPERmono1324'
to_addr = '635069882@qq.com'
smtp_server = 'smtp.exmail.qq.com'  # 发信服务器
subject = '接口测试报告'

if __name__ == '__main__':
    logging.info('hello world!')