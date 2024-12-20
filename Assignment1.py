#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Saira Munawar
Semester: Fall 2024
Description: Completed Assignment 1 - Usage, Main and Valid Date
'''

import sys

def leap_year(year: int) -> bool:
    ''' "return true if the year is a leap year." '''
    if year % 4 == 0: #checks if the year is divisable by 4 (1900 is)
        if year % 100 == 0: #then it checks if the year is divisable by 100 (1900 is)
            if year % 400 == 0: #finally checks if the year is divisable by 400 (1900 is not)
                return True #if it is divisable by 400, it is a leap year
            else:
                return False #if not, then it is not a leap year, 1900 is not.
            return False # if it is divisable by 100, it is not a leap year
        else:
            return True #if it is not divisable by 100, then it is a leap year
        return True # if it is divisable by 4 then it is divisable
    else:
        return False #if not divisable by 4, it is not a leap year

def mon_max(month:int, year:int) -> int:
    ''' "return the last day of the month." '''
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year): #Unless it is both a leap year and Feb - this calls the leap_year() function
        mon_max = 29 #Then Feb last day is 29
        return mon_max
    else:
       return mon_dict[month] #changed it to remove the built in function called get(month). Both do the same thing.  
 
def after(date: str) -> str: 
    #accepts a string parameter named date and will return a string
    '''
    after() -> date for next day in DD/MM/YYYY string format
    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day = (int(x) for x in date.split('-')) #takes date: "DD/MM/YYYY", uses in-built function .split to seperate string and assigns it to day, mon, year using the for loop.
    #changed the order from day, mon, year because the orginally, the YYYY was going to the day and the DD was going to the year + changed '/' to '-' which were being used in test.
    day += 1  # next day
    
    last_day = mon_max(mon, year) #calls the mon_max function
    #determines if day is greater than the last day of the month
    if day > last_day: 
        mon += 1 #if so, go to the next month Jan 32 will go to Feb 1
        if mon > 12: #if the month is more than december
            year += 1 #add a year
            mon = 1 #start again at Jan
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}" #returns the next day/ changed the format to year, month, day instead of day, month, year. ALso removed the / and changed it to -
    
def before(date: str) -> str:
    '''
    before() -> date for previous day in DD/MM/YYYY string format
    Return the date for the previous day of the given date in DD/MM/YYYY format.
    '''   
    year, mon, day = (int(x) for x in date.split('-')) #takes date: "DD/MM/YYYY", uses in-built function .split to seperate string and assigns it to day, mon, year using the for loop.
    day -= 1  # previous day.
    #determine if day is less than the first day of the month.
    if day < 1:
        mon -= 1 #if so, go to the previous month
        if mon < 1: #month cannot go past Jan so
            year -= 1 #go to the previous year 
            mon = 12 #start in december (Jan -> Dec)
        day = mon_max(mon, year) # if tmp_day < this month's max, reset to 31
    return f"{year}-{mon:02}-{day:02}" #returns the previous date. 

def usage():
    '''"Print a usage message to the user"'''
    if len(sys.argv) != 3: #if argument length is less than 3 - 3 arguments, 1: file name, 2: date, 3: divisor
        print('Usage: ' + str(sys.argv[0]) + ' DD/MM/YYYY division')
        sys.exit()
    elif (sys.argv[2] == '0'): #if divisor is '0'
        print('Usage: ' + str(sys.argv[0]) + ' DD/MM/YYYY division')
        sys.exit()
    elif len(sys.argv) == 3 and sys.argv[2] != 0 and not valid_date(str(sys.argv[1])):
        #if arg are 3, and division is not 0 and if valid date returns false:
        print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY division")
        sys.exit()

def valid_date(date: str) -> bool:
    '''"check validity of date"  '''
    year, mon, day = (int(x) for x in date.split('-')) #takes date: "DD/MM/YYYY", uses in-built function .split to seperate string and assigns it to day, mon, year using the for loop.
    #last_day = mon_max(mon, year) this causes an error with the dictonary (month 25 doesn't exist which breaks the dict. To fix this, I moved this line after month and year error checking)
    if year < 1000 or year > 9999: #check if the year is higher than 1000 and less than 10000
        print('Error: wrong year entered')
        return False #if so it returns false
    elif mon < 1 or mon > 12: #if month is less than 1 and higher than 12
        print('Error: wrong month entered')
        return False #return false
    last_day = mon_max(mon, year) #last day is the correct last day of the given date. 2021-02 last day is 28 not 29
    if day <= 0 or day > last_day: #if day is not the same as the correct last day/over it and if day is 0
        print('Error: wrong day entered')
        return False 
    else: 
        return True #else returns true

def dbda(start_date: str, step: int) -> str:
    '''"given a start date and a number of days into the past/future, give date"'''
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    if step > 0: ##if step is a postive number (5 for ex)
        for i in range(step): ##loop increment 5 times,
            start_date = after(start_date) #increasing the date 1 each time (date:jan 1 -> jan 2, loop iterates and become jan 3)
    elif step < 0: #if step is a negative number
        for i in range(-(step)): #loop decrement 5 times (-5) - changed it to be more clear what this step does -(-5) = 5 
            start_date = before(start_date) #which decreases the date by 1 each time (date:jan 1 -> dec 31, loop iterates and become dec 30)
    return start_date #returns the date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    usage() #this always sys.exits 

    total_days = round(365 / int(sys.argv[2])) #shows the total day for dbda() after  
    negative_days = (-(total_days)) #this creates the negative days for dbda() for dbda() before 
    print('A year divided by ' + str(sys.argv[2]) + ' is ' + str(total_days) + ' days.') 
    print('The date ' + str(total_days) + ' days ago was ' + dbda(str(sys.argv[1]), negative_days))
    print('The date ' + str(total_days) + ' days from now will be ' + dbda(str(sys.argv[1]), total_days))
