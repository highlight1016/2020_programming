x = int(input('정수입력 : '))
x1 = (x // 500)
x2 = ((x % 500)//100)      
x3 = ((x % 500 % 100)//50)      
x4 = ((x % 500 % 100 % 50)//10)
print(x1 + x2 + x3 + x4)
