# -*- coding: utf-8 -*-
"""
學員105255570
黃立丞0304/0309/0311 python作業
1.請利用 for range 計算1-50之間的 奇數和 以及總數和
2.請利用 for range 印出 2,4,6,8

3.用巢來寫出以下 (兩個迴圈)

123456789
12345678
1234567
123456
12345
1234
123
12
1

4.完成菱形
   *   
  ***  
 *****
*******
 *****
  ***
   *
5.透過 min max優化這個程式碼
import random

ans = random.randint(1, 100)
guess = 0
min = 1
max = 100
while ans != guess :
    guess = int (input("請輸入1-100之間的整數:")) 
    if guess > ans:
        print("再大一點") 改成介於猜值~最大值
        
    if guess < ans:
        print("再小一點") 改成介於最小值~猜值
print("猜對了")

6.請隨機取數 1-49 取 6 個，且整數 不可重複，並放入串列中 (樂透)

7.[100,80,1,3,10,7]
請排序小到大 [1,3,7,10,80,100]

*氣泡排序:相鄰兩個值去比較
"""
#1.奇數和 1-50
total = 0
num =int(input("請輸入數字:"))  #輸入50
for s in range(1,num+1,2):     #起始為1 後面等差數列2 均為奇數s值，num+1是 終止值不會印出來所以+1
    total +=s                  
    #total 將每一個s值加起來，因為上一個程式碼列出了所有s變數等於 0+第一個s+第二個]s++到最後一個s
    print("總和:",total)       #印出total的值
    
#1-1.偶數和 1-50
total = 0
num = int(input("請輸入數字:")) #輸入50
for k in range(0,num+1,2):
    total += k
    print("總和:",total)
    
#1-2偶數和 1-50(2)
total = 0
num = int(input("請輸入數字:")) #輸入50
for w in range(1,num+1):
    if w % 2 == 0:
        total += w
        print("總和:",total)
        
#2-1用for range 印出 2,4,6,8
j = int(input("請輸入數字:"))   #輸入8
for r in range(2,j+1,2):
    print(r,end=',')           #end='\n'是斷行，將斷行改成,即可
    
#2-2用for range 印出 2,4,6,8 (2)

for g in range(2,9,2):
    print(g,end=',')
#3.
for i in range(10,0,-1):
    for x in range(1,i):
        print(x,end='')
    print()

#4.菱形
for a in range(1,5): #i = 1 2 3 4 
    print(' '*(4-a)+'*'*(2*a-1) )
#菱形的中間是7個* 所以第一行3個空白+* 第二行2個空白+3個* 第三行1個空白+5個* 第四行0空白+7個*
#空白 + * = 4 ，4 - * = 空白 
#' ' = 空白 ， ' ' *(4-a)
#a = * ， a = * = 1 2 3 4 3 2 1 所以迴圈的上半部分1-4，下半部分3-1 
#是1 3 5 7等差數列2 也可以透過 2a-1來寫
#所以完成了迴圈1-4 接下來寫1-3
for a in range(3,0,-1):
    print(' '*(4-a)+ '*'*(2*a-1))
    
print()

#4-1菱形
#每一行的*是 1 3 5 7 5 3 1 等差數列2
for a in range(1,8,2):
    print(('*'*a).center(7))  #center(7)的意思是 取7的中間點 1 2 3 "4" 5 6 7的"4" 也就是從中心點為基礎
for a in range(5,0,-2):
    print(('*'*a).center(7))
print()
#6.
import random
lotal = list() #先給一個空白的串列
while len(lotal) != 6: #無限迴圈，n起始0，直到lotal串列的長度不等於6結束迴圈 (也可以解讀為< 6)
    n = random.randint(1,49) #給n隨機亂數一個範圍 1-49之間
    if lotal.count(n) == 0: #如果這個串列裡面的亂數n重複就是1 沒有重複就是0
        lotal.append(n) #達成上面條件 則新增n亂數進去串列
print(lotal) #直到新增6個長度的串列後，無限迴圈就結束直接印出結果

print()
#6-1.
import random
lotal1 = [0,0,0,0,0,0]
i = 0
while lotal1.count(0) != 0: #初始的0是6個，只要還有0就重複迴圈次數
    n = random.randint(1,49) #給予亂數n1-49的範圍
    if lotal1.count(n) == 0: #如果lotal 裡面的n = 0 表示沒有重複
        lotal1[i] = n #將 i = 0 索引值的值改成n
        i += 1 #延續上一個程序，i + 1 就會順著索引值更新n值下去
print(lotal1) #直到lotal串列裡面的0 沒有了就印出來
print()
#7.氣泡排序

data = [100,80,1,3,10,7] #先給data一個串列值
n =len(data) #氣泡排列是前後比較，所以比較次數是 0-1 1-2 2-3 3-4 4-5 共為5次比較 所以可以寫成長度-1
for x in range(n-1): #迴圈跑 6-1次也就是比較5次數值 x = 0 1 2 3 4
    for z in range(n-x-1): #6 - (0-4) -1也就是每一次比較後，最大的值會去最右邊，所以次數再-1 z=0~5 0~4 0~3 0~2 0~1
        if data[z] > data[z+1]: #如果當索引值 0~4  >索引值0+1 ~ 4+1 則前後交換
            data[z],data[z+1] = data[z+1],data[z]
print(data)

print()

#7.用內建的遞增排序
data = [100,80,1,3,10,7]
data.sort() #將data遞增排序
print(data)
print()
#7-1.
data = [100,80,1,3,10,7]
d = sorted(data) #快捷鍵的概念
print(d)