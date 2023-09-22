import re

text = "112 Places to Stay"
number = int("".join(re.findall(r"\d+", text)))

print(type(number))
