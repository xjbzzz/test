#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
冒泡排序算法实现
包含基本版本和优化版本的冒泡排序算法
"""

import random
import time


def bubble_sort_basic(arr):
    """
    基本冒泡排序算法
    时间复杂度: O(n²) - 最坏情况、平均情况
    空间复杂度: O(1)
    
    参数:
        arr: 要排序的列表
    返回:
        排序后的列表
    """
    # 复制列表以避免修改原始数据
    arr = arr.copy()
    n = len(arr)
    
    # 外层循环：需要进行n-1次冒泡
    for i in range(n - 1):
        # 内层循环：每次冒泡将当前最大元素"浮"到末尾
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def bubble_sort_optimized(arr):
    """
    优化版冒泡排序算法
    1. 如果在某次遍历中没有发生交换，说明数组已经有序，可以提前退出
    2. 记录最后一次交换的位置，下一轮只需要比较到这个位置
    
    时间复杂度: 
        - 最坏情况: O(n²)
        - 最好情况: O(n) - 当数组已经有序时
        - 平均情况: O(n²)
    空间复杂度: O(1)
    
    参数:
        arr: 要排序的列表
    返回:
        排序后的列表
    """
    # 复制列表以避免修改原始数据
    arr = arr.copy()
    n = len(arr)
    
    # 最后一个没有被排序过的元素的位置
    last_unsorted = n - 1
    
    # 当还有未排序的元素时
    while last_unsorted > 0:
        # 最后一次交换的位置
        last_swap = 0
        
        for j in range(last_unsorted):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 记录最后一次交换的位置
                last_swap = j
        
        # 更新最后一个未排序元素的位置
        last_unsorted = last_swap
    
    return arr


def test_sorting_algorithm(sort_func, arr):
    """测试排序算法并计时"""
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    
    print(f"{sort_func.__name__} 耗时: {end_time - start_time:.6f} 秒")
    
    # 验证排序结果
    is_sorted = all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))
    print(f"排序结果正确: {is_sorted}")
    
    return sorted_arr


def main():
    # 生成随机数组进行测试
    print("生成随机数组...")
    random_array = [random.randint(0, 1000) for _ in range(1000)]
    
    print("\n测试基本冒泡排序:")
    basic_sorted = test_sorting_algorithm(bubble_sort_basic, random_array)
    
    print("\n测试优化冒泡排序:")
    optimized_sorted = test_sorting_algorithm(bubble_sort_optimized, random_array)
    
    # 为了比较，使用Python内置排序
    print("\n测试Python内置排序:")
    start_time = time.time()
    python_sorted = sorted(random_array)
    end_time = time.time()
    print(f"Python内置排序耗时: {end_time - start_time:.6f} 秒")
    
    # 验证所有结果是否一致
    print("\n验证所有排序结果是否一致:")
    print(f"基本冒泡排序与优化冒泡排序结果一致: {basic_sorted == optimized_sorted}")
    print(f"优化冒泡排序与Python内置排序结果一致: {optimized_sorted == python_sorted}")
    
    # 展示小型数组的排序过程
    small_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n小型数组排序示例: {small_array}")
    print(f"排序后: {bubble_sort_optimized(small_array)}")


if __name__ == "__main__":
    main()