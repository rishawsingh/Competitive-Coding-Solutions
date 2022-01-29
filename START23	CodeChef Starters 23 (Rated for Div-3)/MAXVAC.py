# cook your dish here
import sys,os,io
import math 
from collections import defaultdict


def ii():
    return int(input())
def li():
    return list(map(int,input().split()))

def solve():
    n,k = [int(x) for x in input().split()]
    s = list(input())
    if s.count('0')==n:
        print(s.count('0')//k)
        return
    left_z = [0]*n 
    left_sum = [0]*n 
    right_z = [0]*n 
    right_sum = [0]*n 
    
    if s[0]=='0':
        left_z[0]=1
        
    for i in range(1,n):
        if s[i]=='0':
            left_z[i]+=left_z[i-1]+1
            left_sum[i] = left_sum[i-1]
        else:
            left_sum[i]+=left_z[i-1]//k + left_sum[i-1]

    if s[-1]=='0':
        right_z[-1]=1

    for i in range(n-2,-1,-1):
        if s[i]=='0':
            right_z[i]+=right_z[i+1]+1
            right_sum[i]=right_sum[i+1]
        else:
            right_sum[i]+=right_z[i+1]//k  + right_sum[i+1]
    
    res = 0
    for i in range(1,n-1):
        if s[i]=='1':
            res = max(res , left_sum[i]+right_sum[i] - (left_z[i-1]//k )-(right_z[i+1]//k) +(left_z[i-1]+right_z[i+1]+1)//k )
    if s[0]=="1":
        res = max(res , right_sum[0] - right_z[i+1]//k + (right_z[i+1]+1)//k)
    if s[-1]=="1":
        res = max(res , left_sum[-1] - left_z[i-1]//k + (left_z[i-1]+1)//k)

    print(res)

t = 1
t = ii()
for _ in range(t):
    solve()
