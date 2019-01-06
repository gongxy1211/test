#coding:utf-8
str="nihao,zhonguo"
print str[0:6]
str2=['wo','shi','ni','ma']
print str2
print str2[0]
#str[0]='l'
str2[0]='nihao'
print str
print str2
str3=('1','2','3')
print str3[0]
dict={}
dict['o']='nice to meet you'
dict[2]='shuzi'
print dict
print dict.values()
print dict.keys()
flag=False
name='hei'
if name=='hello':
  print 'hello boss'
else:
  print name
min='nihaomewohehao'
for i in min:
  if i=='w':
    pass
    print u'此处是空格'
  print i
  flag=1
  while(flag):
    print'Given flag isreallu true' 
    flag=0
  break
  print 'good bye'
import math
content=dir(math)
print content
Money=200
def AddMoney():
  global Money
  Money=Money+1
print Money
AddMoney()
print Money
