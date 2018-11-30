import re
FILENAME = "phone_list"
regex = re.compile('(79|89|77|9)(\d{9})')
st1 = ''
phone_norm = []
f = open(FILENAME, "r")
phone = list(f.readlines())
for x in range(0, phone.__len__()):
    st = str(phone[x])
    for y in range(0, st.__len__()):
        if st[y].isdigit():
            st1 = st1 + st[y]
    phone_norm.insert(x, st1)
    st1 = ''
for x in range(0, phone_norm.__len__()):
    if re.match(regex, phone_norm[x]):
        print(phone[x])


