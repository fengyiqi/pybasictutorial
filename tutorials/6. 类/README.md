# 类

现在我们要接触现代程序设计中最核心的东西了——“面向对象编程”。面向对象编程有三大特性：封装、继承和多态。对我们这个极简教程来说，我们目前只学习封装，不学习继承。对于多态，大家只需要知道Python本身就是一个多态的语言，所以我们不用太关注这个问题。

封装其实不难理解，我们可以以电饭锅作为例子，电饭锅内部是不是有一些电路元器件，但我们平时很难看到，因为它们被一个外壳盖住了。电饭锅外壳上还会有一些按键，不管是触屏的还是按键的，都是一种又外部向内部传递指令的界面，比如开始、保温等等。这其实就是封装的一种形式，把一些细节都隐藏起来，用户不用在意内部是怎么运行的，对外只提供一些接口，按就完了。

在程序设计上，函数其实就是一种封装，接口就是传入的参数和返回值，细节就是函数体。用户知道这个函数是干嘛的，然后传入函数，接收返回值就可以了。

但是以函数为主体的程序，还是很难进行扩展，而且也不符合我们人类认知事物的习惯。我们人类喜欢给东西分类，比如电饭锅属于家用电器类，再细一点属于厨具，再细一点属于烹调用具，甚至电饭锅本身就是一类。在每一个分类等级下都有一些共性，比如家用电器都需要电，厨具都放在厨房里，烹调用具做的东西是用来吃的。这种层层递进，前后相关的关系其实就是继承，但是我们可以先不用深入研究它。如果我们不考虑继承，那么一个具体的电饭锅，比如苏泊尔的电饭锅，可以看做任何分类下的一个实例，在程序设计中叫做对象。具有相同行为的对象，可以归纳为“类”。比如苏泊尔电饭锅可以看做是家用电器的一个实例，跟它平级的可能还有电视机、冰箱。它也可以是电饭锅类的一个实例，跟它具有相似行为的还有美的电饭锅、小米电饭锅等等。

说了这么多，我们可以总结一下。简单的说，类是对象的蓝图和模板，而对象是类的实例，是具体的东西。

## 1. 创建类

定义类需要用到关键字`class`，类的名字一般要求每个单词的首字母都大写，相反，函数和变量一般每个字母都要小写。

电饭锅其实都具有一些相同的属性，比如品牌、价格、功率等等，根据上面的描述，我们这就来创建一个电饭锅类，并且每一个具体的电饭锅都要有这三个属性：

```python
class RiceCooker:
    
    def __init__(self, brand, price, power):
        self.brand = brand
        self.price = str(price) + 'RMB'
        self.power = str(power) + 'W'

rc_media = RiceCooker('Media', 209, 800)
rc_supor = RiceCooker(brand='Supor', price=199, power=780)
rc_mi = RiceCooker(price=249, power=700, brand='mi')
```

- `def __init__(self, brand, price, power):`叫做初始化函数或者构造函数，函数名是固定的，不能用其他的函数名代替。它在每创建一个实例时都会自动调用，其中参数`self`是必须要有的，但它不需要赋值，就像没必要证明我是我。其他三个参数`brand, price, power`是要在每创建一个实例时指定。
- `self.brand = brand`是将传进来`brand`参数赋给这个实例，也就是说“我的品牌是`__init__(self, brand, price, power)`中的`brand`”。换个角度解释一下，其实`__init__(self, brand, price, power)`中的`brand`是参数，而不是属性，只有将`self.brand = brand`执行后，属性才算绑定给了实例。

> 这里两个`brand`同名可能不好理解，我们完全可以写成`self.brand_name = brand`。

- `rc_media = RiceCooker('Media', 209, 800)`是创建了一个具体的实例，它的品牌是`Media`，价格209，功率800。

> 我们可以看到`self.price = str(price) + 'RMB'`是将输入的价格转成了字符串，再在后面加上了单位`RMB`，功率属性与此类似。

- `rc_supor = RiceCooker(brand='Supor', price=199, power=780)`也是创建了一个实例，它与刚刚美的的不太一样，每个参数都写成了一个赋值表达式。其实这种方式与美的的作用是相同的，但这种更具有可读性，而且指定参数的顺序可以调换，比如下一个小米的实例。

创建了类的实例，我们就可以很方便地获取它的属性，比如这样：
```python
print(rc_media.brand)
print(rc_media.price)
```

## 2. 类方法

如果类只有这么点功能，岂不是太弱了。其实我们在类内也可以定义函数，只不过这时候不叫函数了，叫做类方法。定义的方法跟普通函数定义方法是一样的，只不过每个类方法第一个参数都必须是`self`，而且在调用时不需要指定。比如我们在刚刚的类中定义一个打印信息的方法：

```python
class RiceCooker:
    
    def __init__(self, brand, price, power):
        self.brand = brand
        self.price = str(price) + 'RMB'
        self.power = str(power) + 'W'

    def print_info(self):
        print(f'{self.brand}电饭锅，价格{self.price}，功率{self.power}。')

rc_media = RiceCooker('Media', 209, 800)
rc_media.print_info()
```

我们也可以定义一个煮饭的方法，这里用`print()`函数来模拟一下：

```python
class RiceCooker:
    
    def __init__(self, brand, price, power):
        self.brand = brand
        self.price = str(price) + 'RMB'
        self.power = str(power) + 'W'

    def print_info(self):
        print(f'{self.brand}电饭锅，价格{self.price}，功率{self.power}。')
    
    def cook_rice(self, rice_volume, water_volume):
        print('开始煮饭...')
        print('完成！')
        if water_volume <= 1.5 * rice_volume:
            print('米饭太硬了！')
        elif water_volume >= 2.5 * rice_volume:
            print('米饭太稀了！')
        else:
            print('完美')

rc_media = RiceCooker('Media', 209, 800)
rc_media.print_info()
rc_media.cook_rice(1, 1)
rc_media.cook_rice(1, 5)
rc_media.cook_rice(1, 2)
```

## 3. 总结

类可以说是Python编程中的核心，这里只展示了很简单的一个例子。类的其他优点还包括方便扩展、维护。如果使用继承，还可以让代码更为直观、简洁。我建议大家尽量培养这种面向对象编程的思考方式，将程序中可能会出现的事物归类，通过创建类，来整和它们。