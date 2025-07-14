# def my_function(param1 ,param2 = 70): if either one of the is given the value shows error

def my_function(param1 = 45,param2 = 70):
    print(f'Num1 = {param1}, Num2={param2}')
    return param1 + param2

num1= 49
num2=56

result = my_function(num1,num2)
print(f'Result = {result}')

result = my_function(num1)
print(f'Result = {result}')

result = my_function()
print(f'Result = {result}')
