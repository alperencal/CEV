import random
loto=[]
for i in range(0,8):
  loto.append(random.sample(range(1, 50), 6))
print(*loto, sep = "\n")