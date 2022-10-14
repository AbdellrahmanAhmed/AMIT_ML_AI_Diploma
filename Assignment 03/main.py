List = ['Abdelrahman','red',55,1997,'Ahmed']

for i in range(len(List)):
  print('List [',i,'] is : ', List[i])

n = 0
while n < len(List):
  if type(List[n]) is int:
    break
  print('str Number',n+1,' is : ',List[n] )
  n += 1
