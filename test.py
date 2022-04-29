# My first ever calculator V2.0
#
from colorama import init
from colorama import Back


def main():
	# use Colorama to make Termcolor work on Windows too
	init()

	print(Back.BLUE)

	what = input("What I have to do? (+, -): ")

	a = float(input("Please enter the first number: "))
	b = float(input("Please enter the second number: "))

	print(Back.RED)

	if what == "+":
		c = a + b
		print("Result: " + str(c))
	elif what == "-":
		c = a - b
		print("Result: " + str(c))
	else:
		print("Selected wrong operation!")


if __name__ == '__main__':
    main()
