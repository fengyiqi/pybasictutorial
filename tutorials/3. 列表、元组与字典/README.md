# 列表、元组与字典

列表、元组和字典是Python的三个最基本的数据组织形式，在平时的使用中非常普遍，尤其列表。

## 一、列表

列表是什么？列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。在Python中，用方括号`[]`来表示列表，并用逗号来分隔其中的元素。比如：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
列表是一系列数据元素的打包，目的是使用更加方便。很多情况下我们需要获取列表中某个元素，这时需要用到一个叫做`索引`的东西，比如我们想拿到第一个数据，请看下面代码：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'第一个元素是：{bicycles[0]}')
```
这段代码执行的结果是在输出窗口中打印了`trek`。这里需要注意的是，索引是从0开始，而不是从1开始。`bicycles[0]`表示这个列表的第1个元素，那么`bicycles[3]`即表示这个列表的第四个元素`specialized`。

Python还提供了快速获取最后一个元素的方法，即传入索引`-1`：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'最后一个元素是: {bicycles[-1]}')
```

有的时候我们想获得若干个连续的元素，比如我们想获得bicycles中第二个到最后一个的元素，我们可以用`切片`的方式，即使用`:`来进行分割。

对切片方法的使用是个重点同时也是难点。举个例子，`1:4`，这里的1代表起始索引，即第2个元素，这个很好理解；那么后面的4代表第5个元素吗？其实如果在正常的索引使用中，比如`bicycles[4]`确实是代表第五个元素，这个没什么毛病。但是在切片中，这里的`4`是指`直到索引4的元素的前一个元素`。比如这个`1:4`其实是指`bicycles[1], bicycles[2], bicycles[3]`这三个元素，我们来看下面这个例子：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'giant']
# 获取第二个到第四个元素，即'cannondale', 'redline', 'specialized'
print(f'第二个到第四个元素: {bicycles[1:4]}')  
```

大家可以试试取不同值时会有什么变化。

在使用切片时还可以使用一些省略写法比如：
- 如果`:`的前面或者后面不写数字，则代表第一个或最后一个，比如：
  - `:4` 表示从第一个到第四个
  - `2:` 表示从第三个到最后一个
- `:-1`表示的是从第一个到倒数第二个（-1是最后一个，但是用在切片时，后面的元素要前进一位）


### 列表的增删改查

#### 1. 增删

在末尾增删，使用`append()`和`pop()`方法，比如
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('giant')  # 在列表末尾增加, 需要传入增加的元素'giant'
print(f'末尾增加元素后的列表：{bicycles}')
bicycles.pop()  # 在列表末尾删除，不需要传入参数
print(f'末尾删除元素后的列表：{bicycles}')
```

在任意位置增删，使用`insert()`和`remove()`方法，比如想在第二个和第三个元素之间添加`giant`：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(1, 'giant')  # 需要传入两个参数，第一个是位置，第二个是要插入的元素
print(f'在第二个和第三个元素之间添加元素后的列表：{bicycles}')
```
> 大家请注意，我们增加了一个元素之后，新元素之前的元素的索引保持不变，但是新元素后边的索引都会+1，这是由于位置向后移动了一位造成的。

如果想删除原bicycles列表中`redline`元素，可以写如下代码：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.remove('redline')  # 只传入要删除的元素
print(f"删除'redline'后的列表：{bicycles}")
```
> 这里大家注意两点，一是单引号双引号的交替使用，二是删除一个元素后，后边的元素也会向前移动一位。

如果我们不知道某个元素的名字，只知道它的位置，可以像下面这样写：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[2]  # 使用del删除特定位置（索引为2）的元素
print(f"删除第三个元素后的列表：{bicycles}")
```

#### 2. 修改

修改列表的元素很方便，相信大家这么聪明，一看就会，比如下面的代码是将`redline`修改为`giant`：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[2] = 'giant'  # 将bicycles第三个元素修改为giant
print(f"修改后的列表：{bicycles}")
```

#### 3. 查找

如果我们想查询一个元素是否在列表里，我们可以使用关键字`in`，比如：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
trek_exit = 'trek' in bicycles  # trek是否在bicycles里？
giant_exit = 'giant' in bicycles  # giant是否在bicycles里？
print(f"trek是否在bicycles里? {trek_exit}")
print(f"giant是否在bicycles里? {giant_exit}")
```
> 说明：这样的查询会返回布尔型数据，即`True`和`False`

如果我们想知道某一个元素在列表中的位置，可以这样写：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
redline_index = bicycles.index('redline')
print(f"redline在列表中的索引是：{redline_index}")
```

#### 4. 排序
我们在平时的使用中会经常用到排序，Python也提供了一个很方便的排序方法`sort()`，比如我们有一个由数字组成的列表，将它排序：
```python
number = [1, 7, 3, 2, 6, 4, 5]
number.sort()  # sort不传入参数时是升序
print(f'按照升序排列number：\n{number}')
number.sort(reverse=True)  # sort传入reverse=True时是降序
print(f'按照降序排列number：\n{number}')
```
