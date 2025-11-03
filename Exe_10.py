def evod(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    num = int(input("Enter a number: "))
    msg = evod(num)
    print(msg)
if __name__ == "__main__":
    main()