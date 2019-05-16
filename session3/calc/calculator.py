#!/usr/bin/python3
import psycopg2 as pg
from pprint import pprint


def store(num1, num2, op, res):
    cursor = conn.cursor()
    cursor.execute("""insert into tab_calc values(%d, %d, %s, %f)""" % (num1, num2, op, res))

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
	b = true
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        res = (number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        res = (number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        res = (number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        res = (number_1 / number_2)
    else:
		b = false
        print('You have not typed a valid operator, please run the program again.')

	store(number_1, number_2, operation, res)

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


def welcome():
    print('''
Welcome to Calculator
''')


try:
	connect_str = """dbname='calc_db' user='postgres' host='localhost'"""
	conn = pg.connect(connect_str)
except Exception as e:
    print("Error occured when connecting to database")
else:
	welcome()
	calculate()
