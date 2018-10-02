#Get the projected total sales
#October 1, 2018
#CTI-110 P2T1 - Sales Prediction
#Hayden Diaz
# 1. Create function of projected Sales (ask user)
# 2. Create function for profit
# 3. Calculate profit
# 4. Display total profit

totalSales= float ( input ("Enter the projected sales: "))


profit= totalSales * (.23)

print ("Your profit is: $", format (profit, ',.2f'), sep='')
