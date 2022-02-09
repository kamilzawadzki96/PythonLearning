import random
import string

#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
s = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
passlen = 14
p =  "".join(random.sample(s,passlen ))
print(p)