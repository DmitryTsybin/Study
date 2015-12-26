def generator():
    for i in (1, 2, 3):
        print("print in generator: ", i)
        yield i

g = generator()  # create a generator
print(g)

for i in g:
    print(i)

f = generator()
for n in f:
    print(n)