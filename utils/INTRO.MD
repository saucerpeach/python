## 工具类说明
***
### statisUtils.pann_Counter
Reason:

平时，总会有这样的情景，需要统计各种次数，如：入库成功失败的次数。  
count_success = 0;count_fail = 0  
在相应的代码处添加 ++ 操作。呃，略有不便~

example:  
test = pann_Counter()  
\#声明一个counter  
test.increase_1("True")  
test.increase_1("True")  
test.increase_1("True")  
test.increase_1("False")  
print test.toString()  
\#格式化输出统计结果  
输出  
\>False:	1  
\>True:	3
