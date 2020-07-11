#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
# 实现计算机
class calculator:

    def add(self, a, b):
        a=input()
        b=input()
        return a + b
    def div(self, a, b):
        return a / b

    def subtract(selfl,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def div(self,a,b):
        if b== 0 :
            return "非法输入"
        else:
            return a/b
