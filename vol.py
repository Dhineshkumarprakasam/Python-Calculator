#VOLUME[vol]
#file history for saving history
his=open("history.txt","a")

#Volume of cuboid
def cuboid():
    l=float(input("Enter lenght of cuboid : "))
    b=float(input("Enter breadth of cuboid : "))
    h=float(input("Enter height of cuboid : "))
    f=l*b*h
    print("Volume of cuboid : ",round(f,2))
#writing onto the file
    his.write("\nVolume of Cuboid:-")
    his.write("\nLenght : "+str(l))
    his.write("\nBreadth : "+str(b))
    his.write("\nHeight : "+str(h))
    his.write("\nVolume : "+str(round(f,2)))
    his.flush()
#Volume of cube
def cube():
    a=float(input("Enter side of cube : "))
    f=a*a*a
    print("Volume of cube : ",round(f,2))
#writing onto the file
    his.write("\nVolume of Cube:-")
    his.write("\nSide : "+str(a))
    his.write("\nVolume : "+str(round(f,2)))
    his.flush()

#Volume of cylinder
def cylinder():
    r=float(input("Enter radius of cylinder : "))
    h=float(input("Enter height of cylinder : "))
    f=3.14*r*r*h
    print("Volume of cylinder : ",round(f,2))
#writing onto the file
    his.write("\nVolume of Cylinder:-")
    his.write("\nRadius : "+str(r))
    his.write("\nHeight : "+str(h))
    his.write("\nVolume : "+str(round(f,2)))
    his.flush()
