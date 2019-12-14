lst=[x for x in range(1,100) if x%2==0]
genexp=(x for x in range(1,100) if x%2==0)
print(genexp)
for x in genexp:
    print(x)
