def Check_SSN(x):
    if not x[0:2].isdigit():
        return "Invalid SSN"
    if x[3]!= '-' or x[6] != '-':
        return "Invalid SSN"
    if not x[4:5].isdigit():
        return "Invalid SSN"
    if not x[7:].isdigit():
        return "Invalid SSN"
    return "Valid SSN"

# x = input("enter ")
# print(Check_SSN(x))

def check_substrings():
    string1 = input("enter: ")
    string2 = input("enter: ")
    if string1.find(string2) == -1:
        return False
    return True

# print(check_substrings())

def pas_wrd(n):
    total= 0
    if len(n) < 8:
        return "invalid password"
    if not any(x.isalnum() for x in n):
        return "invalid password"
    if not any(x.isdigit() for x in n) and not any(x.isalpha() for x in n):
        return "invalid password"
    for x in n:
        if x.isdigit():
            total+= 1
    if total<2:
        return "invalid password"
    return "Valid password"

def countLetters(s):
    total = 0
    for k in s:
        if k.isalpha():
            total += 1
    return total

print(countLetters("y6y6y6y6"))

def find_genes(x):
    starting_gene = x.find("ATG")

