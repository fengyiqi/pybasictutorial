# 函数

一听到函数，大家往往会联想到初高中数学课上，面对各种各样五花八门的函数而不知所谓。如果说Python的函数跟数学中的函数有点相似之处，你们会不会被吓跑？其实不用担心，Python中的函数是一种更为广义的函数，怎么解释呢。首先我们看一个数学中最简单的二次函数:
<img src="http://chart.googleapis.com/chart?cht=tx&chl= f(x) = x^2" style="border:none;">或者
<img src="http://chart.googleapis.com/chart?cht=tx&chl= y = x^2" style="border:none;">。
这两个函数本质是一样的，只不过
<img src="http://chart.googleapis.com/chart?cht=tx&chl= f(x)" style="border:none;">
更强调一种映射关系，而y强调计算得到的值。

这个函数有一个自变量x，一个对x的计算
<img src="http://chart.googleapis.com/chart?cht=tx&chl=x^2" style="border:none;">，
还有一个用来存储
<img src="http://chart.googleapis.com/chart?cht=tx&chl=x^2" style="border:none;">
计算结果的y。

在Python中函数，其实更为广义，它是一个可以完成具体操作的代码块。如果某项操作是要被反复执行的，区别仅仅是一些初始值不同，那么我们完全可以将这项操作写成函数，并在其他代码中调用它，而不用每次使用时都要重写一遍。

一个完整的函数也基本上由上述三部分，即参数、函数体，返回值，再加一个函数名构成。需要特别指出的是，Python中的函数可以没有参数，也可以没有返回值，但不能没有函数体（可以只写一个`pass`代表什么操作也没有，但这也是函数体）和名字。具体情况依具体问题而定。


## 1. 定义函数

定义函数使用`def`关键字，并且函数体采用缩进的方式表示。下面是一个没有参数没有返回值的函数，操作仅仅是打印`Hello world!`。因为没有参数没有返回值，对这个函数直接调用就可以。
```python
def greeting():
    print('Hello world!')

greeting()
greeting()
greeting()
```
通过调用函数，让我们少打了好多代码。

如果函数传入参数，会大大扩展函数的功能，比如下面这个类似询价的函数，通过传入一个车的品牌，打印车的产地，顺便带大家回忆一下字典的使用。
```python
def get_origin(car):
    origin_dict = {'Benz': '德国',
                   'Audi': '德国', 
                   'BMW': '德国', 
                   'Toyota': '日本', 
                   'BYD': '中国'}
    print(f'{car}的产地是{origin_dict[car]}')

get_origin('Audi')
get_origin('BYD')
```
在调用`get_origin()`函数时，要求传入车的名字（字符串）作为参数，在函数中创建了一个字典，根据传入的参数作为键值来获取相应的产地。
> 刚刚这个函数中`orgin_dict`会在函数被调用时创建，并在函数调用结束时销毁，即打印完产地后就消失不见了。

下面这个函数是既有参数又有返回值的函数，作用基本与上述函数相同，但返回了车的产商所在的国家。返回值使用`return`关键字，想返回什么就在`return`后面加什么。

有了这个国家的信息，就可以使用它做后续的处理，比如打印国家所在的洲。同时，在调用函数时也要有个变量去接收它，比如下面的在函数体外的`country`。
```python
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
```

函数的参数可以有多个，比如我们创建一个获取汽车报价的函数，这个函数除了传入汽车的品牌名，还需要传入一个是否打印产地的布尔值，即`True`就打印，`False`就不打印。
```python
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
```


## 2. 参数默认值

对于上面获得汽车报价的函数，可能对于大部分人来说是不需要打印汽车产地的，但会有很少一部分人是不了解产地信息的。对于前者来说，如果我们在每次调用`get_price()`函数时都要写上`print_origin=False`未免太麻烦了，这显然不是Python的风格，所以这里我们介绍参数默认值。

某个参数如果有默认值，表示在调用函数时，可以不输入这个参数的值，这种情况下这个参数采用默认值。只有在明确指定了这个参数的值时，默认值才会被覆盖掉。比如对于刚刚我们提的问题，我们可以将参数`print_origin`的默认值设为`False`，这样对于大部分人来说就不需要管这个参数了，只有个别的人需要显式地指定`print_origin`为`True`。

指定默认值的方法是在参数列表中给这个参数赋值，同时要特别注意的是，带有默认值的参数一定要放在无默认值参数的后面，请参照下面这个例子：

```python
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
```

> - 这里前两次调用函数`get_price`没有指定`print_origin`的值，所以函数采用默认值，即不打印。第三次调用时指定了`print_origin`为`True`，所以原默认值被覆盖，`print_origin`按照`True`来执行。
> - 带有默认值的函数非常常见，大家要熟练掌握。

## 3. 排序函数

大家是否还记得上一节的排序函数？在最后我提了一个问题，如果降序排列的话需要修改哪里？其实只要将小于号换成大于号就可以啦。

我们现在应用今天所学的知识，将上一节的排序算法封装成一个函数，并且通过传入一个叫做`reverse`的参数来觉得是升序还是降序，默认值为升序，并且返回排序后的列表。

因为列表有自带的排序函数，叫`sort()`，不知大家是否还记得。忘记的小伙伴请点击[这里]()。这个内置的排序函数要比我们上节课实现的算法高效，但我们是为了学习，所以效率暂时无所谓。在这里将我们的排序算法命名为`my_sort`

我们只用第一个算法作为例子，希望大家能够将第二个算法也修改为满足上述要求的函数。下面的代码中有两行不太好理解的地方，已由`###`标注，代码下面有解释。

```python
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
```
- `values_ = values.copy()`是将参数`value`的值复制给了`values_`。这种在变量名后面加`_`的方法很常见，常用来表示一份拷贝，或者二者意思一样，但名字已经被占用的情况。那么这里为什么要拷贝一份呢？因为我们在排序时，会逐渐删掉原始列表，也就是参数`values`的列表中的元素，如果我们不做一份拷贝，函数外面的`values = [5, 2.7, 8.2, 7, 23.9, 23.8, 11, 29, 11, 40, -3]`会被删成空列表，就没法复用了。所以大家要记住，如果函数中有对传进来的参数进行处理的话，一定要做个拷贝。
- `if not reverse and value < base:`其实不难理解，大家只要记住`not reverse`是升序，`and`表示两个条件都必须满足就可以了。这行的意思是“如果是升序并且当前值比基准值还小”。下面的`if reverse and value > base:`可以以此类推。
