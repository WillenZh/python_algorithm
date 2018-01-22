
# coding: utf-8

# In[65]:


from random import randint
from heapq import merge
import time


# In[83]:


number = 0


# In[84]:


#快速排序的实现
def quickSort(myList):
    global number
    if len(myList) <= 1:
        return myList
    else:
        number += 1
        pivot = myList[0]
        left = [x for x in myList[1:] if x < pivot]
        right = [x for x in myList[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)


# In[85]:


#合并排序的实现
def merge_sort(myList):
    if len(myList) <= 1:
        return myList
    else:              
        middle = len(myList)//2
        left = merge_sort(myList[:middle])
        right = merge_sort(myList[middle:])
        return list(merge(left, right))         #heapq.merge()


# In[93]:


#合并排序的实现
def merge_sort2(myList):   #此方法来自维基百科：http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    if len(myList) <= 1:
        return myList
                 
    def merge(left, right):
        merged = []
        
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        
        while left:
            merged.append(left.pop(0))
        
        while right:
            merged.append(right.pop(0))
        
        return merged
        
    middle = int(len(myList) // 2) 
    left = merge_sort(myList[:middle])
    right = merge_sort(myList[middle:])
    return merge(left, right)


# In[99]:


myList = []
for index in range(100000):
    myList.append(randint(1,10000))


# In[95]:


print(*myList)


# In[96]:


number = 0
start = time.time()
print(quickSort(myList))
#quickSort(myList)
end = time.time()
print("时间：%f, 分割次数：%d" % ((end-start), number))


# In[100]:


start = time.time()
#print(merge_sort(myList))
merge_sort(myList)
end = time.time()
print("时间：%f" % (end-start))


# In[101]:


start = time.time()
#print(merge_sort2(myList))
merge_sort2(myList)
end = time.time()
print("时间：%f" % (end-start))

