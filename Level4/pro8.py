note = []
book=[]
for i in range(10):
    note.append(int(input()))

for i in range(10) : 
    a=note[i]%42
    if a not in book:
        book.append(a)

print(len(book))