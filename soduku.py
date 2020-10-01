def printMiniSodoku(a):
  res, n = '', len(a)
  for i in range(n):
    for j in range(n):
      res += f'{a[i][j]:3}'
    if i < n-1:
      res += '\n'
  print(res)


def readMiniSodoku(fn):
  with open("fn", "r") as f:
   sodoku = f.readlines()
   sodoku = [i.strip().split(",") for i in sodoku]
   return sodoku

def checkMiniSodoku(s):
  n = 3
  x = n
  y = n
  count = 1
  check = True
  for a in range(n):
    print(count, "count")
    a = 1
    y =n 
    while a < 4:
      currentnum = []
      for j in range(x-n,x):    
        for k in range(y-n,y):
          if str(s[j][k]) in currentnum:
            check = False        
            break
        
        else:
          currentnum.append(s[j][k])
      a += 1
      count += 1
      y += n
    x += n
  return check
