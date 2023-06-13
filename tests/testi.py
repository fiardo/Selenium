import re



a = "123@@#jkaf"


normal = int("".join(ch for ch in a if ch.isdigit()))
print(normal)
print(type(normal))