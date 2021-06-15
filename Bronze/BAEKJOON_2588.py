A = int(input())
B = str(input())

s1 = A * int(B[-1])
s2 = A * int(B[-2])
s3 = A * int(B[0])

print(s1)
print(s2)
print(s3)
print(s3*100 + s2 * 10 + s1)
