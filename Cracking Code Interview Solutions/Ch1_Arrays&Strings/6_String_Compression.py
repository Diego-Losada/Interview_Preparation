from collections import Counter

#Create a counter
#Create a string using the counter
#If the lenght of the counter  == len(string) return string

def stringCompression(s):
    counter= Counter(s)
    string = ""
    for key in counter.keys():
        val = counter[key]
        string = string + key + str(val)

    if(len(s) < len(string)):
        return s
    else:
        return string



print(stringCompression("abc"))
        
    
