from criticalpath import Node

p = Node('project')

a = p.add(Node('A', duration=14))
b = p.add(Node('B', duration=20))
c = p.add(Node('C', duration=3))
d = p.add(Node('D',duration=20))
e = p.add(Node('E', duration=8))
f = p.add(Node('F', duration=11))
g = p.add(Node('G', duration=13))
h = p.add(Node('H', duration=20))

links = [(a,d), (a,b), (b,c), (d,g), (c,g), (c,e), (d,e), (e,f), (g,h), (f,h)]

for link in links:
    p.link(*link)

p.update_all()

print(p.get_critical_path())
print(p.duration)
