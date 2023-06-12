#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: LiangjunFeng
# Mail: zhumavip@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "ba_strategy",      #这里是pip项目发布的名称
    version = "1.0",  #版本号，数值大的会优先被pip
    keywords = ("pip", "ba_strategy","featureextraction"),
    description = "A plugin based on the nonebot framework for the Granblue file main line walkthrough",
    long_description = "A plugin based on the nonebot framework for the Granblue file main line walkthrough",
    license = "MIT Licence",

    url = "https://github.com/zi-feng-0109/ba_strategy",     #项目相关文件地址，一般是github
    author = "ZiFeng",
    author_email = "2980103980@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["nonebot"]          #这个项目需要的第三方库
)

