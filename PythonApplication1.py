def func1():
	n = int(input("Введите число: "))
	temp = n
	reverse = 0
	while (n > 0):
		drob = n % 10
		reverse = reverse * 10 + drob
		n = n // 10
	if (temp == reverse):
		print("true")
	else:
		print("false")

def func2():
	list2 = []
	list3 = []
	list5 = []
	nList = []
	nList = input("Введите элементы через пробел: ").split()
	nList = list(map(int, nList))
	print(nList)
	for i in range(len(nList)):
		if nList[i] % 2 == 0:
			list2.append(nList[i])
		if nList[i] % 3 == 0:
			list3.append(nList[i])
		if nList[i] % 5 == 0:
			list5.append(nList[i])
	print(list2)
	print(list3)
	print(list5)



def func3():
	n = int(input("Введите число: "))
	temp = n
	reverse = 0
	minus = 1
	if (n < 0):
		minus = -1
	n = n * (-1)
	while (n > 0):
		drob = n % 10
		reverse = reverse * 10 + drob
		n = n // 10
	print(reverse*minus)

def func4():
	x = int(input("Введите число: "))
	n = int(input("Введите корень: "))
	pogr = 0.00001
	a = x
	x1 = 1/n * ( ((n-1) * x) + (a/x**(n-1)) )   
	while (abs(x1-x)>pogr):
		x = x1
		x1 = 1/n * ( ((n-1) * x) + (a/x**(n-1)) )  
	print(x1)


def func5():
	c = "false"
	x = int(input("Введите число: "))
	if (x < 2):
		c = "false"
	x_sqrt = int(x ** 0.5)
	i = 2
	while (x_sqrt >= i):
		if (x % i == 0):
			c = "false"
			break
		else:
			i += 1
	else:
		c = "true"
	print(c)
			
choice = int(input("Выберите функцию от 1 до 5: \n 1 - Палиндром \n 2 - Деление на 2 3 5 \n 3 - Обратное число \n 4- Корень n-степени \n 5 - Простое число \n "))
if (choice == 1):
	func1()
if (choice == 2):
	func2()
if (choice == 3):
	func3()
if (choice == 4):
	func4()
if (choice == 5):
	func5()
elif(choice not in range(1,5)):
	print("Ошибка")