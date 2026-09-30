s ="hfdsjhf$$$$$$"
s1= s.replace("$", "")
print(s1)
s2="".join([c for c in s if c != "$"])
print(s2)
