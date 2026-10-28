def sqr(n):
    if n == 0:
        return 0
    else:
        return n**2

if __name__ == "__main__":
    num = int(input("Enter a Number to be Squared: "))
    print(sqr(num))