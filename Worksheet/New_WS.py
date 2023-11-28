#Question 1
def mood_read(x):
    if x.count(":-)") > x.count(":-("):
        print("happy")
    elif x.count(":-)") < x.count(":-("):
        print("sad")
    elif x.count(":-)") == x.count(":-("):
        print("unsure")
    else:
        print("none")


z = input("enter text: ")

mood_read(z)
print("hello")