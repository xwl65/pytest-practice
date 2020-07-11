#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
#测试文件
from calc import calculator

import allure

class TestCalc:
    def setup_class(self):
        self.cal = calculator()
    @pytest.mark.parametrize('a,b,result',[
    (1,1,2)],ids=["int"])
    def test_add(self,a,b,result):

        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2)], ids=["加法"])
    def test_subtract(self, a, b, result):
        result =a +b
        assert result == self.cal.subtract(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2)], ids=["减法"])
    def test_subtract(self, a, b, result):
        result = a -b
        assert result == self.cal.subtract(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 2, 2)], ids=["乘法"])
    def test_subtract(self, a, b, result):
        result = a*b
        assert result == self.cal.multiply(a, b)

    @pytest.mark.parametrize('a,b,result', [
        (1, 0, "ZeroDivisionError: division by zero")], ids=["除法"])
    def test_subtract(self, a, b, result):
        result = a/b
        assert result == self.cal.div(a, b)