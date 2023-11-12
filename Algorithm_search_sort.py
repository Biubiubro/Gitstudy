import time
import random
import math

"""
    顺序查找(顾名思义)
    从第一个元素开始，顺序进行比较，直到找到为止
    enumerate(list)函数循环遍历了列表的所有元素，并通过增加从零开始的计数器变量来为每个元素生成索引
    并生成索引加元素的元组对的形式
"""
# def linear_search(lst, item):
#     for index, value in enumerate(lst):
#         if value == item:
#             return index
#     else:
#         return None
#
# list_test = ['a', 'b', 'c', 'd', 'e', 'f']
# print(linear_search(list_test, 'c'))



"""
    二分查找(也很简单)
"""
# def binary_search(lst, item):
#     left_index = 0
#     right_index = len(lst) - 1
#     mid_index = (right_index - left_index) // 2
#     while True:
#         if item == lst[mid_index]:
#             return mid_index
#         elif right_index < left_index:
#             print('元素不存在')
#             return -1
#         elif item < lst[mid_index]:
#             right_index = mid_index - 1
#             mid_index = (right_index + left_index) // 2
#         elif item > lst[mid_index]:
#             left_index = mid_index + 1
#             mid_index = (right_index + left_index) // 2
#
# list_test = [1, 2, 3, 4, 5, 6, 7]
# print(binary_search(list_test, 7))



"""
    冒泡排序(基础排序算法)
    逐个把最大或最小的元素依次比较放在列表的两边
    可以使用Python特别的语法进行交换(a, b = b, a)
"""
# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 temp_item = lst[j]
#                 lst[j] = lst[j + 1]
#                 lst[j + 1] = temp_item
#     return lst
#
# list_test = [1, 4, 2, 6, 9, 10, 2, 5]
# print(bubble_sort(list_test))



"""
    选择排序
    每次挑出列表中最小(最大)的元素,继续在剩下的元素中重复这样的操作
    避免空间浪费只需在原列表上操作即可
"""
# def select_sort(lst):
#     for i in range(len(lst) - 1):
#         min_index = i
#         for j in range(i + 1, len(lst)):
#             if lst[min_index] > lst[j]:
#                 min_index = j
#         if min_index != i:
#             temp_item = lst[min_index]
#             lst[min_index] = lst[i]
#             lst[i] = temp_item
#
# list_test = [1, 4, 5, 2, 8, 10, 3]
# select_sort(list_test)
# print(list_test)



"""
    插入排序
    可以令列表第一个元素为已知元素,后面的元素依次比较插入到已知元素中,不断重复操作
    前提是已知元素列已经排序完毕
    同样在一个列表上操作不再开辟新空间    
    (这个算法代码简洁)
"""
# def insert_sort(lst):
#     for i in range(1, len(lst)):
#         temp_item = lst[i]
#         j = i - 1
#         while j >= 0 and lst[j] > temp_item:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = temp_item
#         print(lst)
#
# list_test = [1, 4, 5, 2, 8, 10, 3]
# insert_sort(list_test)
# print(list_test)



'''
    运用系统库查看算法执行效率
'''
# # 自己写一个计时装饰器(以排序算法为例)
# def timeCount(func):
#     def algorithmTime(*args):
#         print('sb')
#         start_time = time.time()
#         func(*args)
#         end_time = time.time()
#         print('Runtime: ' + str(abs(end_time - start_time)))
#     return algorithmTime
#
# @timeCount
# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 temp_item = lst[j]
#                 lst[j] = lst[j + 1]
#                 lst[j + 1] = temp_item
#     return lst
#
# # 生成乱序数组
# list_test = list(range(10000))
# random.shuffle(list_test)
# print(list_test)
# bubble_sort(list_test)



''' 
    快速排序(较为复杂运用递归)
    每次把第一个元素移到中间并左边元素均小于中间元素,右边元素均大于中间元素,左右两边进行递归实现
    先写一个partition函数进行一次排序,剩下的部分进行递归
'''
# def partition(lst, left, right):
#     temp = lst[left]
#     while left < right:
#         while left < right and lst[right] >= temp:
#             right -= 1
#         lst[left] = lst[right]
#         while left < right and lst[left] <= temp:
#             left += 1
#         lst[right] = lst[left]
#     lst[left] = temp
#     return left  # 为快排函数返回mid值
#
# def quick_sort(lst, left, right):
#     if left < right:
#         mid = partition(lst, left, right)
#         quick_sort(lst, left, mid - 1)
#         quick_sort(lst, mid + 1, right)
#
# list_test = [6, 3, 4, 7, 9, 11, 2]
# quick_sort(list_test, 0, len(list_test) - 1)
# print(list_test)



''' 
    堆排序(非常复杂)
    分为两步第一步构造堆,第二部逐次取出堆顶元素
    其中取出元素的过程随时保持当前堆是一颗完全二叉树
'''
# def shift(lst, low, high):
#     """
#     :param lst: 列表
#     :param low: 根节点
#     :param high: 最后一个叶子节点
#     :return:
#     """
#     i = low
#     j = 2 * i + 1
#     temp = lst[low]
#
#     while j <= high:
#         if j + 1 < high and lst[j + 1] > lst[j]:
#             j += 1
#         if lst[j] > temp:
#             lst[i] = lst[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             lst[i] = temp
#             break
#     else:
#         lst[i] = temp
#
# def heap_sort(lst):
#     n = len(lst)
#     # 构造堆(从最小子树开始依次往上构造)
#     for i in range((n - 2) // 2, -1, -1):
#         shift(lst, i, n - 1)
#
#     # 逐次取出堆顶元素并放置到最后一位,堆排序完成
#     for i in range(n - 1, -1 , -1):
#         lst[i], lst[0] = lst[0], lst[i]
#         shift(lst, 0, i - 1)
#
# list_test = list(range(20))
# random.shuffle(list_test)
# print(list_test)
# heap_sort(list_test)
# print(list_test)



