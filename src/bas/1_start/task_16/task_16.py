l1 = ['abcd', 786, 2.23, 'john', 70.2]
print(l1)
print(l1[0])
print(l1[2::])
l2 = ['second', '123']
l3 = [l1, l2]
l1[1] = 867
print(l3)
l4 = [l2]
l2[0] = 321
print(l4)