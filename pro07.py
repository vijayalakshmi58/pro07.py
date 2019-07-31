# pro07.py
any=int(input())
green=1
while(green<=any and green*2<=any):
    green=green*2
if(green==any):
    print("0")
else:    
    print(any-green)
