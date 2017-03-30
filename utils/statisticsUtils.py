# -*- coding: UTF-8 -*-
# ******************************************************
# Author       : 潘涛
# Last modified: 2017-03-30
# Email        : saturnpeach@163.com
# Description  :
# ******************************************************
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class pann_Counter(object):
    def __init__(self):
        self.result = {}

    def increase_1(self,key_):
        if not self.result.has_key(key_):
            self.result[key_] = 1
        else:
            self.result[key_] += 1

    def increase_n(self,key_,n):
        if not self.result.has_key(key_):
            self.result[key_] = n
        else:
            self.result[key_] += int(n)

    def toString(self):
        return '\n'.join([str(i)+":\t"+str(self.result[i]) for i in self.result.keys()])