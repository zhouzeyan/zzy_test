#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ==== # ==== # ==== # ==== 
# __author__ = "Brenda.Zhou"  
# QQ:2423812308  
# FileName: *.py  
# Version:3.6.5  
# ==== # ==== # ===== # ====


class A():
    # 在调用A类时，首先会执行它的__init__()方法，所以要对其进行传参。初始化所做的事情就是将输入的参数转化为int类型，这样可以在一定程度上保证程序的容错性。而
    # add（）方法可以直接拿初始化方法__init__的self.a和self.b两个参数进行计算，于是add方法无须再进行传参
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


count = A('4', 5)
print(count.add())
