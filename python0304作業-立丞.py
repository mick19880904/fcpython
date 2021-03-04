# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:36:15 2021
學員105255570
黃立丞0304 python作業
1.請利用 for range 計算1-50之間的 奇數和 以及總數和
2.請利用 for range 印出 2,4,6,8
"""
#奇數和 1-50
total = 0
num =int(input("請輸入數字:"))  #輸入50
for s in range(1,num+1,2):     #起始為1 後面等差數列2 均為奇數s值，num+1是 終止值不會印出來所以+1
    total +=s                  
    #total 將每一個s值加起來，因為上一個程式碼列出了所有s變數等於 0+第一個s+第二個]s++到最後一個s
    print("總和:",total)       #印出total的值
    
#偶數和 1-50
total = 0
num = int(input("請輸入數字:")) #輸入50
for k in range(0,num+1,2):
    total += k
    print("總和:",total)
    
#偶數和 1-50(2)
total = 0
num = int(input("請輸入數字:")) #輸入50
for w in range(1,num+1):
    if w % 2 == 0:
        total += w
        print("總和:",total)
        
#用for range 印出 2,4,6,8
j = int(input("請輸入數字:"))   #輸入8
for r in range(2,j+1,2):
    print(r,end=',')
    
#用for range 印出 2,4,6,8 (2)

for g in range(2,9,2):
    print(g,end=',')