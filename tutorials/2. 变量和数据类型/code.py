# -*- coding: utf-8 -*-


# 1. 字符串, string

message = "Hello Python world!"
print(message)

message = "Hello 'Python' world!"
print(message)

message = "Hello " + "Python world!"
print(message)

message = "Hello! \nPython world!"
print(message)


# 2. 整型, int

a = 2
b = 3
print(a + b, a - b, a * b, a / b, a ** b)  # '**'表示乘方运算，即a的b次方


# 3. 浮点型，float

a = 2.5  # a为浮点型数据
b = 3    # b为整形数据
print(a + b, a - b, a * b, a / b, a ** b)  # '**'表示乘方运算，即a的b次方

# 整型转成字符串型
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
# ---------------------------------------------
# 浮点型转成整型，即去掉小数部分，本质是向0取整
a = -1.3
b = 2.5
a_int = int(a)  # 使用a_int这个名字表示a经int转换之后的值
b_int = int(b)
print("取整后的a和b为：\n", a_int, b_int)


# 4. 布尔型，bool


# print()函数的扩展

a = -1.3
b = 2.5
a_int = int(a)  # 使用a_int这个名字表示a经int转换之后的值
b_int = int(b)
print(f"取整后的a为{a_int}, 取整后的b为{b_int}")