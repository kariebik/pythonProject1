# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False

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

# class Square:
#     def __init__(self, side_l):
#         self.side = side_l
#
#     def perimeter(self):
#         return 4 * self.side
#
#     def area(self):
#         return self.side**2
#
#
# if __name__ == '__main__':
#     square1 = Square(5)
#     print(square1.perimeter())

# class Triangle:
#     def __init__(self, base, height, side):
#         self.base = base
#         self.height = height
#         self.side = side
#
#     def area(self):
#         return self.base * self.height / 2
#
#     def perimeter(self):
#         return

# class Cuboid:
#     def __int__(self, length, breadth, height):
#         self.height = height
#         self.length = length
#         self.breadth = breadth
#
#     def volume(self):
#         return self.height * self.length * self.breadth
#
#     def surface_area(self):
#         return ((self.breadth * self.height) + (self.breadth * self.length) + (self.height * self.length)) * 2
#
#
# if __name__ == '__main__':
#     cuboid1 = Cuboid(6, 4, 5)
#     print(cuboid1.volume())

# import math
# class RegularPolygon:
#     def __init__(self, n_side, lenght, x=0, y=0):
#         self.__n_side = n_side
#         self.__length = lenght
#         self.__x = x
#         self.__y = y
#     def perimeter(self):
#         return self.__n_side * self.__length
#     def get_area(self):
#         return (self.__n_side * self.__length**2)/(4*math.tan(math.pi/self.__n_side))

# class Stock:
#     def __init__(self, symbol, name, previous_price, current_price):
#         self.__symbol = symbol
#         self.__name = name
#         self.__previous_closing_price = previous_price
#         self.__current_price = current_price
#
#     def get_symbol(self):
#         return self.__symbol
#     def get_name(self):
#         return self.__name
#     def get_previous_closing_price(self):
#         return self.__previous_closing_price
#     def get_current_price(self):
#         return self.__current_price
#
#     def get_change_percent(self):
#         return ((self.__previous_closing_price - self.__current_price)/self.__current_price) * 100
#
# if __name__ == '__main__':

# def check_bids(n):
#     names = []
#     bids = []
#     max_bid = 0
#     max_index = ""
#     if 1<= n <= 100:
#         for i in range(n):
#             name = input()
#             bid = int(input())
#             names.append(name)
#             bids.append(bid)
#             if bids[i] > max_bid:
#                 max_bid = bids[i]
#                 max_index = names[i]
#
#     return max_index
#
# n = int(input(""))
# print(check_bids(n))

# P = int(input("enter p"))
# N = int(input("enter n"))
# R = int(input("enter r"))
#
# days = 0
# tot_sik = N
#
# while tot_sik < P:
#     tot_sik *= tot_sik*R
#     days += 1
# print(days)

# def shift_num(n, k):
#     total = n
#     for i in range(1, k+1):
#         total+= n*10**i
#     return total
#
# n = int(input())
# k = int(input())
# print(shift_num(n, k))

# import math
# def Cal_dis(point1, point2):
#     return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
#
# def hypotenuse(point1, point2, point3):
#     a = Cal_dis(point1, point2)
#     b = Cal_dis(point2, point3)
#     c = Cal_dis(point1, point3)
#     if a**2 + b**2 != c**2:
#         raise Exception("must be a right angle triangle")
#     print(c)
#
# if __name__ == '__main__':
#     point1 = [int(x) for x in input("enter the coordinates of first vertex").split(", ")]
#     point2 = [int(p) for p in input("enter the coordinates of second vertex").split(", ")]
#     point3 = [int(p) for p in input("enter the coordinates of third vertex").split(", ")]
#     hypotenuse(point1, point2, point3)

# x = eval(input())
# def factor(x):
#     if int(x) != x:
#         raise Exception("number must be an integer.")
#     for i in range(1, x+1):
#         if x % i == 0:
#             print(i)
#
# factor(x)

# def is_prime(x):
#     if x<0 or int(x) != x:
#         raise Exception("number must be a positive integer")
#     total = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             total += i
#     if total > (x + 1):
#         return False
#     else:
#         return True
#
# x = eval(input("enter number: "))
# # print(is_prime(x))
#
# def lst_prime(x):
#     lst = []
#     for k in range(2, x):
#         if is_prime(k):
#             lst.append(k)
#     print(lst)
#
# lst_prime(x)
