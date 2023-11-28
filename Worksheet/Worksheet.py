# radius=input("enter radius of the circle: ")
# radius= int(radius)
# circumference= (2*radius*22/7)
# print("the circumference is", circumference)

# side=input("enter the side length: ")
# side=int(side)
# area=(side*side)
# print("the area of the square is", area)

# side1=input("enter the length of the longer side of the rectangle: ")
# side2=input("enter the length of the shorter side of the rectangle: ")
# side1=int(side1)
# side2=int(side2)
# area=(side1*side2)
# print("the area of the rectangle is", area)

# length=input("enter the length of the cuboid: ")
# breadth=input("enter the breadth of the cuboid: ")
# height=input("enter the height of the cuboid: ")
# height=int(height)
# breadth=int(breadth)
# length=int(length)
# volume=(length*breadth*height)
# print("the volume of the cuboid is", volume)

# name=input("Please enter your name: ")
# print("Good day", name)

# result=(9.5*4.5-2.5*3)/(45.5-3.5)
# print(result)

# x=input("please enter the x value: ")
# x=float(x)
# y=(3*x**2)+(5*x)-2
# print("the y value is ", y)

# hours=(45.5/60)
# distance=(14/1.6)
# velocity=(distance/hours, "miles per hour.")
# print("the velocity is ", velocity)

# seconds=5*365*24*60*60
# births= seconds//7
# deaths= seconds//13
# immgrants= seconds//45
# population=312032486
# new_population= population+births+immgrants-deaths
# print("the population in the next five years will be", new_population)

# grade=float(input("please enter student's grade: "))
# if grade < 50:
#  print("the studeent has failed")
# else:
#  print("the student has passed")

# mark=float(input("Please enter the student's mark: "))
# if mark >= 80:
#  grade="A"
# elif mark>=70:
#   grade="B"
# elif mark>=60:
#   grade="C"
# elif mark>=50:
#   grade="D"
# else:
#   grade="f"
# print("their grade is "+grade)

# x=float(input("Please enter your x value"))
# y=float(input("Please enter your y value"))
# if x>0 and y>0:
#   print("this point is located in the 1st quadrant")
# elif x<0 and y>0:
#   print("this point is located in the 2nd quadrant")
# elif x<0 and y<0:
#   print("this point is located in the 3rd quadrant")
# elif x>0 and y<0:
#   print("this point is located in the 4th quadrant")
# else:
#   print("this point is not located in a quadrant")

# num=float(input("Please enter the number: "))
# result= num%2
# if result==0:
#  print("even")
# else:
#   print("odd")

# angle1= float(input("please enter the first angle: "))
# angle2= float(input("please enter the second angle: "))
# angle3= float(input("please enter the third angle: "))
# if angle1+angle2+angle3==180 and angle1==angle2==angle3:
#   print("this is an equilateral triangle")
# elif angle1+angle2+angle3==180 and angle1==angle2!=angle3 or angle1!=angle2==angle3 or angle1==angle3!=angle2:
#   print("this is an isosceles triangle")
# elif angle1+angle2+angle3==180 and angle1!=angle2!=angle3:
#    print("this is an scalene triangle")
# else:
#   print("Err0r!")

# total=0
# for i in range(1,101):
#  total = total + i
# print(total)

# total=0
# n=int(input("enter your integer "))
# for i in range(1,n+1):
#  total= total + i
# print(total)

# user_input=int(input("Enter an integer, the input ends if it is 0:"))
# negative_inputs=0
# positive_inputs=0
# while user_input != 0:
#  user_input=int(input("Enter an integer, the input ends if it is 0:"))
#  if user_input<0:
#   negative_inputs= negative_inputs+1
#  else:
#    positive_inputs= positive_inputs+1

# print("negative numbers: ", negative_inputs )
# print("positive numbers: ", positive_inputs

# lst=input("Please enter a list of value: ").split( )
# lst2=[int(x) for x in lst]
# print(lst2)

# lst=input("Please enter a list of value: ").split(" ")
# lst2=[int(x) for x in lst]
# lst2.sort()
# print(lst2)

# lst=input("Please enter a list of value: ").split(" ")
# lst2=[int(x) for x in lst]
# lst2.reverse()
# print(lst2)

# year=int(input("Enter the year: "))
# if year%4==0:
#  print(True)
# else:
#   print(False)

# def is_even(number):
#   if number % 2 == 0:
#     return True
#   else:
#     return False

# x=int(input("Please enter an integer: "))
# print(is_even(x))

# total=0
# for n in range(1,11):
#   total= total+(n*n)
# print(total)

# total=0
# for n in range(1,11):
#   total= total+(n/(n+1))
# print(total)


# def cube():
#   total=0
#   for n in range(1,51):
#    total = total + n**3
#   return total

# print(cube())

# def fraction():
#   total=0
#   for n in range(1,11):
#     total= total+(n/(n+1))
#   return total

# print(fraction())

# def fraction():
#   total=0
#   for n in range(1,98,2):
#     total= total+(n/(n+2))
#   return total

# print(fraction())

