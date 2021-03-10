# -*- coding: utf-8 -*-
"""
0309作業 - 學員立丞
用巢來寫出以下 (兩個迴圈)

123456789
12345678
1234567
123456
12345
1234
123
12
1

   *   
  ***  
 *****
*******
 *****
  ***
   *
透過 min max優化這個程式碼
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
"""

#第一題
for i in range(10,0,-1):
    for x in range(1,i):
        print(x,end='')
    print()

#第二題