#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021-09-14 11:05
# @Author : Lionel
# @Version：V 0.1
# @File : CarNetworking.py
# @desc :==============================================

import unittest
from CarNetworking.common import common


class CarNetworking(unittest.TestCase):

    common = common.CommonWay()
    common.openDriver()

    def test_loginr(self):
        self.common.login('TSP后台自动化用例.xlsx', 'loginr', 1, 1)

    def test_login(self):
        self.common.login('TSP后台自动化用例.xlsx', 'login', 2, 'maxrow')

    def test_VehicleInf(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'VehicleInf', '/html/body/div[1]/div[2]/ul/li[2]',
                    '/html/body/div[1]/div[2]/ul/li[2]/dl/dd[1]/a', 2, 12)
        self.common.screen('TSP后台自动化用例.xlsx', 'VehicleInf', 13, 'maxrow')

    def test_dealerinf(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'dealerinf', '/html/body/div[1]/div[2]/ul/li[2]',
                    '/html/body/div[1]/div[2]/ul/li[2]/dl/dd[2]/a', 2, 24)
        self.common.screen('TSP后台自动化用例.xlsx', 'dealerinf', 25, 'maxrow')

    def test_careq(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'careq', '/html/body/div[1]/div[2]/ul/li[3]',
                    '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[1]/a', 2, 25)
        self.common.screen('TSP后台自动化用例.xlsx', 'careq', 26, 'maxrow')

    def test_SIM(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'SIM', '/html/body/div[1]/div[2]/ul/li[3]',
                    '/html/body/div/div[2]/ul/li[3]/dl/dd[2]/a', 2, 22)
        self.common.screen('TSP后台自动化用例.xlsx', 'SIM', 23, 'maxrow')

    def test_carstate(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'carstate', '/html/body/div[1]/div[2]/ul/li[3]',
                    '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[3]/a', 2, 19)
        self.common.screen('TSP后台自动化用例.xlsx', 'carstate', 20, 'maxrow')

    def test_XSGJ(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'XSGJ', '/html/body/div[1]/div[2]/ul/li[3]',
                    '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[4]/a', 2, 13)
        self.common.screen('TSP后台自动化用例.xlsx', 'XSGJ', 14, 'maxrow')

    def test_alarminf(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'alarminf', '/html/body/div[1]/div[2]/ul/li[3]',
                    '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[5]/a', 2, 16)
        self.common.screen('TSP后台自动化用例.xlsx', 'alarminf', 17, 'maxrow')

    def test_SXXX(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'SXXX', '/html/body/div[1]/div[2]/ul/li[3]', '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[6]/a', 2, 24)
        self.common.screen('TSP后台自动化用例.xlsx', 'SXXX', 25, 'maxrow')

    def test_message(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'message', '/html/body/div[1]/div[2]/ul/li[3]', '/html/body/div[1]/div[2]/ul/li[3]/dl/dd[7]/a', 2, 8)
        self.common.screen('TSP后台自动化用例.xlsx', 'message', 9, 'maxrow')

    def test_appuser(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'appuser', '/html/body/div[1]/div[2]/ul/li[4]', '/html/body/div[1]/div[2]/ul/li[4]/dl/dd[1]/a', 2, 22)
        self.common.screen('TSP后台自动化用例.xlsx', 'appuser', 23, 31)
        self.common.addUser('TSP后台自动化用例.xlsx', 'appuser', 32, 49)
        self.common.compileUser('TSP后台自动化用例.xlsx', 'appuser', 50, 58)

    def test_appmessage(self):
        self.common.uiTest('TSP后台自动化用例.xlsx', 'appmessage', '/html/body/div/div[2]/ul/li[4]', '/html/body/div[1]/div[2]/ul/li[4]/dl/dd[2]/a', 2, 13)
        # self.common.screen('TSP后台自动化用例.xlsx', 'appmessage', 14, 21)
        self.common.messageCreate('TSP后台自动化用例.xlsx', 'appmessage', 22, 31)


if __name__ == '__main__':
    unittest.main(verbosity=2)
