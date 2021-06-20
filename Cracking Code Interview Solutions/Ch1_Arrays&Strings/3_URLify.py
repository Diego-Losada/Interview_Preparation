def URLify(s1, num):
    s1 = s1.strip()
    s1 = s1.replace(" ", "%20")
    return(s1)

if "Mr%20John%20Smith" == URLify("Mr John Smith ", 5):
    print(True)
else:
    print(False)
