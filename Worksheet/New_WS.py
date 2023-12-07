#Question 1

# def mood_read(x):
#     if x.count(":-)") > x.count(":-("):
#         print("happy")
#     elif x.count(":-)") < x.count(":-("):
#         print("sad")
#     elif x.count(":-)") == x.count(":-("):
#         print("unsure")
#     else:
#         print("none")
#
#
# z = input("enter text: ")
#
# mood_read(z)

#Question 2

# def vote_counter():
#     vot_num = int(input())
#     x = input()
#     if x.count("A") + x.count("B") != vot_num:
#         raise ValueError
#     if x.count("A") > x.count("B"):
#         print("A")
#     elif x.count("A") < x.count("B"):
#         print("B")
#     elif x.count("A") == x.count("B"):
#         print("Tie")
#
# try:
#     vote_counter()
# except ValueError:
#     print("The number of votes entered isn't equal to the number of votes")

#Question 3

