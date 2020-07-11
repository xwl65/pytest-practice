#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
#测试文件
from calc import calculator


class TestCalc:
    def setup_class(self):
        self.cal = calculator()
    @pytest.mark.parametrize('a,b,result',[
    (1,1,2)],ids=["int","int"])
    def test_add(self,a,b,result):

        assert result == self.cal.add(a, b)

