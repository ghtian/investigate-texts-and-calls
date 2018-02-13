"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
"""取得各电话的通话总时长"""
num_totaltime={}
for call in calls:
    num_from=call[0]
    num_to=call[1]
    time=int(call[3])
    if num_from not in num_totaltime.keys():
        num_totaltime[num_from]=time
    else:
        num_totaltime[num_from]+=time
    if num_to not in num_totaltime.keys():
        num_totaltime[num_to]=time
    else:
        num_totaltime[num_to]+=time

""""取得最大时长与对应的号码集"""
nums=[]
max_totaltime=max(num_totaltime.values())
for num,time in num_totaltime.items():
    if time==max_totaltime:
        nums.append(num)

""""改变号码的展现方式，因为可能存在多个号码"""
num_msg=""
for num in nums:
    num_msg+=num+" "

"""输出结果"""
msg="{}spent the longest time, {} seconds, on the phone during September 2016.".format(num_msg,max_totaltime)
print(msg)
