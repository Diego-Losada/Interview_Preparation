"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Input: String
Output: Boolean
"""
#O(n)
def IsUnique(string):
    string2 = ''
    string = string.lower()

    for char in string:
        if char not in string2:
            string2 += char
    
    if string == string2:
        return True
    else:
        return False

#O(n) Where n is the length of the strings
def IsUniquePython(string):
    return set(string) == set(string.lower())

print(IsUnique('Mama'))
print(IsUnique('Coding'))
print(IsUnique('Coc'))

print(IsUniquePython('Mama'))
print(IsUniquePython('Coding'))
print(IsUniquePython('Coc'))
