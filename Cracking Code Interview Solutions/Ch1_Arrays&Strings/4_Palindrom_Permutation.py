from collections import Counter


def Palindrome_Permutation(s):

    #Go through each character and store character in dictionary if
    #it is hasn't been stored yet. If it has been stored then, increase
    #the number by 1.
    #Do not store the space
    dic = {}
    
    s = s.replace(" ", "")
    s = s.lower()
    for let in s:
        if(dic.get(let) == None):
            dic[let] = 1
        else:
            dic[let] += 1


    #If there are even numbers of characters that is not the space, then their
    #values has to be the same. If not
    print(dic)
    arr = dic.values()
    odd = 0


    for num in arr:
        if (num % 2 == 1):
            odd += 1
            if(odd > 1): return False    
        
    return True

def palindrome_git_solution(s):


    s = s.replace(" ", '').lower()
    dic = Counter(s)
    print(dic)

    odd = 0

    for val in dic.values():
        if (val % 2 == 1):
            odd += 1
            if(odd >1):
                return False

    return True
    



def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1


if (palindrome_git_solution("Taco cat") == True):
    print("Pass")
else:
    print("Not Pass")
