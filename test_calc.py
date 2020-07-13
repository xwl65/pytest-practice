#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
import os
#测试文件
from pythoncode.calc import calculator
import os
import allure
import yaml

#本作用是可以用来把数据提取出来给add这个函数使用，脚本可以节省编写空间
with open("cacl.yaml") as f:
    dates = yaml.safe_load(f)
    myids=dates.keys()
    mydates=dates.values()

#如下两步结合起来当有效果，相当于把数据里面的add读写出来。效果相当的好
def get_steps():
    with open("aaa.yaml") as f:
        steps = yaml.safe_load(f)
        return steps

cal=calculator()
def steps(a,b,result):
    steps1 = get_steps()
    for step in steps1:
        if 'add' == step:
            assert result == cal.add(a,b)
        elif 'add1' == step:
            assert result == cal.add1(a,b)
        elif 'add2' ==step:
            assert  result == cal.add2(a,b)

class TestCalc:
    #def setup_class(self):
    #   self.cal = calculator()
    #@pytest.mark.flaky(rerurns=5)
    @pytest.mark.parametrize('a,b,result', mydates,ids=myids)
    def test_add(self,a,b,result):
        steps(a,b,result)
        #assert result == self.cal.add(a, b)
        #assert result == self.cal.add1(a,b)
        #assert result == self.cal.add2(a, b)
        #assert result == self.cal.add3(a, b)
    @pytest.mark.flaky(rerurns=10)
    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 3)], ids=["减法"])
    def test_subtract(self, a, b, result):
        result =a +b
        assert result == self.cal.subtract(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 76)], ids=["减法"])
    def test_subtract1(self, a, b, result):
       False

    @pytest.mark.parametrize('a,b,result', [
        (1, 2, 2)], ids=["乘法"])
    # 如果test_subtract1执行成功，那么subtract2就会被执行，如果失败，那么不会被执行。
    @pytest.mark.dependency(depends=["test_subtract1"])
    def test_subtract2(self, a, b, result):
        result = a*b
        assert result == self.cal.multiply(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 0, "ZeroDivisionError: division by zero"),
            (3,4,0.75),
            (1,2,0.5),
            (1,1,1)], ids=["除法","除法","除法","除法"])
    @pytest.mark.run(order=-999)
    def test_subtract4(self, a, b, result):
        result = a/b
        assert result == self.cal.div(a, b)
    @pytest.mark.run(order=1)
    def test_assume(self):
        print("登录")
        pytest.assume(1==2)
        pytest.assume(1 == 2)
        pytest.assume(3== 2)





