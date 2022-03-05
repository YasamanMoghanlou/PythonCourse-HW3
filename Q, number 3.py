# a, b, c, d, e are numbers

a = int (input ("please enter a: "))
b = int (input ("please enter b: "))
c = int (input ("please enter c: "))
d = int (input ("please enter d: "))
e = int (input ("please enter e: "))

# I used if else loop here so that if there were duplicates it'll write Duplicate
# otherwise it'll write All unique


if a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e:
    print ("Duplicate!")

else:
    print("All unique!")