# a, b, c are numbers and sides of the triangle

a = int (input ("please enter a: "))
b = int (input ("please enter b: "))
c = int (input ("please enter c: "))

# then we use the formula of the right triangle with if loop

if a ** 2 + b ** 2 == c ** 2 :
    print ("Right")
    
else:
    print ("Not right")
    
    
# if you write a: 3, b: 4, c: 5 it will write --> right
# if you write a: 2, b: 2, c: 2 it will write --> Not right