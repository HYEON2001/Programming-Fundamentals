import re

email = input("Type your email: ")

pattern = r'^[A-Za-z0-9-_.]{5,}@[A-Za-z0-9-_.]{5,}\.com$'
print(re.search(pattern, email)  != None)
