# 剝皮法
a=1234
while a>0:
  ans=ans*10+a%10
  a=a//10
  print('現在的a是', a ,'撥出來的皮是a%10', a%10,'現在的就變成', ans)