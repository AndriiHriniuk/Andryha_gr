name = input("Как Вас зовут? ")
print("Привет,", name, ",я помогу тебе решить квадратное уравнение типа ax^2+bx+c=0")
x = 1
a=input("введите переменную a")
b=input("введите переменную b")
c=input("введите переменную c")
a = int(a)
b = int(b)
c = int(c)
D = (b ** 2 - 4 *( a) *  (c))

if (D<0):print("Уравнение не имеет решний")

else:import math
Dsqrt = math.sqrt(D)


print("x1=",(b*(-1)+Dsqrt)//(2*a))
print("x2=",(b*(-1)-Dsqrt)//(2*a))






