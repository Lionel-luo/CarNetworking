#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021-09-14 11:05
# @Author : Lionel
# @Version：V 0.1
# @File : run.py
# @desc :==============================================

import HTMLTestRunner
import unittest
from time import strftime, localtime, time
from CarNetworking.Test_Case import CarNetworking

suite = unittest.TestSuite()
# suite.addTest(CarNetworking.CarNetworking('test_loginr'))
suite.addTest(CarNetworking.CarNetworking('test_login'))
suite.addTest(CarNetworking.CarNetworking('test_VehicleInf'))
suite.addTest(CarNetworking.CarNetworking('test_dealerinf'))
suite.addTest(CarNetworking.CarNetworking('test_careq'))
suite.addTest(CarNetworking.CarNetworking('test_SIM'))
suite.addTest(CarNetworking.CarNetworking('test_carstate'))
suite.addTest(CarNetworking.CarNetworking('test_XSGJ'))
suite.addTest(CarNetworking.CarNetworking('test_alarminf'))
suite.addTest(CarNetworking.CarNetworking('test_SXXX'))
suite.addTest(CarNetworking.CarNetworking('test_message'))
suite.addTest(CarNetworking.CarNetworking('test_appuser'))
suite.addTest(CarNetworking.CarNetworking('test_appmessage'))


if __name__ == '__main__':
    # 执行测试
    runner = unittest.TextTestRunner()
    now = strftime("%Y-%m-%d %H-%M", localtime(time()))
    # 当前时间
    report_path = "D:/CarNetworking/CarNetworking/Test_Report/" + now + "result.html"
    # 文件名
    fp = open(report_path, 'wb')
    # 已二进制的方式打开文件并写入结果
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="车联网TSP后台UI测试",
        description="该测试限于车联网TSP后台UI自动化测试，且仅显示用例是否通过，具体结果需查看excel内结果")
    runner.run(suite)
    fp.close()
