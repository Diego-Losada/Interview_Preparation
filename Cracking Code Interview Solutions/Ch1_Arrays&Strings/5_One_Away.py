from collections import Counter

def oneAway(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)
    dif = count1 -count2

    num = 0
    for val in dif.values():
        num += val
    if (num <=1):
        return True
    else:
        return False

print(oneAway("pales", "pale"))


#Split two strings

#Make two Counters

#Calculate the difference of the counters into a new counter

#if len(Counter.keys()) <= 1: return True else return False

