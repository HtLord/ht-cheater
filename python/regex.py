import re


# group every n char
a = '123456'
ptn = re.compile(r'..')
ptn.findall(a) # ['12', '34', '56']


# Positions
# $, ^

# match numbers
# *, +, ?, {m}, {m, n}


# None greedy
# *?, +?, ??
a = '<a>some value</a>' 
re.match(r'<.*>', a) # will get all string
re.match(r'<.*?>', a) # will get <a>