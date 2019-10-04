#CTI-110
#P3HW2 - MealTipTax
#Jacob Williams
#10/04/19
#Calculate total cost of a meal including tax and tip
#
#PsuedoCode
#Have user input cost of food
#Have user select available tip percentage
#If correct percentage is chosen calculate total
#If incorrect percentage is chosen display error message




#Get cost of food.
Food_Cost =float(input('Enter Cost of Meal:$'))

#Get tip amount
Tip_Input =input ("Enter Tip Percentage 16% 18% or 20%:")

#Calculate Tip
Tip= (Tip_Input*Food_Cost)/100

#Get tax amount
Taxes=float(Food_Cost*.06)
#Calculate Total if correct tip is chosen
Total=(Food_Cost+Tip+Taxes)
if Tip_Input==16:
    print("Cost of food: $",format(Food_Cost, '.2f'))
    print("+")
    print("Tip amount:$",format(Tip,'.2f'))
    print("+")
    print("Tax:$",format(Taxes,'.2f'))
    print("")
    print("Total:$",format(Total,'.2f'))
elif Tip_Input==18:
    print("Cost of food: $",format(Food_Cost, '.2f'))
    print("+")
    print("Tip amount:$",format(Tip,'.2f'))
    print("+")
    print("Tax:$",format(Taxes,'.2f'))
    print("")
    print("Total:$",format(Total,'.2f'))
elif Tip_Input==20:
    print("Cost of food: $",format(Food_Cost, '.2f'))
    print("+")
    print("Tip amount:$",format(Tip,'.2f'))
    print("+")
    print("Tax:$",format(Taxes,'.2f'))
    print("")
    print("Total:$",format(Total,'.2f'))
#Display error message if incorrect value is inserted
elif Tip_Input!=16:
    print("Error: Please choose 16%,18% or 20%")
elif Tip_Input!=18:
    print("Error: Please choose 16%,18% or 20%")
elif Tip_Input!=20:
    print("Error: Please choose 16%,18% or 20%")

