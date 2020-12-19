# -*- coding: utf-8 -*-


# 类

# 1. 创建类
print('-----创建类-----')

class RiceCooker:
    
    def __init__(self, brand, price, power):
        self.brand = brand
        self.price = str(price) + 'RMB'
        self.power = str(power) + 'W'

rc_media = RiceCooker('Media', 209, 800)
rc_supor = RiceCooker(brand='Supor', price=199, power=780)
rc_mi = RiceCooker(price=249, power=700, brand='mi')

print(rc_media.brand)
print(rc_media.price)


# 2. 类方法
print('-----类方法-----')

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