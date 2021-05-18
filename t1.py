# 什么是python
# 编程语言：解释型语言（python、js、lua）、编译型语言（java、golang）
# 什么是解释型语言：程序不需要编译，在运行的时候才翻译成机器语言，所以他是
# 每执行一次都翻译一次

# 变量、流程控制语句、函数(方法)

# python 可以动态的指定变量类型
a = 1
b = "abc"
print("a:{},b:{}".format(type(a),type(b)))

# 流程控制语句
# 1.判断语句
# if elif else
if a == 1:
    print("1")
elif a == 2:
    print("2")
else:
    print(3)

# 2.循环语句
for i in range(10):
    print(i)

while a >1:
    a -= 1

# 列表推导式
# [print (i) for i in range(10)]

for a in [[1,2],[3,4]]:
    for i in a:
        if i == 4:
            print(i)
            break
        else:
            continue

[print(i) for i in range(10) if i %2 !=0]

# 数据结构
# 元组、列表、字典

# Python的元组与列表类似，不同之处在于元组的元素不能修改。
d = (1,2,3)

# 列表
f = [1,3,3]
f.append(4)

f.remove(3)
f.pop()
print(f)

# 字典 键值对类型的数据库，类似java的map
d = {"znn":1,"cb":2}
# 迭代
for k,v in d.items():
    print("key:{},value:{}".format(k,v))
print(d.keys(),d.values())
print(d.get("znn"))

# 方法
def say_hello():
    print("hello")
say_hello()

def get_hello():
    return 'hello'
h = get_hello()
print(h)

def get_input(p:str):
    print(p)

get_input("abc")

# 类

class znn:
    def __init__(self) -> None:
        self.znn='2'
    def change_s(self):
        self.znn='3'
    def say_hello(self):
        print("hello i am in class")
    def start(self,input_str):
        # znn = '4'
        # self.change_s()
        # print(self.znn)
        # print(znn)
        # print(input_str)
        print("-"*100)
        self.say_hello()
        say_hello()
z = znn()
z.start('b')

#作业 构造一个类，初始化一个字典{"znn":1,"cb":2}，类里的方法可以解析字典
