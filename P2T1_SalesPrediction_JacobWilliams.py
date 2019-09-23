#Determine company's annual profit
#09/22/19
#CTI-110 P2T1 - Sales Prediction
#Jacob Williams
#
#Get total sales.
total_sales=float(input('Enter projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit=total_sales*0.23

#Display total profit.
print('The profit is $',format(profit, ',.2f'))
