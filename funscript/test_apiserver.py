# -*- coding:utf-8 -*-
# @Time    : 2019/11/13 19:16
# @Author  : zengln
# @File    : test_apiserver.py

import requests
import os
from .base import ApiServerUnittest
from . import test_runner, utils


class TestApiServer(ApiServerUnittest):

    def setUp(self):
        super(TestApiServer, self).setUp()
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        self.clear_user()

    def tearDown(self):
        super(TestApiServer, self).tearDown()

    # def test_create_user_not_existed(self):
    #     self.clear_user()
    #
    #     url = "%s/api/users/%d" % (self.host, 1000)
    #     data = {
    #         "name": "user1",
    #         "password": "123456"
    #     }
    #     resp = self.api_client.post(url, json=data)
    #
    #     self.assertEqual(200, resp.status_code)
    #     self.assertEqual(True, resp.json()["success"])

    def clear_user(self):
        url = "%s/api/reset-all" % (self.host,)

        resp = self.api_client.get(url)
        self.assertEqual(True, resp.json()['success'])

    def test_run_test_single_testcase_success(self):
        testcase_file_path = os.path.join(os.getcwd(), "funscript\\tests\\create_user_not_existed.json")
        testcase = utils.load_testcases(testcase_file_path)
        success, _ = test_runner.run_single_testcase(testcase)
        self.assertTrue(success)