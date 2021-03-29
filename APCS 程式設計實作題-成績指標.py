# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:11:37 2021

@author: 筱
"""
x = int(input("請輸入班級人數:"))

score = []
lucky = []
unlucky = []
while len(score) != x:
    score.append(int(input("請輸入成績:")))
print(x)
for i in sorted(score):
    print(i,end=" ")
print()
for i in sorted(score):
    # print(i,end=" ")
    if i > 60 and len(lucky) == 0:
        lucky.append(i)
        sorted(lucky)
        print("及格最低:",lucky[0])
   

for i in sorted(score,reverse=True):
    if i < 60 and len(unlucky) == 0:
        unlucky.append(i)
        print("不及格最高:",unlucky[0])
        print()
        

if len(lucky) == 0:
    print("worst case")
if len(unlucky) == 0:
    print("bset case")