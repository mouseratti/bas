from variables import l1, l2, l3, l4

print(l1)
print('First is ',l1[0])
print('>= 3 ',l1[2::])

l3.append(l1)
l3.append(l2)

print('l3 = ',l3)

l1[1]=100
print('l1[1] = ',l1[1])

print('l3 = ',l3)

l4.append(l2)
print('l4 = ',l4)

l2[0]='first'
print('l2[0] = ',l2[0])

print('l4= ',l4)


