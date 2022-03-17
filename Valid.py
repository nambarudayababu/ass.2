s=input()
l=0
u=0
d=0
s=0
for i in s:
        if(i.islower()):
            l=l+1
        elif(i.isupper()):
            u=u+1
        elif(i.isdigit()):
            d=d+1
        else:
            s=s+1  
if(u>=1 and l>=1 and d>=1 and s>=1):
        print('valid')
else:
        print('invalid')
        
