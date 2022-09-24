def is_prime(num):
  i = 2
  if (num < 2 ):          
    return 'not a prime number'
  else:
    while (i < num):
      if(num % i == 0):
        return "not a prime number"
        break
      i = i + 1
    return 'prime number'
for i in range (-1,21): 
  print("Number "+ str(i) + " " + is_prime(i))