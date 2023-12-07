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