# the income is the amount of the payment which is number

income = int (input ("please enter the income: "))

# here we write if it's less than 1000 there is no need to pay tax
if income < 1000 : 
    tax = 0 * income 
   
# if the payment is between 1000 and 2500 you have to pay 10% of it as tax 
elif 1000 < income <= 2500 :
    tax = 0.1 * income
    
# if the payment is between 2500 and 4000 you have to pay 15% of it as tax
elif 2500 < income <= 4000 :
    tax = 1.5 * income
# if the payment is between 4000 and 6000 you have to pay 20% of it as tax    
elif 4000 < income <= 6000 :
    tax = 0.2 * income
    
# if the payment is greater than 8000 you have to pay 30% of it as tax    
else: 8000 < income
tax = 0.3 * income 
  

# here I used format string    
print (f"tax: {tax}" )