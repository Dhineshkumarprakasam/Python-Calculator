#Total Surface Area

#HISTORY in text file "history"
his=open("history.txt","a")

#1.surface area of circle
def circle():
    r=float(input("Enter the radius of circle : "))
    f=3.14*r*r
    print("Total surface area of circle : ",round(f, 2))
#writing onto the text file
    his.write("\nTotal surface area of Circle:-")
    his.write("\nRadius : "+str(r))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()

    
    
#2.surface area of rectangle
def rectangle():
    l=float(input("Enter the length of rectangle : "))
    w=float(input("Enter the width of rectangle : "))
    f=l*w
    print("Total surface area of rectangle : ",round(f,2))
#writing onto the text file
    his.write("\nTotal surface area of Rectangle:-")
    his.write("\nLenghth of rectangle : "+str(l))
    his.write("\nWidth of rectangle : "+str(w))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#3.surface area of square
def square():
    s=float(input("Enter the length of side of square : "))
    f=s*s
    print("Total surface area of square : ",round(f,2))
#writing onto the text file
    his.write("\nTotal surface area of Square:-")
    his.write("\nSide : "+str(s))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
    
#4.surface area of triangle
def triangle():
    b=float(input("Enter the base of triangle : "))
    h=float(input("Enter the height of triangle : "))
    f=1/2*b*h
    print("Total surface area of triangle : ",round(f,2))
#writing onto the text file
    his.write("\nTotal surface area of Triangle:-")
    his.write("\nBase : "+str(b))
    his.write("\nHeight : "+str(h))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#5.surface area of cube
def cube():
    s=float(input("Enter the length of side of cube : "))
    f=6*s*s
    print("Total surface area of cube : ",round(f,2))
#writing onto the file
    his.write("\nTotal surface area of Cube:-")
    his.write("\nSide : "+str(s))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#6.surface area of cuboid
def cuboid():
     h=float(input("Enter the height of cuboid : "))
     l=float(input("Enter the length of cuboid : "))
     b=float(input("Enter the breadth of cuboid : "))
     f=2*(l*b+b*h+h*l)
     print("Total surface area of cuboid : ",round(f,2))
#writing onto the file
     his.write("\nTotal surface area of Cuboid:-")
     his.write("\nHeight : "+str(h))
     his.write("\nLenght : "+str(l))
     his.write("\nBreadth : "+str(b))
     his.write("\nSurface area : "+str(round(f,2)))
     his.flush()
     
#7.surface area of sphere
def sphere():
    r=float(input("Enter the radius of sphere : "))
    f=4*3.14*r*r
    print("Total surface area of sphere : ",round(f,2))
#writing onto the file
    his.write("\nTotal surface area of Sphere :- ")
    his.write("\nRadius : "+str(r))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#8.surface area of cylinder
def cylinder():
    r=float(input("Enter the radius of cylinder : "))
    h=float(input("Enter the height of cylinder : "))
    f=2*3.14*r*(r+h)
    print("Total Surface area of cylinder : ",round(f,2))
#writing onto the file
    his.write("\nTotal surface area of Cylinder:-")
    his.write("\nRadius : "+str(r))
    his.write("\nHeight : "+str(h))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#9.surface area of cone
def cone():
    r=float(input("Enter the radius of cone           : "))
    l=float(input("Enter the slant height of cone  : "))
    f=3.14*r*(l+r)
    print("Total Surface area of cone : ",round(f,2))
#writing onto the file
    his.write("\nTotal surface area of Cone:-")
    his.write("\nRadius : "+str(r))
    his.write("\nSlant Height : "+str(l))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
    
#10.surface area of hemisphere
def hemisphere():
    r=float(input("Enter the radius of hemisphere : "))
    f=3*3.14*r*r
    print("Total Surface area of hemisphere : ",round(f,2))
#writing onto the file
    his.write("\nTotal surface area of Hemisphere:-")
    his.write("\nRadius : "+str(r))
    his.write("\nSurface area : "+str(round(f,2)))
    his.flush()
