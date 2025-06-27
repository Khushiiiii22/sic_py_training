#  Check if a +ve integer is Perfect square

                               
positive_integer = int(input('Enter number: '))
  
if(int(positive_integer**0.5)**2 == positive_integer):
    print(positive_integer , 'is a perfect square')

else:
     print(positive_integer , 'is not a perfect square')

