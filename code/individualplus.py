h=int(input())
c=h//3600
m=(h-c*3600)//60
s=h%60
print(c,h,s)