"""
Assignment: Function Return Value Assignment
Program: function_return_value.py
Author: Colby Boell
Last date modified: 02/03/2022

The purpose of this program is to use a basic function to allow user to put in name,
hours, worked and pay rate. It then returns a value back down for us to print. The value
will consist of a string that says employee name and weekly pay. weekly_pay is called
within the hourly_employee_input function
"""


def hourly_employee_input():  # function to get employee input for name, hours, and hourly pay rate
    # prompts for user to input name
    name = input('Please enter your name: ')
    print(' ')
    # prompts for user input of hours with try statement to ensure valid input
    try:
        hours_worked = int(input('Enter hours worked: '))
        if hours_worked >= 0:
            print('Hours recorded', end=': ')
        else:
            hours_worked = 0
    except ValueError as err:
        hours_worked = 0
        print('Invalid input, hours recorded as 0')
    else:
        print(f'{hours_worked} hours worked')
    finally:
        print(' ')
    # prompts user to enter hourly pay rate, try statement to ensure valid input
    try:
        hourly_pay_rate = float(input('Enter your hourly pay rate: '))
        if hourly_pay_rate >= 0:
            print('Hourly pay recorded', end=": ")
        else:
            hourly_pay_rate = 0
    except ValueError as err:
        hourly_pay_rate = 0
        print('Invalid input, pay rate recorded as 0')
    else:
        print(f'${hourly_pay_rate:,.2f} per hour')
    finally:
        print(' ')
    # variable that calls weekly_pay function  to get a value
    week_total_pay = weekly_pay(hours_worked, hourly_pay_rate)
    # returns string
    return f'{name.capitalize()} earned  ${week_total_pay:,.2f} this week'


# function to calculate the weekly pay amount
def weekly_pay(hours_worked, hourly_pay_rate):
    pay_for_week = hours_worked * hourly_pay_rate
    return pay_for_week


# when run the scrip this calls the function
if __name__ == '__main__':
    # variable calling the function to get the return value
    pay_info = hourly_employee_input()
    # prints variable value
    print(pay_info)

"""
Tests:
1.)
Please enter your name: Colby 
 
Enter hours worked: 32
Hours recorded: 32 hours worked
 
Enter your hourly pay rate: 20.18
Hourly pay recorded: $20.18 per hour
 
Colby  earned  $645.76 this week

2.)
Please enter your name: Colby
 
Enter hours worked: hi
Invalid input, hours recorded as 0
 
Enter your hourly pay rate: -89
$0.00 per hour
 
Colby earned  $0.00 this week
"""

