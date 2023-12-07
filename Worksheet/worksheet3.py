# total=0
# for i in range(1,101):
#  total = total + i
# print(total)

# total=0
# n=int(input("enter your integer "))
# for i in range(1,n+1):
#  total= total + i
# print(total)

def chek_CHarge():
    user_input = input("Enter an integer, the input ends if it is 0:")
    if not user_input.isdigit():
        raise ValueError
    user_input = eval(user_input)
    negative_inputs=0
    positive_inputs=0
    while user_input != 0:
        user_input = input("Enter an integer, the input ends if it is 0:")
        if not user_input.isdigit():
            raise ValueError
        user_input = eval(user_input)
    if user_input<0:
        negative_inputs = negative_inputs+1
    else:
        positive_inputs= positive_inputs+1

    print("negative numbers: ", negative_inputs )
    print("positive numbers: ", positive_inputs)

try:
    chek_CHarge()
except ValueError:
    print("bhjghfycyf")