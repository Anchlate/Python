# -*- coding: UTF-8 -*-

# ----------> 1 变量 <----------  #

"""
Python 中的变量赋值不需要类型声明。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
"""

counter = 100   # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"   # 字符串

print counter
print miles
print name



# ----------> 2 多个变量赋值 <----------  #
# Python允许你同时为多个变量赋值。例如：

a = b = c = 1

print id(a)
print id(b)
print id(c)

# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。

#您也可以为多个对象指定多个变量。例如：
d, e, f = 1, 2, "john"
print d
print e
print f


# ----------> 3 标准数据类型 <----------  #

"""
在内存中存储的数据可以有多种类型。
例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""

# ----------> 4 Python数字 <----------  #

"""数字数据类型用于存储数值。
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number对象就会被创建："""

var1 = 1
var2 = 10

print id(var1)
print var1
print var2

var1 = 11;
print id(var1)

# 您也可以使用del语句删除一些对象的引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]

del var1
# print id(var1) 这一句会报错，var1已被删除


# 您可以通过使用del语句删除单个或多个对象的引用。例如：
var3 = 10
var5 = 11
print var3
print var5

del var3, var5

"""
Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
"""