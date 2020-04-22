import numpy as np
from collections import deque



class AL(object):
    def __init__(self):
        self.sorted_pool = [0,1,2,3,4,5,6,7,8,9]
        self.unorder_arr = [ np.random.randint(50) for i in range(20)]


    def search(self, type, aim):
        arr = self.order('sele')
        print(arr)
        if type == 'bs':
            return self.binary_search(arr, aim)
        if type == 'bs_dc':
            return self.binary_search_dc(arr, aim)


    def order(self, type):
        if type == 'sele':
            self.unorder_arr =self.select_sort(self.unorder_arr)
            return self.unorder_arr
        if type == 'qs':
            self.unorder_arr =self.quick_sort(self.unorder_arr)
            return self.unorder_arr

    def binary_search(self, order_list, aim):
        left = 0
        right = len(order_list) - 1
        num = 0
        while left <= right:
            num += 1
            mid = (left + right) // 2
            # print(mid, num)
            if order_list[mid] == aim:
                return mid, num
            elif order_list[mid] > aim:
                right = mid - 1
            else:
                left = mid + 1
        return -1, num

    def binary_search_dc(self, order_list, aim):
        left = 0
        right = len(order_list) - 1
        mid = (left + right) // 2
        # print(order_list)
        # print(left, mid, right)

        if len(order_list)==1 and order_list[0]!=aim:
            return -1, 1
        if order_list[left] > aim or order_list[right] < aim:
            return -1, 1
        if aim == order_list[mid]:
            return mid, 1
        elif aim < order_list[mid]:
            foo = self.binary_search_dc(order_list[left:mid], aim)
            return (foo[0], 1+foo[1])
        else:
            foo = self.binary_search_dc(order_list[mid+1:right+1], aim)
            if foo[0] == -1:
                return (foo[0], 1+foo[1])
            return (mid+1+foo[0], 1+foo[1])


    def select_sort(self, arr):
        # print(arr)
        order_arr = list()
        for i in range(len(arr)):
            # print(len(arr))
            smallest = self.find_smallest(arr)
            order_arr.append(arr.pop(smallest))
        return order_arr

    def find_smallest(self, arr):
        res = arr[0]
        res_i = 0
        for i, v in enumerate(arr):
            if res > v:
                res = v
                res_i = i
        return res_i

    def quick_sort(self, arr):
        if len(arr)<2:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x<pivot]
            right = [x for x in arr[1:] if x>=pivot]
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def breadth_first_search(self, graph, name):
        search_queue = deque()
        search_queue += graph[name]
        searched = set()                # 用于记录检查过的人，防止进入死循环
        while search_queue:
            person = deque.popleft()
            if person not in searched:  # 避免重复检查
                if person_is_seller(person):
                    return True
                else:
                    search_queue += graph[person]
                    searched.add(person)# 记录检查过的人
        return False

    def mysum(self, arr):
        if len(arr) == 0:
            return 0
        else:
            return arr[0]+self.mysum(arr[1:])

    def get_unorder_arr(self):
        return self.unorder_arr

# print(AL().search('bs', 7))
# print(AL().order('sele'))

# 分而治之
# foo = AL().get_unorder_arr()
# print(foo)
# print(sum(foo), AL().mysum(foo))

# al = AL()
#
# print(al.search('bs', 11))
# print(al.search('bs_dc', 11))

# 快速排序
al = AL()
print(al.order('sele'))
print(al.order('qs'))

al = AL()
print(al.order('qs'))
print(al.order('sele'))
