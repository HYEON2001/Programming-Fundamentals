def isPalindrome(s):
    if s != s[::-1]:
        return False
    else:
        return True

input_str = input("input : ")

if isPalindrome(input_str) == True:
    print("Yes")
else:
    print("NO")