# def integer_n(m):
#   n=1
#   while n**2<= m:
#     n+=1
#     return n
#
# def zz(n):
#   digits=0
#   while n >0:
#     digits+=1
#     n=n//10
#   return digits

# n=int(input("enter n: "))
# print(zz(n))

# lst1=input("enter first list: ").split(" ")
# lst1=[int(x)*2 for x in lst1]
# print(lst1)

# str=input("enter string: ")
# print(str[0: 2])


# name=input("Enter name: ")
# name=name.capitalize()
# print(name)


# string=input("enter string: ")
# def contain_digit(str):
#     lenght=len(str)
#     for n in range(0, lenght):
#         if str[n].isdigit():
#             return True
#     return False
# print(contain_digit(string))


# this 5 btw
# def val_pas(password):
#     lenght=len(password)
#
#     for n in range(0, lenght):
#         if not password[n].isalnum():
#             return False
#         if not password[n].isdigit():
#                  return False
#         if not password[n].isalpha():
#                  return False
#   return True
#
# password=input("Enter Password: ")
# print(val_pas(password))


#password question
# def val_pass(password):
#     lenght=len(password)
#     if lenght<8:
#         return False
#     if not all(x.isalnum for x in password):
#         return False
#     if all(x.isalpha for x in password):
#         return False
#     return True
#
# password=input("enter password: ")
# print(val_pass(password))


#number 7 complited
# def count_letters(string):
#     letters = 0
#     lenght=len(string)
#     for n in range(0, lenght):
#          if string[n].isalpha():
#              letters=letters+1
#     return letters
# string=input("enter letters: ")
# print(count_letters(string))


# number 8 complited
# def spr_sheet(cell):
#     row = ord(cell[0]) - ord("A")
#     column = int(cell[1]) - 1
#     print("the row is", row)
#     print("the column is", column)
#
# cell=input("enter cell: ")
# spr_sheet(cell)


# number 9
# def encrypt(string):
#     new_string=""
#     lenght=len(string)
#     for n in range(0, lenght):
#         new=ord(string[n]) + 2
#         new2=chr(new)
#         new_string+= new2
#     return new_string
# string=input("enter: ")
# print(encrypt(string))


#number10
# def encrypt(string, x):
#     new_string=""
#     x=int(x)
#     for l in string:
#         if (ord(l)+x) <= ord("z"):
#             new = ord(l) + x
#         else:
#             new = (ord(l)+x)-ord("z")+ ord("a") -1
#         new2=chr(new)
#         new_string+= new2
#     return new_string
#
# x=input("enter integer: ")
# string=input("enter string: ")
# print(encrypt(string, x))


#number10 v.2(not working rn)
# def encrypt(string, x):
#     new_string=""
#     x=int(x)
#     for l in string:
#         new = ((ord(l) + x)%25) + ord("a")
#         new2=chr(new)
#         new_string+= new2
#     return new_string
#
# x=input("enter integer: ")
# string=input("enter string: ")
# print(encrypt(string, x))


#worksheet6
#Q1(doing too much)
# def fsh_finder(a, b, c, d):
#     lst=[a, b, c, d]
#     lst2=[int(x) for x in lst]
#     rs=lst2.sort()
#     dv= rs.reverse()
#Q1
# def fish(f1, f2, f3, f4):
#     if f1 < f2 < f3 < f4:
#         print("Fish Rising")
#     elif f1 > f2 > f3 > f4:
#         print("Fish Diving")
#     elif f1 == f2 == f3 == f4:
#         print("Fish Constant")
#     else:
#         print("No Fish")
#
# f1 = int(input())
# f2 = int(input())
# f3 = int(input())
# f4 = int(input())
#
# fish(f1, f2, f3, f4)


#Q2
# def GLD(N):
#     AB_40_count=0
#     for i in range(N):
#         points=int(input("enter points: "))
#         fouls=int(input("enter fouls: "))
#         stars=points*5 - fouls*3
#         if stars > 40:
#             AB_40_count+=1
#     if AB_40_count == N:
#         GD_T="+"
#     else:
#         GD_T="-"
#     print(AB_40_count, GD_T)
#
# N=int(input("enter number of player: "))
# GLD(N)


# new unit
# for t in range(100, 0, -1):
#     for k in range(t, 0, -1):
#         print(k, end=" ")
# print()


#
# for j in range(1, 6):
#     for i in range(j, j + 10):
#         print(i, end=" ")
#     print()


# def displayPattern(n):
#     for t in range(1, n+1):
#         for k in range(t, 0, -1):
#             print(k, end=" ")
#         print()
#
# n = int(input("enter n: "))
# displayPattern(n)


# n = int(input("enter: "))+1
# def pyramid(n):
#     for j in range(1, n):
#         spaces_count = (n - j) * 2
#         print(" " * spaces_count, end="")
#         for i in range(j, 0, -1):
#             print(i, end=" ")
#         for k in range(2, j+1):
#             print(k, end=" ")
#         print()
#
# pyramid(n)


# somethinelse
# total=0
# lst = [4, 6, 8, 9]
# for x in lst:


