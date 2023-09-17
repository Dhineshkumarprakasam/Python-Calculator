#CALCULATOR
import dmas
import tsa
import csa
import vol
#text for option
text="""
0.EXIT
1.CALCULATOR
2.TOTAL SURFACE AREA
3.CURVED SURFACE AREA
4.VOLUME
5.HISTORY
6.CLEAR HISTORY
"""
#text for DMAS
text1="""
0.EXIT
1.ADD
2.SUB
3.MULTIPLY
4.DIVIDE
"""
#text for TSA
text2="""
0.EXIT
1.CIRCLE
2.RECTANGLE
3.SQUARE
4.TRIANGLE
5.CUBE
6.CUBOID
7.SPHERE
8.CYLINDER
9.CONE
10.HEMISPHERE"""

#text for CSA
text3="""
0.EXIT
1.CYLINDER
2.CONE
3.HEMISPHERE
"""
#text for VOL
text4="""
0.EXIT
1.CUBE
2.CUBOID
3.CYLINDER
"""
while True:
    #choice1 to select option
    try:
        print(text)
        #select option
        choice1 =int(input("Enter your choice  {0/1/2/3/4/5/6} : "))
        
        if choice1==1:
            print(text1)
            choice2=int(input("Enter your choice {0/1/2/3/4} : "))
            if choice2==1:
                dmas.add()
            elif choice2==2:
                dmas.sub()
            elif choice2==3:
                dmas.mul()
            elif choice2==4:
                dmas.div()
            else:
                print("Out of range")
                continue
            
        elif choice1 ==2:
            #total surface area
            while True:
                try:
                    print(text2)#shapes
                    choice2=int(input("Enter your option {0/1/2/3/4/5/6/7/8/9/10} : "))
                    if choice2==1:
                        tsa.circle()
                    elif choice2==2:
                        tsa.rectangle()
                    elif choice2==3:
                        tsa.square()
                    elif choice2==4:
                        tsa.triangle()
                    elif choice2==5:
                        tsa.cube()
                    elif choice2==6:
                        tsa.cuboid()
                    elif choice2==7:
                        tsa.sphere()
                    elif choice2==8:
                        tsa.cylinder()
                    elif choice2==9:
                        tsa.cone()
                    elif choice2==10:
                        tsa.hemisphere()
                    elif choice2==0:
                        print("Exit")
                        break
                    else:
                        print("Out of range")
                        continue
                except ValueError:
                    print("Something went wrong")
                    continue
                
        elif choice1==3:
            #curved surface area
            while True:
                try:
                    print(text3)#shapes
                    choice2=int(input("Enter your option {0/1/2/3} : "))
                    if choice2==1:
                        csa.cylinder()
                    elif choice2==2:
                        csa.cone()
                    elif choice2==3:
                        csa.hemisphere()
                    elif choice2==0:
                        print("Exit")
                        break
                    else:
                        print("Out of range")
                        continue
                    
                except ValueError:
                    print("Something went wrong")
                    continue

        elif choice1==4:
            while True:
                try:
                    print(text4)
                    choice2=int(input("Ente your option {0/1/2/3/4/5/6} : "))
                    if choice2==1:
                        vol.cube()
                    elif choice2==2:
                        vol.cuboid()
                    elif choice2==3:
                        vol.cylinder()
                    elif choice2==0:
                        print("Exit")
                        break
                    else:
                        print("Out of range")
                        continue
                except ValueError:
                    print("Something went wrong")
                    continue
            
        elif choice1==5:
            his=open("history.txt","r")
            for a in his:
                print(a)
            his.close()
            
        elif choice1 ==6:
            his=open("history.txt","w")
            his.write("")
            his.close()
            print("Successfully cleared history")

        elif choice1 ==0:
            print("Exit")
            break
        
        else:
            print("Out of range")
            continue
    except ValueError:
        print("Something went wrong")
        continue
        
    

    

    

