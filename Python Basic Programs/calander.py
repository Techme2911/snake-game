# program 2 (updated)

# Program to show the calender of a specific month of a year

# First import the calendar module  
import calendar  
# ask of month and year  
yy = int(input("Enter the year:"))  
mm = int(input("Enter the month:"))  
# display the calendar  
print(calendar.month(yy,mm))
