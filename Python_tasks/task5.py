s = 'dw3QF8jSNApvXhrMWaKpja6rgCCk3JvbuIJXoLSc'
count = 0

for i in s:
    if i.lower() in 'aeiou':
        count += 1

print(f'Number of vowels in the string: {count}')