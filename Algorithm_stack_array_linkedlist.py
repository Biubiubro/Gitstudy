"""
    手动实现stack的各种操作(后进先出)
    直接定义栈类,手写各种操作
"""
# class Stack:
#     # 初始化栈
#     def __init__(self):
#         self.stack = []
#
#     # 入栈
#     def push(self, element):
#         self.stack.append(element)
#
#     # 出栈
#     def pop(self):
#         return self.stack.pop()
#
#     # 查看栈顶元素
#     def get_top(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None
#
#     # p判断空栈
#     def is_empty(self):
#         return len(self.stack) == 0

'''
    栈的应用括号匹配问题
    ‘()[][{()[]}]’
    如果括号匹配就出栈,当读取完成栈为空栈时则代表匹配成功
'''
# def brace_match(str_bracket):
#     match = {'}':'{', ']':'[', ')':'('}
#     stack = Stack()
#     for bkt in str_bracket:
#         if bkt in {'(', '{', '['}:
#             stack.push(bkt)
#         else:
#             if stack.is_empty():
#                 return False
#             elif stack.get_top() == match[bkt]:
#                 stack.pop()
#             else:
#                 return False
#     if stack.is_empty():
#         return True
#     else:
#         return False
#
# print(brace_match('()[][{()[]}]'))



'''
    队列(和栈相对应,先进先出)
    采用环形数组的方式
    出队: font = (font + 1) % MaxSize
    入队: rear = (rear + 1) % MaxSize
    队空条件: rear == font
    队满条件: (rear + 1) % MaxSize == font
'''
# class Queue:
#     # 初始化队列,规定数组长度,队首队尾
#     def __init__(self, size = 100):
#         self.queue = [0 for _ in range(size)]
#         self.rear = 0
#         self.font = 0
#         self.size = size
#
#     # 入队
#     def push(self, element):
#         if not self.is_filled():
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = element
#         else:
#             raise IndexError("Queue is filled")
#
#     # 出队
#     def pop(self):
#         if not self.is_empty():
#             self.font = (self.font + 1) % self.size
#             return self.queue[self.font]
#         else:
#             raise IndexError("Queue is empty")
#
#     # 队空
#     def is_empty(self):
#         return self.rear == self.font
#
#     # 队满
#     def is_filled(self):
#         return (self.rear + 1) % self.size == self.font
#
# que = Queue(10)
# for i in range(que.size - 1):
#     que.push(i)
# print(que.is_filled())
# for i in range(3):
#     print(que.pop())
# over

















