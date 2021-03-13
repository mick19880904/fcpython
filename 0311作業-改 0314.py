# -*- coding: utf-8 -*-
"""
0311python作業
1.
請隨機取數 1-49 取 6 個，且整數 不可重複，並放入串列中 (樂透)

2.
[100,80,1,3,10,7]
請排序小到大 [1,3,7,10,80,100]

*氣泡排序:相鄰兩個值去比較
"""

#1.
import random
# lotal = random.randint(1,49)
# lotal1 = random.randint(1,49)
# lotal2 = random.randint(1,49)
# lotal3 = random.randint(1,49)
# lotal4 = random.randint(1,49)
# lotal5 = random.randint(1,49)
# print(lotal,lotal1,lotal2,lotal3,lotal4,lotal5)


    
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
# print("list  :", list1)
list2 = random.sample(list1, 6)
print("隨機取數6位不重複:", list2)

#2.參考這個網頁https://www.mdeditor.tw/pl/peQ6/zh-tw
def bubbleSort(arr):
    leng=len(arr)
    while leng-1>0:
        i=1
        while i<=leng-1 :
            if(arr[i]<arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]
            i+=1
        leng-=1
    return arr
arr = [100,80,1,3,10,7]
bubbleSort(arr)

print(arr)

#2.-2參考了這個，細節仍然沒解讀出來...明白原理但 讀不懂
data = [100,80,1,3,10,7]
def bubbleSort(data): #定義資料長度
    n = len(data)  # n = 6
    for i in range(n-2): #有N個資料長度但只要執行n-1次
        for j in range(n-i-1): #從第一個開始比較直到最後一個還沒到最終的位置
            if data[j] > data[j+1]: #比大小然後互換
                data[j],data[j+1] = data[j+1],data[j]
bubbleSort(data)
print(data)
# data = [100,80,1,3,10,7]
# n = len(data)
# print(n)

# data = [100,80,1,3,10,7]
# n = len(data)
# for i in range(n-2):
#     print(i)


