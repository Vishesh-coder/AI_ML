s = 'dw3QF8jSNApvXhrMWaKpja6rgCCk3JvbuIJXoLSc'
count = 0

for i in s:
    if(i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u'):
        count += 1

print(f'Number of vowels in the string: {count}')