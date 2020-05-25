import re

text = '''"Whether you think you can or
whether you think you can't,
you're right!
-HENRY FORD-'''

text = text.lower()
print("# of Chars: {}".format(len(re.sub(r'\W', '', text))))
print("# of Chars: {}".format(re.subn(r'e', '', text)[1]))

