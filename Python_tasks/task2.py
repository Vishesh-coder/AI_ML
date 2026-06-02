n = [71, 15, 30, 5, 87, 41, 96, 25, 34, 60, 77, 43, 12, 14, 84]
even=[]
odd=[]

for i in n:
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print(f"Even Numbers: {even}")
print(f"Odd Numbers: {odd}")