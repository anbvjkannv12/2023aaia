a=[1, 3, 5, 7, 9, 11, 13, 15, 17]
N= len(a)
for i in range(N-1):
  d=a[1]-a[0]
  if a[i+1]-a[i]!=d:
    print("出錯了")
print("成功測試ok")