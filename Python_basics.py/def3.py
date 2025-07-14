def my_function(param1 = 45,param2 = 70):
    print(f'Num1 = {param1}, Num2={param2}')
    return param1 + param2

num1= 49
num2=56

result = my_function(num1,num2)
print(f'Result = {result}')

result = my_function(param2 = num1 , param1 = num2)       #Named parameters
print(f'Result = {result}')
