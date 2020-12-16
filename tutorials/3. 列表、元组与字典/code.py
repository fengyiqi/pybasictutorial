# -*- coding: utf-8 -*-


# 1. 列表

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
print(cars)

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
print(f'第一个元素是：{cars[0]}')

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
print(f'最后一个元素是: {cars[-1]}')

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
# 获取第二个到第四个元素，即'Audi', 'BMW', 'Toyota'
print(f'第二个到第四个元素: {cars[1:4]}') 


# 1.1 列表的增删改查

# - 增删

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
cars.append('Honda')  # 在列表末尾增加, 需要传入增加的元素'Honda'
print(f'末尾增加元素后的列表：{cars}')
cars.pop()  # 在列表末尾删除，不需要传入参数
print(f'末尾删除元素后的列表：{cars}')

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
cars.insert(1, 'Honda')  # 需要传入两个参数，第一个是位置，第二个是要插入的元素
print(f'在第二个和第三个元素之间添加元素后的列表：{cars}')

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
cars.remove('Toyota')  # 只传入要删除的元素
print(f"删除'Toyota'后的列表：{cars}")

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
del cars[2]  # 使用del删除第三个（索引为2）元素
print(f"删除第三个元素后的列表：{cars}")

# - 修改

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
cars[3] = 'Honda'  # 将cars第四个元素修改为Honda
print(f"修改后的列表：{cars}")

# - 查找

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
benz_exist = 'Benz' in cars  # Benz是否在cars里？
bmw_exist = 'BMW' in cars  # BMW是否在cars里？
honda_exist = 'Honda' in cars  # Honda是否在cars里？
print(f"Benz是否在cars里? {benz_exist}")
print(f"BMW是否在cars里? {bmw_exist}")
print(f"Honda是否在cars里? {honda_exist}")

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
audi_index = cars.index('Audi')
print(f"Audi在列表中的索引是：{audi_index}")

# - 排序

number = [1, 7, 3, 2, 6, 4, 5]
number.sort()  # sort不传入参数时是升序
print(f'按照升序排列number：\n{number}')
number.sort(reverse=True)  # sort传入reverse=True时是降序
print(f'按照降序排列number：\n{number}')


# 2. 元组

a = (1, 2, 3, 4, 5)
print(f'元组a的第二个元素是a[1]')
# 由于元组无法修改，所以下面这句话会报错
# a[1] = 6


# 3. 字典

exam = {'姓名': '张三', '学号': 202018942, '成绩': 87, '备注': None}
# 注意下面引号的使用
print(f"这是{exam['姓名']}的试卷，学号是{exam['学号']}，考试成绩为{exam['成绩']}")

exam['姓名'] = '李四'
exam['学号'] = 202018944
exam['成绩'] = 92
exam['性别'] = '男'
exam.pop('备注')
print(exam)

print(f'exam的键有{exam.keys()}')
print(f'exam的值有{exam.values()}')