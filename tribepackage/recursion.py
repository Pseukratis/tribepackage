def sum_array(array):

   '''Return sum of all items in array'''

   if len(array)==0:
      return 0
   else:
      return array[0] + sum_array(array[1:])




def fibonacci(n):
  '''
  This function returns the nth term in the fibonacci sequence
  '''
  if n == 1:
      return 1
  elif n==2:
      return  1
  elif n==0:
      return 0
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)





def factorial(n):
  '''
  Return n!
  '''
  if n == 1:
      return n
  elif n == 0:
      return 1
  else:
      return n * factorial(n-1)




def reverse(word):
  '''
  Return word in reverse
  '''
  if len(word)==0:
      return ""
  else:
      return word[-1] + reverse(word[:-1])
