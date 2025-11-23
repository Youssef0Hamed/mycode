x = float(input("enter angle " ))
y = float(input("enter angle" ))
z = float(input("enter angle" ))
if x !=  0 or  y != 0 or x!= 0 :
    if x+y+z ==180 :
        if x == y == z :
            print("this is equilateral triangle ")
        elif x == 90 or  y == 90 or z == 90 :
            print("this is right angle triangle")
        elif x ==  y or  y == z  :
            print("this is isosceles triangle")    
        elif x !=  y or  y != z or x!=z  :
            print("this is scalene triangle")    
