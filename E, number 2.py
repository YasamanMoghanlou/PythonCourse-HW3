val = int (input("please enter a number: "))
if val < 10:
    if val != 5:
        print ("wow ", end='')
        
    else:
        if val == 17:
            val += 10
            
        else:
            print ("whoa ", end='')
            
print (val) 


# a) the program will print "wow 3"  if we give the input number 3
# b) the program will print "21"     if we give the input number 21
# c) the program will print "whoa 5" if we give the input number 5
# d) the program will print "17"     if we give the input number 17
# e) the program will print "wow -5" if we give the input number -5