'''
    基于堆排序的top_k问题(这里运用小根堆,运用堆排序算法的复杂度会降低)
    首先改成小根堆排序,再依次取出列表后续元素
'''
# def shift(lst, low, high):
#     """
#     :param lst: 列表
#     :param low: 根节点
#     :param high: 最后一个叶子节点
#     :return:
#     """
#     i = low
#     j = 2 * i + 1
#     temp = lst[low]
#
#     while j <= high:
#         if j + 1 <= high and lst[j + 1] < lst[j]:
#             j += 1
#         if lst[j] < temp:
#             lst[i] = lst[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             lst[i] = temp
#             break
#     else:
#         lst[i] = temp
#
# def topk(lst, k):
#     heap = lst[0: k]
#     # 对前k个元素进行建堆
#     for i in range((k - 2) // 2, -1, -1):
#         shift(heap, i, k - 1)
#         # print(heap)
#     print(heap)
#     # 遍历列表后续元素与根节点进行比对并调整堆元素
#     for i in range(k, len(lst)):
#         if lst[i] > heap[0]:
#             heap[0] = lst[i]
#             shift(heap, 0, k - 1)
#         print(heap)
#     # 排序输出
#     for i in range(k - 1, -1, -1):
#         heap[i], heap[0] = heap[0], heap[i]
#         shift(heap, 0, i - 1)
#     return heap
#
# list_test = list(range(20))
# random.shuffle(list_test)
# print(list_test)
# print(topk(list_test, 5))



'''
    归并排序
    将两段有序的序列合并成一个有序的列表
    依次取出两段中第一个元素进行比较依次取出即可  
'''
# 先进行一次归并
# def merge(lst, low, mid, high):
#     i = low
#     j = mid + 1
#     temp_lst = []
#     while i <= mid and j <= high:
#         if lst[i] < lst[j]:
#             temp_lst.append(lst[i])
#             i += 1
#         else:
#             temp_lst.append(lst[j])
#             j += 1
#     while i <= mid:
#         temp_lst.append(lst[i])
#         i += 1
#     while j <= high:
#         temp_lst.append(lst[j])
#         j += 1
#     lst[low: high + 1] = temp_lst
#
# # 进行递归拆分再归并
# def merge_sort(lst, low, high):
#     if low < high:
#         mid = (low + high) // 2
#         merge_sort(lst, low, mid)
#         merge_sort(lst, mid + 1, high)
#         merge(lst, low, mid, high)
#
# list_test = list(range(20))
# random.shuffle(list_test)
# print(list_test)
# merge_sort(list_test, 0, len(list_test) - 1)
# print(list_test)



'''
    希尔排序
    就是在插入排序前先分组
'''
# def insert_sort_gap(lst, gap):
#     for i in range(gap, len(lst)):
#         temp = lst[i]
#         j = i - gap
#         while j >= 0 and lst[j] > temp:
#             lst[j + gap] = lst[j]
#             j -= gap
#         lst[j + gap] = temp
#     print(lst)
#
# # 进行希尔排序(每次排序完成分组长度减半)
# def shell_sort(lst):
#     distance = len(lst) // 2
#     while distance >= 1:
#         insert_sort_gap(lst, distance)
#         distance //= 2
#
# list_test = list(range(20))
# random.shuffle(list_test)
# print(list_test)
# shell_sort(list_test)
# print(list_test)


'''
    计数排序(较为简单)
    0到列表中最大的数进行遍历计数
'''
# def count_sort(lst):
#     lst_count = [0 for _ in range(max(lst) + 1)]
#     for num in lst:
#         lst_count[num] += 1
#     lst.clear()
#     for idx, num in enumerate(lst_count):
#         for i in range(num):
#             lst.append(idx)
#
# list_test = list(range(20))
# random.shuffle(list_test)
# print(list_test)
# count_sort(list_test)
# print(list_test)



'''
    桶排序
    将列表分成几段,对么一段分别排序,最后在拼接到一起
    开放性较强分桶后可以按照自己喜欢的排序算法进行分组排序
'''
# def bucket_sort(lst):
#     bucket_num = 10
#     max_num = max(lst)
#     buckets = [[] for _ in range(bucket_num)]
#     for var in lst:
#         i = min(var // 10, bucket_num - 1)
#         buckets[i].append(var)
#         for j in range(len(buckets[i]) - 1, 0, -1):
#             if buckets[i][j] < buckets[i][j - 1]:
#                 buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
#             else:
#                 break
#     lst.clear()
#     for buc in buckets:
#         lst.extend(buc)
#     print(lst)
#
# list_test = list(range(100))
# random.shuffle(list_test)
# print(list_test)
# bucket_sort(list_test)



'''
    基数排序
    稳定排序类型,不会改变相同元素的相对位置
    先从个位数开始排
'''
# def radix_sort(lst):
#     max_num = max(lst)
#     count = int(math.log(max_num, 10))
#     for i in range(count + 1):
#         buckets = [[] for _ in range(10)]
#         for var in lst:
#             digit = (var // 10 ** i) % 10
#             buckets[digit].append(var)
#         lst.clear()
#         for buc in buckets:
#             lst.extend(buc)
#     print(lst)
#
# list_test = list(range(100))
# random.shuffle(list_test)
# print(list_test)
# radix_sort(list_test)

