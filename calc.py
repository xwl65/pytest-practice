#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
# 实现计算机
class calculator:

    def add(self, a, b):
        return a + b
    def div(self, a, b):
        return a / b

    def subtract(selfl,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def div(self,a,b):


        if b == 0:
            raise Exception("非法输入", )
            # 触发异常后，后面的代码就不会再执行
        else:
            return  a/b
