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
#
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

# def index_of_min(lst):
#     value = 1000000
#     index_val = 0
#     for i in range(len(lst)):
#         if lst[i] < value:
#            value = lst[i]
#            index_val = i
#     print(index_val)
#
#
# lst = input("enter list:").split(" ")
# lst3 =[int(x) for x in lst]
#
# index_of_min(lst3)

# n = int(input("enter digit: "))
# zz = input("enter: ")
# print(zz[0] + zz[1])
# print("your name is "+ zz.capitalize())

# def pas_wrd(n):
#     if len(n) < 8:
#         return "invalid password"
#     if not any(x.isalnum() for x in n):
#         return "invalid password"
#     if not any(x.isdigit() for x in n) and not any(x.isalpha() for x in n):
#         return "invalid password"
#     return "Valid password"

# print(pas_wrd(zz))

# def encryptz(n, val):
#     f_val = ""
#     for i in val:
#         r = ((ord(i) - ord("a") + n) % 25) + ord("a")
#         thing = chr(r)
#         f_val += thing
#     print(f_val)

# encryptz(n, zz)

# def dice_ten(n, m):
#     tens = 0
#     for i in range(n + 1):
#         for k in range(m+1):
#             if i + k == 10:
#                 tens += 1
#     print("There are", tens, "ways to get the sum 10")
#
# n = int(input("enter: "))
# m = int(input("enter: "))
# dice_ten(n, m)

# def is_magic():
#     r1 = [int(x) for x in input("enter row 1: ").split(" ")]
#     r2 = [int(x) for x in input("enter row 2: ").split(" ")]
#     r3 = [int(x) for x in input("enter row 3: ").split(" ")]
#     r4 = [int(x) for x in input("enter row 4: ").split(" ")]
#     c = []
#     for i in range(4):
#         k = r1[i] + r2[i] + r3[i] + r4[i]
#         c.append(k)
#     if sum(r1) == sum(r2) == sum(r3) == sum(r4) == c[0] == c[1] == c[2] == c[3]:
#         return "Magic"
#     return "not magic"
#
# print(is_magic())

# lst1 =[1, 2, 3, 4, 5]
# lst2 = [6]
# print(lst1 + lst2)

# def is_palindrome(lst):
#     lst2 = lst[::-1]
#     if lst == lst2:
#         return True
#     return False
#
# def pali_leng(lst_1):
#     p = []
#     for k in range(len(lst_1)):
#         for n in range(len(lst_1)):
#             if is_palindrome(lst_1[k:n]):
#                 p.append((n+2) - k)
#
#     p.sort(reverse=True)
#     return p[0]
#
#
# print(pali_leng("abababyabababa"))

# def encryptz(n, val):
#     f_val = ""
#     for i in val:
#         r = ((ord(i) - ord("a") + n) % 25) + ord("a")
#         thing = chr(r)
#         f_val += thing
#     print(f_val)

def rovarspraket(word):
    vowel = ["a", "e", "i", "o", "u"]
    result = ""
    for x in word:
        if x in vowel:
            result += x
        else:
            result += x

            if ord("a") < ord(x) < ord("d"):
                result += "a"
            elif ord("d") <= ord(x) < ord("h"):
                result += "e"
            elif ord("h") <= ord(x) < ord("l"):
                result += "i"
            elif ord("l") <= ord(x) < ord("s"):
                result += "o"
            elif ord("s") <= ord(x) <= ord("z"):
                result += "u"

            if chr(ord(x) +1) in vowel:
                result += chr(ord(x) +2)
            else:
                result += chr(ord(x) + 1)


    return result

print(rovarspraket("joy"))