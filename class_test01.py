#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ==== # ==== # ==== # ==== 
# __author__ = "Brenda.Zhou"  
# QQ:2423812308  
# FileName: *.py  
# Version:3.6.5  
# ==== # ==== # ===== # ====


class A():

    def add(self, a, b):
        return a+b

# 创建A类和A的方法add，创建B类，继承A类，所以B拥有了A的add()函数
class B(A):

    def sub(self,a,b):
        return a-b


print(B().add(4, 5))