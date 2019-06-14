# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 11:25
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : main.py
# @Software : PyCharm
import pytest
from Common import dir_config
from Common.send_email import sendEmail

pytest.main(["--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])
# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--junitxml=TestResult/reports/report.xml"])
# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])


#执行完毕之后，发送测试报告
sendEmail().send_email('liqi_629@163.com',dir_config.report_path)