#CTI-110
#P3HW1 - Month Number
#Jacob Williams
#10-04-19
#
#Convert user inputed number to month of the year

#PsuedoCode
#Ask user to input number of desired month
#Assign user input to User_Input variable
#Use user input to print name of month input
#Create error message if input is not between 1-12



#Get input from user
User_Input =input("Enter number of desired month:")
#Use user input to print correlating month name
if User_Input =='1':
    print("January")
elif User_Input =='2':
    print('February')
elif User_Input =='3':
    print('March')
elif User_Input =='4':
    print('April')
elif User_Input =='5':
    print('May')
elif User_Input =='6':
    print('June')
elif User_Input =='7':
    print('July')
elif User_Input =='8':
    print('August')
elif User_Input =='9':
    print('September')
elif User_Input =='10':
    print('October')
elif User_Input =='11':
    print('November')
elif User_Input =='12':
    print('December')
#Print error message if User_Input is outside of the 1-12 range
if User_Input >'12':
    print('Please enter a number between 1-12')
if User_Input < '1':
    print('Please enter a number between 1-12')
