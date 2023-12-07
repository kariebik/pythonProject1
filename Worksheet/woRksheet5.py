# str=input("enter string: ")
# print(str[0: 2])

string=input("enter string: ")
def contain_digit(tr):
    if not isinstance(tr, str):
        raise ValueError
    lenght=len(tr)
    for n in range(0, lenght):
        if tr[n].isdigit():
            return True
    return False
try:
    print(contain_digit(string))
except ValueError:
    print("")
