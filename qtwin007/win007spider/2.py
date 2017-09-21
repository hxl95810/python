# -*- coding: utf-8 -*-


import re
a="var matchcount=221;"

# print (filter(a))
# abc=filter(str.isdigit, a)

# abc=re.findall("\d+", a)
# abc=re.sub("\D", "", a)
# print ( abc[2])

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
# l=l[4:8]
# print (l )

# a=[]
# m=0;
# 
# for i in range(1,10):
# 
#     a.append(i)
#     
#     m+=1
#     
# print (a)

str="17-09-0516:00"
print(str[0:8])
print(str[-5:])

matchTime = str[0:8]+' '+str[-5:]
print(matchTime)


