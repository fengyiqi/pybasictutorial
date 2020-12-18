# -*- coding: utf-8 -*-


# 1.判断

a = 8
if a <= 10:
    print('a小于等于10')
else:
    print('a大于10')
    
a = 8
if a < 10 or a == 10:  # 更上面的例子是一个意思，但这里只是为了说明
    print('a小于等于10')
else:
    print('a大于10')
    
a = 8
if not (a > 10):  # 不确定执行顺序的时候，毫不犹豫地加括号上去
    print('a小于等于10')
else:
    print('a大于10')
    
a = 8
if a <= 5:
    print('a小于等于5')
elif a > 5 and a <= 10:
    print('a大于五小于等于10')
else:
    print('a大于10')
    

# 2. 循环
print('-----2. 循环-----') 

# for循环
print('-----for循环-----') 

cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
for i in range(len(cars)):
    print(cars[i])
    
cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
print(f'len(cars)的结果为：{len(cars)}')
for i in range(len(cars)):
    print(f'此时i为：{i}')
    print(cars[i])
    
cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
for i in cars:
    print(i)
    
cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
for car in cars:
    print(car)
    
# while循环
print('-----while循环-----')   
 
cars = ['Benz', 'Audi', 'BMW', 'Toyota', 'BYD']
i = 0
while i <= 4:
    print(cars[i])
    i = i + 1


# 3. 判断与循环的综合应用：排序
print('-----3. 判断与循环的综合应用：排序-----')    


values = [5, 2.7, 8.2, 7, 23.9, 23.8, 11, 29, 11, 40, -3]
sorted_values = []           # 初始化一个空列表用于存放当前最小值

while len(values) != 0:      # 只要values不为空，就循环
    minimum = values[0]      # 先选取values第一个值为基数
    for value in values:     # 遍历values中所有值
        if value < minimum:  
            minimum = value  # 如果这个值比基数小，就更新基数
    # 遍历完当前values后，确定了最小值，将这个最小值存入sorted_values
    sorted_values.append(minimum)  
    # 从当前values中删除这个最小值，因为不需要它参与后续的比较。
    # 此时values减少一个元素
    values.remove(minimum)  

print(sorted_values)


values = [5, 2.7, 8.2, 7, 23.9, 23.8, 11, 29, 11, 40, -3]

for i in range(len(values)):  
    for j in range(i, len(values)):
        if values[i] > values[j]:
            temp = values[i]
            values[i] = values[j]
            values[j] = temp

print(values)
