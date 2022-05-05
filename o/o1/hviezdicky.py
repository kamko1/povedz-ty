n = int(input("n = "))

for i in range(n):
    print((i+1) * "* ")
print()
for k in range(n):
    print((n-k) * " " + n * " * ")
print()
for j in range(n+1):
    print((n+1 + n-1) * " " + j *  " *")
    n -= 1
