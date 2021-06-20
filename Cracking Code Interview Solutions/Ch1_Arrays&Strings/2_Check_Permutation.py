import unittest



#O(n log(n)) Solution

def check_Permutation(s1, s2):
    if len(s1) != len(s2) and s1 == s2:
        return False

    s1, s2 = sorted(s1), sorted(s2)

    for i in range (len(s1)):
        if(s1[i] != s2[i]):
            return False
    return True

#O(n^2) Solution



def check_Permutation2(string1, string2):

    if len(string1) == len(string2) and string1 != string2:

        for letter1 in string1:
            for letter2 in string2:
                if string1.find(letter2) != -1:
                    string1 = string1.replace(letter2, "", 1)
                    string2 = string2.replace(letter2, "", 1)

    if len(string1) == 0 & len(string2) == 0:
        return True
    
    else:
        return False


class Test(unittest.TestCase):

    test_cases = [
        ("hola", "aloh", True),
        ("hi", "i", False),
        ("diego", "ogdie", True),
        ("s", "s", False)]

    def test_p(self):

        for s1, s2, boolean in self.test_cases:
            assert check_Permutation(s1, s2) == boolean 

        


if __name__ == "__main__":
    unittest.main()
