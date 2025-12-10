#basic calculator class
import logging
import mylib
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()

class BasicCalc:
    #this project is a basic calcuulator which is adding and subtracting two numbers
    def add(self, a, b):#calling my functions
        return a + b
    def sub(self, a, b):
        return a - b

#Function for adding
def add():
    num1 = int(input("Enter the first number: "))#takes two values, both integers
    num2 = int(input("Enter the second number: "))

    calc = BasicCalc()
    total = calc.add(num1, num2)

    print(f"{num1} + {num2} = {total}")

#Function for subtracting numbers
def sub():
    num1 = int(input("Enter the first number: "))#takes two values, both integers
    num2 = int(input("Enter the second number: "))

    calc = BasicCalc()
    total = calc.sub(num1, num2)

    print(f"{num1} - {num2} = {total}")

if __name__ == "__main__":
    main()

#end