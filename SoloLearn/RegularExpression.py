import re

pattern = r"spam"

"""
if re.search(pattern, "asdaspamfadsdfas"):
    print('Match')
else:
    print("Doesn't match!")
"""

#print(re.findall(pattern, "eggsspamspammilk"))

match=re.search(pattern, "eggspampampamrampamspam")

print(match.end())
print(match.start())
print(match.group())
print(match.span())