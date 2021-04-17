# Set retains only unique values
s = set()
print(type(s))
s_from_list = set([1, 2, 3, 4, 5])
print(s_from_list)
print(type(s_from_list))
l = [1, 2, 3, 4, 5]
s_from_list_var = set(l)
print(s_from_list_var)

s.add(1)
s.add(2)
s1 = s.union({1, 2, 3})
print(s, s1)
s1 = s.intersection({1, 2, 3})
print(s, s1)
s1 = s.difference({1, 2, 3})
print(s, s1)
s1 = s.symmetric_difference({1, 2, 3})
print(s, s1)
s1 = s.isdisjoint({1, 2, 3})
print(s, s1)
s1 = s.issubset({1, 2, 3})
print(s, s1)
s1 = s.issuperset({1, 2, 3})
print(s, s1)

s.remove(2)
print(s)


