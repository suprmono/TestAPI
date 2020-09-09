import unittest
from HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_mail

logging.info("====================== 测试开始 =======================")
suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, 'wb') as f:
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="zjk").run(suite)

# send_mail(report_file)
logging.info("======================= 测试结束 =======================")