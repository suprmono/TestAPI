import requests
import json
import os
import unittest
from config.config import *
from lib.case_log import log_case_info
from lib.read_excel import *


class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserLogin")

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list, "test_user_login_normal")
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data.get('url')
        data = eval(case_data.get('data'))  # 注意字符串格式，需要用json.loads()/eval()转化为字典格式
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.text, expect_res)
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
