# Sets in python

l=[1,1, 31, 100]
s= set(l)
s.add(122)
s.add(122)
s1= s.union([12,122, 31, 39])
s2 = s.intersection([12,122, 31, 39])
sett=set([23, 56,89, 1])
# s3= s.copy()
s3= s.difference(sett)

print(s)
print(s1)
print(s2)
print(s3)
