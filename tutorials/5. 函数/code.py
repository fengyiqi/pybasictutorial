# -*- coding: utf-8 -*-


# 函数

# 1. 定义函数

# 无参数无返回值
print('-----无参数无返回值-----')
def greeting():
    print('Hello world!')

greeting()
greeting()
greeting()

# 有参数无返回值
print('-----有参数无返回值-----')
def get_origin(car):
    origin_dict = {'Benz': '德国',
                   'Audi': '德国', 
                   'BMW': '德国', 
                   'Toyota': '日本', 
                   'BYD': '中国'}
    print(f'{car}的产地是{origin_dict[car]}')

get_origin('Audi')
get_origin('BYD')

# 有参数有返回值
print('-----有参数有返回值-----')
def get_origin(car):
    origin_dict = {'Benz': '德国',
                   'Audi': '德国', 
                   'BMW': '德国', 
                   'Toyota': '日本', 
                   'BYD': '中国'}
    country = origin_dict[car]
    print(f'{car}的产地是{country}')
    return country

country = get_origin('Audi')
if country == '德国':
    print(f'{country}位于欧洲')
if country == '日本' or country == '中国':
    print(f'{country}位于亚洲')
    
# 具有两个参数的函数
print('-----具有两个参数的函数-----')
def get_price(car, print_origin):
    car_info = {'Benz': [500000, '德国'],
                'Audi': [400000, '德国'], 
                'BMW': [450000, '德国'], 
                'Toyota': [100000, '日本'], 
                'BYD': [80000, '中国']}
    print(f'{car}的价格是{car_info[car][0]}')
    if print_origin:
        print(f'{car}的产地是{car_info[car][1]}')

get_price('BMW', print_origin=True)
get_price('Toyota', print_origin=False)


# 2. 参数默认值
print('-----参数默认值-----')
def get_price(car, print_origin=False):
    car_info = {'Benz': [500000, '德国'],
                'Audi': [400000, '德国'], 
                'BMW': [450000, '德国'], 
                'Toyota': [100000, '日本'], 
                'BYD': [80000, '中国']}
    print(f'{car}的价格是{car_info[car][0]}')
    if print_origin:
        print(f'{car}的产地是{car_info[car][1]}')

get_price('BMW')
get_price('BYD')
get_price('Toyota', print_origin=True)


# 3. 排序函数
print('-----排序函数-----')
def my_sort(values, reverse=False):

    sorted_values = []           
    values_ = values.copy()  ###
    while len(values_) != 0:
        base = values_[0]
        for value in values_: 
            if not reverse and value < base:  ###
                base = value
            if reverse and value > base:
                base = value
        sorted_values.append(base)  
        values_.remove(base)  

    return sorted_values

values = [5, 2.7, 8.2, 7, 23.9, 23.8, 11, 29, 11, 40, -3]

sorted_values = my_sort(values)
print(sorted_values)

sorted_values_reverse = my_sort(values, reverse=True)
print(sorted_values_reverse)
