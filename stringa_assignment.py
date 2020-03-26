# Exercise 5
#The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string)

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# This function checks if the letter is lowercase, if it is it returns true. If the letter is not lowercase, it returns false. This function checks if it is a lowercase and returns a boolean. 


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# This checks if the string 'c' is lowercase, which it is, and returns a string 'True"


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# this checks if the letter c is lowercase, and stores the boolean True or False depending on if it's true or not to the variable flag. It then prints flag.


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# This checks if the letter is lowercase and returns a boolean. The flag prints either true or false depending on the answer, as it prints either the already states false or the boolean found with istrue. The or function searches for the true, so this really is uncessary with initiating flag as false and printing that value or the boolean as it would always print out the boolean info.


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# This checks if the letter is lowercase with a boolean statement. It states if it is not lowercase (if islower is false) return false. otherwise it prints nothing and then prints true outide the if statement.

#print(any_lowercase5("And"))

# Exercise 6
def rotate_word(number, string):
    
    number = int(number)
    string = string.lower()
    new = ''
    for i in string:
        code = ord(i) + number
        new = new + chr(code)
    return new

print(rotate_word(7, "cheer"))
print(rotate_word(-10, "melon"))
