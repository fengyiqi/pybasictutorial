# 变量和数据类型

## 变量

变量是数据的载体，可以简单理解为一个数据的标签或者代称。我们修改一下上次Hello world的代码：
```Python
message = "Hello Python world!"
print(message)
```
这里`message`就是"Hello Python world!"这段话的代称。这里`print(message)`其实就是`print('Hello Python world!')`，但我们用`message`代替了这句话。

> 可以回想一下恐怖的数学课，老师是不是经常说“把x=2带入到方程中，然后我们得到......”

这里使用一个变量来代称"Hello Python world!"这句话，其实变量还可以用来代称一个数字、一组数字、一个函数等等，在接下里的学习中我们就会看到。

## 变量的类型

我们刚刚提到，变量可以代替一句话或者一个数，但是我们总不能讲一句话带入到方程中吧。这时我们就要区分不同的变量类型。一般情况下会存在以下几种常用的基础数据类型：

### 1. 字符串, string

字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。比如刚刚我们的`"Hello Python world!"`就是一个字符串。关于字符串的使用，大家要注意三点：

- 如果字符串内还需要引号，需要跟最外面的一层不同，比如
```python
message = "Hello 'Python' world!"
print(message)
```
- 字符串的拼接可以使用`+`号，比如：
```python
message = "Hello" + "Python world!"
print(message)
```
- 如果需要换行，可以使用两次`print`函数，也可以字符串中使用`\n`来进行换行，比如
```Python
message = "Hello \nPython world!"
print(message)
```