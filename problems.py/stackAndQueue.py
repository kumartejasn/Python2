# stack

from collections import deque

d=deque("teja")
d.append("s")
print(d)
d.appendleft("N")
print(d)
d.pop()
print(d)
d.popleft()
print(d)

print(list(d))

d.extend("feds")
print(d)
d.extendleft("ds")
print(d)

print(list(reversed(d)))


# l=[]
# l.append("t")
# print(l)
# l.append("f")
# print(l)
# l.append("k")
# print(l)
# l.append("g")
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)




