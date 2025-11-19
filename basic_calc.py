class BasicCalc:
    def add(self, a, b):
        return a + b


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    calc = BasicCalc()
    total = calc.add(num1, num2)

    print(f"{num1} + {num2} = {total}")


if __name__ == "__main__":
    main()