import pandas as pd
import re

# 初步处理告警信息
def chuliTrigger(x):
    x = re.search(r"(主机node_[0-9]+)(.*)", x).group(2)
    x = "".join(x.split(" "))
    
  
    if re.search(r"url:http://node_[0-9]+:[0-9]+(//)?访问失败", x):
        x = "".join(re.search(r"(url):http://node_[0-9]+:([0-9]+.*)", x).groups())

    if re.search(r"HTTP:http://\*\*\*\*\*\*\*\*\*\*\*\*\*，慢响应（调用耗时超过1000ms）次数：.*", x):
        x = "".join(re.search(r"(HTTP:http)://\*\*\*\*\*\*\*\*\*\*\*\*\*，(慢响应)（调用耗时超过1000ms）次数：.*", x).groups())
    if re.search(r'空闲CPU为.*', x):
        x = "CPU利用率过高"

    if re.search(r"网卡eth0发送流量持续.*", x):
        x = "网卡发送流量过高"

    if re.search(r"网卡eth0接收流量持续.*", x):
        x = "网卡接收流量过高"

    if re.search(r"sd(a|b|d)IO使用率.*", x):
        x = "磁盘I/O异常"

    if re.search(r"FullGC平均耗时：.*", x):
        x = "FullGC平均耗时异常"

    if re.search(r"FullGC次数：.*", x):
        x = "FullGC次数异常"

    if re.search(r"堆内存平均使用率：.*（大于阈值：90%）", x):
        x = "堆内存平均使用率大于阈值"
    if re.search(r"上.*", x):
        x = x[1:]
    return x



def chuli(df):
    del df['Unnamed: 0']
    df['trigger'] = df['triggername'].apply(lambda x: chuliTrigger(x))
    df['node'] = df['triggername'].apply(lambda x:  re.search(r"(主机node_[0-9]+)(.*)", x).group(1)[2:])
    del df['triggername']
    #print(df)
    return df

for i in range(0,100):
    df = pd.read_csv("./data_release/train/"+str(i)+".csv")
    df = chuli(df)
    df.to_csv("./data_release/pre_train/"+str(i)+".csv", encoding='utf_8_sig')