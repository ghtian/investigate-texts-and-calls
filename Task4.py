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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

""""取得所有收发短信的电话号码"""
def get_text_nums(texts):
    nums = []
    for text in texts:
        num_from = text[0]
        num_to = text[1]
        if num_from not in nums:
            nums.append(num_from)
        if num_to not in nums:
            nums.append(num_to)
    return nums

""""取得所有被呼叫的电话号码"""
def get_callto_nums(calls):
    nums = []
    for call in calls:
        num_to = call[1]
        if num_to not in nums:
            nums.append(num_to)
    return nums

""""打印电话列表，每个号码占一行"""
def printline(sales_nums):
    for num in sorted(sales_nums):
        print(num)

""""主程序"""
sales_nums=[]
usual_nums = get_text_nums(texts) + get_callto_nums(calls)
for call in calls:
    num_from = call[0]
    if num_from not in usual_nums and num_from not in sales_nums:
        sales_nums.append(num_from)
print("These numbers could be telemarketers: ")
printline(sales_nums)
