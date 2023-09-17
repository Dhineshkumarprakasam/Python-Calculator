#CURAVED SURFACE AREA
his=open("history.txt","a")
#csa of cylinder
def cylinder():
    r=float(input("Enter radius of cylinder : "))
    h=float(input("Enter height of cylinder: "))
    f=2*3.14*r*h
    print("Curved surface area of cylinder : ",round(f,2))
#writing onto the file
    his.write("\nCurved surface area of Cylinder:-")
    his.write("\nRadius : "+str(r))
    his.write("\nHeight : "+str(h))
    his.write("Area of cylinder : "+str(round(f,2)))
    his.flush()
#csa of cone
def cone():
    r=float(input("Enter radius of cone : "))
    l=float(input("Enter slant height of cone : "))
    f=3.14*r*l
    print("Curved surface area of cone : ",round(f,2))
#writing onto the file
    his.write("\nCurved surface area of Cone:-")
    his.write("\nRadius : "+str(r))
    his.write("\nLength : "+str(l))
    his.write("\nArea of cone : "+str(round(f,2)))
    his.flush()
def hemisphere():
    r=float(input("Enter radius of hemisphere : "))
    f=2*3.14*r*r
    print("Curved surface area of hemisphere : ",round(f,2))
#writing onto the file
    his.write("\nCurved surface area of Hemisphere:-")
    his.write("\nRadius : "+str(r))
    his.write("\nArea of hemisphere : "+str(round(f,2)))
    his.flush()


