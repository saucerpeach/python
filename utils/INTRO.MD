## 工具类说明
***
### statisUtils.pann_Counter
Reason:  
平时，总会有这样的情景，需要统计各种次数，如：入库成功失败的次数。  
<pre><code>
count_success = 0
count_fail = 0
# 在相应的代码处添加 ++ 操作
***
count_success += 1
***
count_fail += 1
</code></pre>
呃，略有不便~So~
<p>example:  </p>

<pre><code>
test = pann_Counter()           #声明一个counter实例
test.increase_1("count_success ")
test.increase_1("count_success ")
test.increase_1("count_success ")
test.increase_1("count_fail")
print test.toString()           #格式化输出统计结果  

输出:
>count_fail:	1
>count_success:	3
</code></pre>
