f = open('loremipsum.txt')

print(f.read())

print(f.read())

f.seek(0)

print(f.read())

f.seek(0)

print(f.readline())

f.seek(0)

print(f.readlines())

print(f.closed)
f.close()
print(f.closed)