# TAX = 0.13
# tom_size = 'L'
# helen_size = 'S'
# valdo_size = 'M'
#
# S_shrt = float(input("Enter the price for SMALL shirts: "))
# M_shrt = float(input("Enter the price for MEDIUM shirts: "))
# L_shrt = float(input("Enter the price for LARGE shirts: "))
# print()
# print("{:23}".format("William Store's Prices:"))
# print("{:23}".format("======================="))
# print("{:6}: {:4}".format("Small", S_shrt))
# print("{:6}: {:4}".format("Medium", M_shrt))
# print("{:6}: {:4}".format("Large", L_shrt))
# print()
# print("Helen's size is S")
# H_Qty = int(input("number of shirts they are buying:"))
# print("Tom's size is L")
# T_Qty = int(input("number of shirts they are buying:"))
# print("Valdo's size is M")
# v_Qty = int(input("number of shirts they are buying:"))
# print()
# H_SUB=round(H_Qty * S_shrt)
# T_SUB=round(T_Qty * L_shrt)
# V_SUB=round(v_Qty * M_shrt)
# print("{:8}|{:6}|{:7}|{:5}|{:11}|{:7}|{:8}".format("Customer", " Size", " Price", " Qty", " Sub-total", " tax", " total"))
# print("{:8}|{:6}|{:7}|{:5}|{:11}|{:7}|{:8}".format("Helen", "S", S_shrt, H_Qty, H_SUB, H_SUB * TAX, H_SUB+(H_SUB*TAX)))
# print("{:8}|{:6}|{:7}|{:5}|{:11}|{:7}|{:8}".format("Tom", "L", L_shrt, T_Qty, T_SUB, T_SUB * TAX, T_SUB+(T_SUB*TAX)))
# print("{:8}|{:6}|{:7}|{:5}|{:11}|{:7}|{:8}".format("Valdo", "M", M_shrt, v_Qty, V_SUB, V_SUB * TAX, V_SUB+(V_SUB*TAX)))

# def numb(n):
#    if n == 1:
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print()
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#    elif n == 2:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 3:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 4:
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#    elif n == 5:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 6:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", " "))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 7:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print()
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#    elif n == 8:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 9:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#    elif n == 0:
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print()
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format(" *", "     ", "*"))
#        print("{:2}{:5}{:1}".format("  ", "* * *", " "))
#
#
# n = int(input("Enter a digit between 0 and 9: "))
# numb(n)

# import math
#
# def Cal_dis(point1, point2):
#     return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
#
# def ty_ang(a, b, c):
#     if a**2 + b**2 > c**2:
#         return "Acute"
#     elif a**2 + b**2 == c**2:
#         return "Right Angle"
#     elif a**2 + b**2 < c**2:
#         return "Obtuse"
#     else:
#         return "N/A"
#
# if __name__ == '__main__':
#     num = 0
#     lst_d = []
#     lst_p = []
#     lst_t = []
#     run = True
#     while run:
#         print("Trinangle", num)
#         point1 = [float(p) for p in input("enter the coordinates of first vertex").split(", ")]
#         point2 = [float(p) for p in input("enter the coordinates of second vertex").split(", ")]
#         point3 = [float(p) for p in input("enter the coordinates of third vertex").split(", ")]
#         dis1 = Cal_dis(point1, point2)
#         dis2 = Cal_dis(point3, point2)
#         dis3 = Cal_dis(point1, point3)
#         lst_d.append(dis1)
#         lst_d.append(dis2)
#         lst_d.append(dis3)
#         lst_p.append(point1)
#         lst_p.append(point2)
#         lst_p.append(point3)
#         ty_ang(dis1, dis2, dis3)
#         run = input("Do you wish to enter another triangle? [y/n]: ") == "y"
#         num += 1
#         print()
#
#     print("{:10} | {:12} | {:44} | {:12}".format(" ", "Type", "Points", "Side Lengths"))
#     for i in range(0, len(lst_d), 3):
#         print("{:10} | {:12} | {:44} | {:12}".format("Triangle"+" "+str(i//3), ty_ang(dis1, dis2, dis3), str(lst_p[i])+ str(lst_p[i+1])+ str(lst_p[i+2]), str(lst_d[i])+", "+ str(lst_d[i+1])+", "+ str(lst_d[i+2])))


# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False
#
# year = int(input("enter year: "))
# print(is_leap(year))


# total = 0
# str = input("enter: ")
# for i in range(len(str)):
#    total += int(str[i])
# print(total)

# lst1 = [1, 2, 2, 3, 2, 4, 5, 5, 6, 7, 8]
# lst2 = []
# for i in lst1:
#     if i % 2 == 0:
#         if i not in lst2:
#             lst2.append(i)
# print(lst2)

#
# def factor(x):
#     if int(x) != x:
#         raise Exception("number must be an integer.")
#     for i in range(1, x+1):
#         if x % i == 0:
#             print(i)
#
# def is_prime(x):
#     if x<0 or int(x) != x:
#         raise Exception("number must be a positive integer")
#     total = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             # could
#             total += i
#     if total > (x + 1):
#         return False
#     else:
#         return True
#
# def lst_prime(x):
#     lst = []
#     for k in range(2, x):
#         if is_prime(k):
#             lst.append(k)
#     print(lst)