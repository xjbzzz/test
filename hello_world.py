#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一个简单的Python示例文件
包含基本的函数、类和一些常用操作
"""

import random
import datetime


def greet(name="世界"):
    """返回问候语"""
    return f"你好，{name}！"


def calculate_fibonacci(n):
    """计算斐波那契数列的第n个数"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)


class Person:
    """人员类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_at = datetime.datetime.now()
    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁。"
    
    def celebrate_birthday(self):
        self.age += 1
        return f"{self.name}过生日了，现在{self.age}岁了！"


def main():
    # 打印问候语
    print(greet("GitHub"))
    
    # 计算并打印斐波那契数列的前10个数
    print("斐波那契数列的前10个数:")
    for i in range(10):
        print(f"第{i+1}个数: {calculate_fibonacci(i)}")
    
    # 创建一个Person实例
    person = Person("张三", random.randint(20, 40))
    print(person.introduce())
    
    # 庆祝生日
    print(person.celebrate_birthday())
    
    # 打印当前时间
    print(f"当前时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("程序执行完毕！")


if __name__ == "__main__":
    main()