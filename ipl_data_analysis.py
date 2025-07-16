print("\n\n\n\t\t\t\t\t\t\t\t\t>>>>  WELCOME  TO  MY  PROGRAM  <<<<\t\t\t\t\t\t")
while True:
    print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
    print("\nAll Choices of Assignment are as follows:")
    print("1.Open Assignment 1 ")
    print("2.Open Assignment 2 ")
    print("3.Open Assignment 3 ")
    print("4.Open Assignment 4 ")
    print("5.Open Assignment 5 ")
    print("6.Open Assignment 6 ")
    print("7.Open Assignment 7 ")
    print("8.Open Assignment 8 ")
    print("9.Exit")
    n=int(input("Enter choice (Which assignment you want to see) :"))
    if n==1:
    #ASSIGNMENT 1
        print( )
        print( )
        print("All operations are as follows:")
        print("1.Geanerate even no. upto n")
        print("2.Geanerate odd no. upto n")
        print("3.Geanerate prime no. upto n")
        print("4.Inputed number is a perfect square or not")
        print("5.Generate fibonacci series upto n")
        print("6.Generate tables of given number")
        print("7.Area of common figures")
        print("8.To check inputed string is palindrome or not")
        print("9.To find factorial of inputed number")
        print("10.To swap two variable without third variable")
        print("11.To generate electricity bill")
        print("12.To display the piramind of stars")
        print("13.To display the piramind of numbers ")
        print("14.Exit")
        while True:
            if n==1:
                choice=int(input("enter choice(1-14) :"))
            def even():
                a=int(input("enter number:"))
                i=2
                while i<=a:
                    print(i)
                    i+=2
            def odd():
                a=int(input("enter number:"))
                i=1
                while i<=a:
                    print(i)
                    i+=2
            def prime():
                upto = int(input("Find prime numbers upto : "))
                print("\nAll prime numbers upto", upto, "are : ")
                for num in range(2, upto + 1):
                    i=0
                    for i in range(2,num):
                        if(num % i == 0):
                            i = num
                            break;
        # If the number is prime then print it.
                    if(i != num):
                        print(num)
            def square():
                y=float(input("enter number"))
                if (y**(1/2))%1==0:
                    print(y,"is a perfect sqquare root")
                else:
                    print(y,"is not a perfect square root")
            def series():
                i=int(input("enter the terms"))
                a=0
                b=1
                if i<=0:
                    print("the finacci seris is",a)
                else:
                    print(a,b,end=" ")
                    c=2
                    while c>=2 and c<=i:
                        next=a+b
                        print(next,end=" ")
                        a=b
                        b=next
                        c+=1
                return
            def tables():
                n=float(input("enter number"))
                print("Table of ",n,"is")
                i=1
                while i<=10:
                    print(n,"x",i,"=",i*n)
                    i+=1
            def area():
                print("1.area of square")
                print("2.area of rectangle")
                print("3.area of traingle")
                print("4.area of circle")
                n=int(input("enter choice(1-4):"))
                if n==1:
                    a=float(input("enter length of square(cm):"))
                    print("Area of square is",a**2,"cm")
                elif n==2:
                    a=float(input("enter length of rectangle(cm):"))
                    b=float(input("enter breath of rectangle(cm):"))
                    print("Area of Rectangle is",a*b,"cm")
                elif n==3:
                    h=float(input("enter height of traingle(cm):"))
                    b=float(input("enter breath of traingle(cm):"))
                    print("area of traingle is",0.5*h*b,"cm")
                elif n==4:
                    pie=3.14
                    r=float(input("enter radius of circle(cm)"))
                    print("Area of circle is",pie*r**2,"cm")
                else:
                    print("choice is invalid")
            def palindrome():
                n=input("enter string")
                a=n[::-1]
                if n==a:
                    print("string is palindrome")
                else:
                    print("string is not palindrome")
            def factorial():
                n=int(input("enter number"))
                if n<0:
                    print("factorial of negative no. is not present")
                elif n==0:
                    print("factoril of 0 is 1")
                else:
                    factorial=1
                    for i in range(1,n+1):
                        factorial*=i
                    a=factorial
                    print("Factorial of",n,"is",a)
            def swap():
                a=input("enter value")
                b=input("enter value")
                a,b=b,a
                print("first value after swap",a)
                print("second value after swap",b)
            def bill():
                name=input("enter your name")
                unit=float(input("enter unit consumed"))
                metrecost=150
                if unit<=100 and unit>=0:
                    a=unit*7+metrecost
                    print("Name :",name)
                    print("unit consumed:",unit,"watt")
                    print("metrecost:",metrecost,"Rs")
                    print("final amount to pay is",a,"Rs")
                elif unit>100 and unit<=150:
                    a=100*7
                    b=(unit-100)*10
                    c=a+b+metrecost
                    print("Name :",name)
                    print("unit consumed:",unit,"watt")
                    print("metrecost:",metrecost,"Rs")
                    print("final amount to pay is after extra charges",c,"Rs")
                elif unit>150:
                    a=100*7
                    b=50*10
                    c=(unit-150)*20
                    d=a+b+c+metrecost
                    print("\t\tELECTRICITY BILL")
                    print("Name :",name)
                    print("unit consumed:",unit,"watt")
                    print("metrecost:",metrecost,"Rs")
                    print("final amount to pay is after extra charges",d,"Rs")
                else:
                    print("invalid unit")
            def stars():
                print("pyiramid of stars")
                n=int(input("enter rows of piramid"))
                for i in range(1,n+1):
                    for y in range(1,n-i+1):
                        print(end=" ")
                    for y in range(i,0,-1):
                        print("*",end="")
                    for y in range(2,i+1):
                        print("*",end="")
                    print()
            def numbers():
                print("Piramid of numbers(1,2,3,4)")
                n=int(input("enter rows of piramid"))
                for i in range(1,n+1):
                    for y in range(1,n-i+1):
                        print(end=" ")
                    for y in range(i,0,-1):
                        print(y,end="")
                    for y in range(2,i+1):
                        print(y,end="")
                    print()
            if choice==1:
                even()
            elif choice==2:
                odd()
            elif choice==3:
                prime()
            elif choice==4:
                square()
            elif choice==5:
                series()
            elif choice==6:
                tables()
            elif choice==7:
                area()
            elif choice==8:
                palindrome()
            elif choice==9:
                factorial()
            elif choice==10:
                swap()
            elif choice==11:
                bill()
            elif choice==12:
                stars()
            elif choice==13:
                numbers()
            elif choice==14:
                break
            else:
                print("ERROR:choice invalid")
        
             
    #ASSIGNMENT 2
            
                   
    elif n==2:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            #Question1(ASSI2)
            if a==1:
                list1=[22,42,31,11,1,6,1,1,6,42,42,22,22]
                print("list1 = ",list1)
                print("LIST OPERATIONS")
                print("1.to find length of list")
                print("2.to create list")
                print("3.to append element")
                print("4.to append list")
                print("5.to insert element")
                print("6.to count an element")
                print("7.to find index value")
                print("8.to remove an element")
                print("9.to pop out and remove and element")
                print("10.to reverse the order of list")
                print("11.to sort the list")
                print("12.to sort and make a another list")
                print("13.to find minimum value in list")
                print("14.to find maximum value in list")
                print("15.to find sum of elements of list")
                print("16.Exit")
                while True:
                    choice=int(input("Enter choice (1-16):"))
                    if choice==1:
                        a=len(list1)
                        print("length fo the list is",a)
                    elif choice==2:
                        print("1.to create empty list")
                        print("2. to create list from string")
                        m=int(input("enter Choice (1-2):"))
                        if m==1:
                            l1=list()
                            print(l1)
                        elif m==2:
                            a=input("enter string")
                            l1=list(a)
                            print(l1)
                        else:
                            print("choice is invalid")
                    elif choice==3:
                        n=int(input("enter element to append"))
                        list1.append(n)
                        print(list1)
                    elif choice==4:
                        l2=[]
                        n=int(input("enter no. of elements in list"))
                        print("enter elements")
                        for i in range(n):
                            b=int(input())
                            l2.append(b)
                        list1.extend(l2)
                        print(list1)
                    elif choice==5:
                        n=int(input("enter position"))
                        m=int(input("enter element"))
                        list1.insert(n,m)
                        print(list1)
                    elif choice==6:
                        n=int(input("enter no. to count"))
                        a=list1.count(n)
                        print(n,"appears",a,"times")
                        print(a)
                    elif choice==7:
                        n=int(input("enter element"))
                        a=list1.index(n)
                        print("index value of",n,"is",a)
                    elif choice==8:
                        n=int(input("enter element to remove"))
                        list1.remove(n)
                        print(n,"is removed")
                    elif choice==9:
                        n=int(input("enter position to pop out and remove"))
                        n-=1
                        if n<len(list1):
                            print(list1.pop(n))
                            print(list1)
                        else:
                            print("position doesnot exist")
                    elif choice==10:
                        list1.reverse()
                        print("reversed list:")
                        print(list1)
                    elif choice==11:
                        print("1. sort in ascending order")
                        print("2. sort in descending order")
                        n=int(input("enter choice(1-2):"))
                        if n==1:
                            list1.sort()
                            print(list1)
                        elif n==2:
                            list1.sort(reverse=True)
                            print(list1)
                        else:
                            print("invalid choice")
                    elif choice==12:
                        l2=sorted(list1)
                        print("sorted list=",l2)
                    elif choice==13:
                        print(min(list1))
                    elif choice==14:
                        print(max(list1))
                    elif choice==15:
                        print(sum(list1))
                    elif choice==16:
                        break
                    else:
                        print("inavlid choice")
                
            #Question2(ASSI2)
            elif a==2:
                    print("choices are as follows:")
                    print('1. create a list')
                    print('2. list from string')
                    print('3. traverse a list')
                    print('4. access a particular element')
                    print('5. compare two list')
                    print('6. replicate a list')
                    print("7.Exit")
                    while True:
                        list1=[1,2,3,4,5]
                        print("list1 is",list1)
                        choice=int(input("enter choice from 1-7:"))
                        if choice==1:
                            l1=[]
                            a=int(input("enter no. of elements in list"))
                            print("enter elements")
                            for i in range(a):
                                b=input()
                                l1.append(b)
                                print(l1)

                        elif choice==2:
                            n=input("enter string")
                            l2=[]
                            for i in n :
                                l2.append(i)
                            print(l2)
                        
                        elif choice==3:
                            for i in list1 :
                                print(i)

                        elif choice==4:
                            c=int(input("enter position of element"))
                            c-=1
                            if c<len(list1):
                                print('element is',list1[c])
                            else:
                                print("position doesnot exist")

                        elif  choice==5:
                            list2=[]
                            n=int(input("enter no. of elements"))
                            print("enter elements of list2 to compare")
                            for i in range(n):
                                a=int(input())
                                list2.append(a)
                            if list2>list1:
                                print("list2 is greater than list1")
                            elif list2<list1:
                                print('list2 is smaller than list1')
                            else :
                                print('list2 is equal to list1')
                        elif choice==6:
                            n=int(input("enter no. of times want to replicate list:"))
                            print(list1*n)
                        elif choice==7:
                            break
                        else:
                            print("your choice is invalid")
            elif a==3:
                break
            else:
                print("Invalid choice")
                           


    #ASSIGNMENT 3
    elif n==3:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            
            #Question1(ASSI3)

            if a==1:
                dict1={"Mohan":95,"Ram":89,"Suhel":92,"Sangeeta":85,"Ramesh":80}
                dict2={}
                print("my dictionary is :",dict1)
                print("\n All dictionary operations are:")
                print("1. find length of dictionary")
                print("2. return keys in dictionary")
                print("3. return values in dictionary")
                print("4. return key value pair in dictionary")
                print("5. find value from key")
                print("6. append another dictionary")
                print("7. clear all items in dictionary")
                print("8. delete item from dictionary ")
                print("9.Exit")
                while True:
                    print(end="\n")
                    choice=int(input("enter choice(1-9):"))
                    def length():
                        print("length of dictionary is:",len(dict1))
                    def key():
                        print(dict1
                              .keys())
                    def value():
                        print(dict1.values())
                    def item():
                        print(dict1.items())
                    def ge():
                        a=input("enter key:")
                        b=dict1.get(a)
                        print("value is",b)
                    def updatee():
                        b=int(input("enter no. of element in dictionary"))
                        for num in range(b):
                            s=input("enter key")
                            d=input("enter value")
                            dict2[s]=d
                        dict1.update(dict2)
                        print(dict1)
                    def clear1():
                        dict1.clear()
                        print(dict1)
                    def delete(dict1):
                        print("1. Delete item from key")
                        print("2. Delete dictionary from memory")
                        n=int(input("enter choice(1-2):"))
                        if n==1:
                            a=input("enter key")
                            if a in dict1:
                                del dict1[a]
                                print(dict1)
                            else:
                                print("key is not present")
                        elif n==2:
                            c=input("DO you want to delete whole dictionary(y/n):")
                            if c=="y":
                                del dict1
                            elif c=="n":
                                delete(dict1)
                            else:
                                print("invalid choice:")
                        else:
                            print("invalid choice")
                    
                    if choice==1:
                        length()
                    elif choice==2:
                        key()
                    elif choice==3:
                        value()
                    elif choice==4:
                        item()
                    elif choice==5:
                        ge()
                    elif choice==6:
                        updatee()
                    elif choice==7:
                        clear1()
                    elif choice==8:
                        delete(dict1)
                    elif choice==9:
                        break
                    else:
                        print("ERROR:Invalid Choice")
            #Question2(ASSI3)
                        
            elif a==2:
                dict1={'rahul':90,'mahesh':75,'pranav':95,'mintu':88}
                print("dict1= ",dict1)
                print("1.create a dictionary")
                print("2.access a key-value pair")
                print("3.traverse the dictionary")
                print("4.append a value")
                print("5.removeing item")
                print("6.search for element in dictionary")
                print("7.Exit")
                while True:
                    choice=int(input("enter choice(1-7):"))
                    if choice==1:
                        dict2={}
                        n=int(input("enter no. of elements in dictionary"))
                        for z in range(n):
                            key=input("enter key")
                            value=input("enter marks")
                            dict2[key]=value
                        print(dict2)
                    elif choice==2:
                        n=input("enter key")
                        if n in dict1:
                           print("key =",n,"\n","value=",dict1[n])
                        else:
                            print("key doesnot exists")
                    elif choice==3:
                        for key in dict1:
                            print(key,"\t",dict1[key])
                    elif choice==4:
                        key=input("enter key to append")
                        value=input("enter value to append")
                        if key in dict1:
                            print("key already present in dictionary")
                        else:
                            dict1[key]=value
                        print(dict1)
                    elif choice==5:
                        key=input("enter key to remove")
                        del dict1[key]
                        print(dict1)
                    elif choice==6:
                        n=input("enter name ")
                        for i in dict1:
                            if n==i:
                                print("marks of",n,"is",dict1[n])
                        if n not in dict1:
                            print("name is not present ")
                    elif choice==7:
                        break  
                    else:
                        print("invalid choice")
            #Exit
            elif a==3:
                break
            else:
                print("Invalid choice")


    #ASSIGNMENT 4
    elif n==4:
        while True:
            
            print( )
            print( )
            print("1.Open Assignment4 Part A")
            print("2.Open Assignment4 Part B")
            print("3.Exit")
            a=int(input("Enter choice(TO choice part) :"))
            #ASSIGNMENT 4 A
            if a==1:
                while True:
                    print( )
                    print( )
                    print("1.Open Question1")
                    print("2.Open Question2")
                    print("3.Open Question3")
                    print("4.Open Question4")
                    print("5.Exit")
                    print( )
                    print( )
                    a=int(input("Enter choice (Which Question want to select) :"))
                    #Question1(ASSI4A)
                    if a==1:
                        import numpy as np
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows\n")
                        print("1.To create a zero array")
                        print("2.To create a vowel array")
                        print("3.To create ones array")
                        print("4.To create myarray1")
                        print("5.To create myarray2")
                        print("6.Exit")
                        while True:
                            n=int(input("enter choice:"))
                            if n==1:
                                zeros=np.zeros(10,dtype=int)
                                print("Array of zeros :\n",zeros)
                            elif n==2:
                                vowles=np.array(["a","e","i","o","u"])
                                print("array of vowles :\n",vowles)
                            elif n==3:
                                ones=np.ones((2,5),dtype=int)
                                print("array of ones:\n",ones)
                            elif n==4:
                                myarray1=np.array([[2.7,-2,-19]
                                                   ,[0,3.4,99.9]
                                                   ,[10.6,0,13]])
                                print("myarray1 :\n",myarray1)
                            elif n==5:
                                myarray2=np.arange(4,61,4,dtype=float).reshape(3,5)
                                print("myarray2 :\n",myarray2)
                            elif n==6:
                                break
                            else:
                                print("INVALID CHOICE")

                    #Question2(ASSI4A)
                    elif a==2:
                        import numpy as np 
                        zeros=np.zeros(10,dtype=int)
                        print("Array of zeros :\n",zeros)
                        vowels=np.array(["a","e","i","o","u"])
                        print("Array of vowels :\n",vowels)
                        ones=np.ones((2,5),dtype=int)
                        print("array of ones:\n",ones)
                        myarray1=np.array([[2.7,-2,-19],[0,3.4,99.9],[10.6,0,13]])
                        print("myarray1 :\n",myarray1)
                        myarray2=np.arange(4,61,4,dtype=float).reshape(3,5)
                        print("myarray2 :\n",myarray2)
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows\n")
                        print("1.To find the dimensions, shape, size, and data type of the items and itemsize of arrays ")
                        print("2.Reshape the array ones to have all the 10 elements in a single row")
                        print("3.Display the 2nd and 3rd element of the array vowels")
                        print("4. Display all elements in the 2nd and 3rd row of the array myarray1")
                        print("5. Display the elements in the 1st and 2nd column of the array myarray1")
                        print("6. Display the elements in the 1st column of the 2nd and 3rd row of the array myarray1")
                        print("7.Reverse the array of vowels")
                        print("8.Exit")
                        while True:
                            n=int(input("Enter choice :"))
                            if n==1:
                                print("\nALL choices are as follows\n")
                                print("1.1.Of zeros")
                                print("1.2.Of vowels")
                                print("1.3.Of Ones")
                                print("1.4.Of myarray1")
                                print("1.5.Of myarray2")
                                print("1.6.Exit")
                                while True:
                                    n=float(input('enter choice :'))
                                    if n==1.1:
                                        print("Dimension is : ",zeros.ndim)
                                        print("Shape is : ",zeros.shape)
                                        print("Size is : ",zeros.size)
                                        print("Datatype is : ",zeros.dtype)
                                        print("Itemsize is : ",zeros.itemsize)
                                    elif n==1.2:
                                        print("Dimension is : ",vowels.ndim)
                                        print("Shape is : ",vowels.shape)
                                        print("Size is : ",vowels.size)
                                        print("Datatype is: : ",vowels.dtype)
                                        print("Itemsize is : ",vowels.itemsize)
                                    elif n==1.3:
                                        print("Dimension is : ",ones.ndim)
                                        print("Shape is : ",ones.shape)
                                        print("Size is : ",ones.size)
                                        print("Datatype is: : ",ones.dtype)
                                        print("Itemsize is : ",ones.itemsize)
                                    elif n==1.4:
                                        print("Dimension is : ",myarray1.ndim)
                                        print("Shape is : ",myarray1.shape)
                                        print("Size is : ",myarray1.size)
                                        print("Datatype is: : ",myarray1.dtype)
                                        print("Itemsize is : ",myarray1.itemsize)
                                    elif n==1.5:
                                        print("Dimension is : ",myarray2.ndim)
                                        print("Shape is : ",myarray2.shape)
                                        print("Size is : ",myarray2.size)
                                        print("Datatype is: : ",myarray2.dtype)
                                        print("Itemsize is : ",myarray2.itemsize)
                                    elif n==1.6:
                                        break
                                    else:
                                        print("INVALID CHOICE")
                            elif n==2:
                                ones=ones.reshape(10)
                                print("array ones :\n",ones)
                            elif n==3:
                                print("2nd and 3rd element of vowels array : \n",vowels[1:3])
                            elif n==4:
                                print("2nd and 3rd row of the array myarray1 : \n",myarray1[1:3])
                            elif n==5:
                                print("1st and 2nd column of the array myarray1 : \n",myarray1[:,0:2])
                            elif n==6:
                                print("1st column of the 2nd and 3rd row of myarray1 : \n",myarray1[1:3,0])
                            elif n==7:
                                print("reverse the array vowles : ",vowels[::-1])
                            elif n==8:
                                break
                            else:
                                print("INVALID CHOICE")

                    #Question3(ASSI4A)
                    elif a==3:
                        import numpy as np
                        zeros=np.zeros(10,dtype=int)
                        print("Array of zeros :\n",zeros)
                        vowels=np.array(["a","e","i","o","u"])
                        print("Array of vowels :\n",vowels)
                        ones=np.ones((2,5),dtype=int)
                        print("array of ones:\n",ones)
                        myarray1=np.array([[2.7,-2,-19],[0,3.4,99.9],[10.6,0,13]])
                        print("myarray1 :\n",myarray1)
                        myarray2=np.arange(4,37,4,dtype=float).reshape(3,3)
                        print("myarray2 :\n",myarray2)
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows\n")
                        print("1.Divide all elements of array ones by 3")
                        print("2.Add the arrays myarray1 and myarray2")
                        print("3.Substract myarray1 from myarray2 and store the result in a new array")
                        print("4.Multiply myarray1 and myarray2 elementwise")
                        print("5. matrix multiplication of myarray1 and myarray2 ")
                        print("6.Divide myarray1 by myarray2")
                        print("7.Find the cube of all elements of myarray1 and divide the result by 2")
                        print("8.Find the square root of all elements of myarray2 and divide the resultby 2")
                        print("9.Exit")
                        while True:
                            n=int(input("Enter choice :"))
                            if n==1:
                                print("array ones after dividing :\n",ones/3)
                            elif n==2:
                                print("arrays after adding : \n",myarray1+myarray2)
                            elif n==3:
                                print("arrays after substracting : \n",myarray2-myarray1)
                            elif n==4:
                                print("arrays after multiplying : \n",myarray1*myarray2)
                            elif n==5:
                                myarray3=myarray1 @ myarray2
                                print("myarray3 is :\n",myarray3)
                            elif n==6:
                                print("arrays after dividing : \n",myarray1/myarray2)
                            elif n==7:
                                print("myarray1 after finding cube and dividing by 2 :\n",(myarray1**3)/2)
                            elif n==8:
                                myarray4=(myarray2**0.5)/2
                                print("myarray2 after finding square root and dividing by 2 :\n",np.round(myarray4,decimals=2))
                            elif n==9:
                                break
                            else:
                                print("INVALID CHOICE")        

                    #Question4(ASSI4A)
                    elif a==4:
                        import numpy as np
                        zeros=np.zeros(10,dtype=int)
                        print("Array of zeros :\n",zeros)
                        vowels=np.array(["a","e","i","o","u"])
                        print("Array of vowels :\n",vowels)
                        ones=np.ones((2,5),dtype=int)
                        print("array of ones:\n",ones)
                        myarray1=np.array([[2.7,-2,-19],[0,3.4,99.9],[10.6,0,13]])
                        print("myarray1 :\n",myarray1)
                        myarray2=np.arange(4,61,4,dtype=float).reshape(3,5)
                        print("myarray2 :\n",myarray2)
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows:")
                        print("1.Find the transpose of ones and myarray2")
                        print("2.Sort the array vowels in reverse")
                        print("3.Sort the array myarray1 column wise")
                        print("4.Exit")
                        while True:
                            n=int(input("enter choice :"))
                            if n==1:
                                print("transpose of array ones : \n",ones.transpose())
                                print("transpose of array myarray2 : \n",myarray2.transpose())
                            elif n==2:
                                print("array vowels after sorting in reverse order :\n",vowels[::-1])
                            elif n==3:
                                print( )
                                a=np.sort(myarray1,axis=0)
                                print("myarray1 after sorting(column wise): \n",a)
                            elif n==4:
                                break
                            else:
                                print("INVALID CHOICE")

                    #Exit
                    elif a==5:
                        break
                    else:
                        print("Invalid Choice")

            #ASSIGNMENT 4 B
            elif a==2:
                while True:
                    print( )
                    print( )
                    print("1.Open Question1")
                    print("2.Open Question2")
                    print("3.Open Question3")
                    print("4.Exit")
                    print( )
                    print( )
                    a=int(input("Enter choice (Which Question want to select) :"))
                    #Question1(ASSI4B)
                    if a==1:
                        import numpy as np
                        zeros=np.zeros(10,dtype=int)
                        print("Array of zeros :\n",zeros)
                        vowels=np.array(["a","e","i","o","u"])
                        print("Array of vowels :\n",vowels)
                        ones=np.ones((2,5),dtype=int)
                        print("array of ones:\n",ones)
                        myarray1=np.array([[2.7,-2,-19],[0,3.4,99.9],[10.6,0,13]])
                        print("myarray1 :\n",myarray1)
                        myarray2=np.arange(4,61,4,dtype=float).reshape(3,5)
                        print("myarray2 :\n",myarray2)
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows:")
                        print("1.To split myarray2 in 5 parts columnwise")
                        print("2.Split the array zeros at array index 2, 5, 7, 8")
                        print("3.Concatenate the arrays myarray2A, myarray2B and myarray2C ")
                        print("4.Exit")
                        myarray2A, myarray2B, myarray2C, myarray2D, myarray2E=np.split(myarray2,[1,2,3,4],axis=1)
                        while True:
                            n=int(input("enter choice :"))
                            if n==1:
                                print("myarray2A : \n",myarray2A)
                                print("myarray2B : \n",myarray2B)
                                print("myarray2C : \n",myarray2C)
                                print("myarray2D : \n",myarray2D)
                                print("myarray2E : \n",myarray2E)
                            elif n==2:
                                zero1 = np.split(zeros,[2,5,7,8])
                                zerosA = zero1[0]
                                zerosB = zero1[1]
                                zerosC = zero1[2]
                                zerosD = zero1[3]
                                print("zerosA : \n",zerosA)
                                print("zerosB : \n",zerosB)
                                print("zerosC : \n",zerosC)
                                print("zerosD : \n",zerosD)
                            elif n==3:
                                array1=np.concatenate((myarray2A, myarray2B, myarray2C),axis=1)
                                print("Array after concatination :\n",array1)
                            elif n==4:
                                break
                            else:
                                print("INVALID CHOICE")


                    #Question2(ASSI4B)
                    elif a==2:
                        import numpy as np
                        myarray4=np.arange(-1,9.5,0.25)
                        myarray4=myarray4.reshape(14,3)
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("\nALL choices are as follows")
                        print("1.Display myarray4")
                        print("2.Split myarray4 in 3 equal parts and display")
                        print("3.Exit")
                        while True:
                            n=int(input("Enter choice"))
                            if n==1:
                                print("myarray4 :\n",myarray4,"\n")
                        #splitting array
                            elif n==2:         #To split in three equal parts we reshape array to (21,2)
                                myarray4=myarray4.reshape(21,2)
                                firstpart , secondpart, thirdpart =np.split(myarray4,3,axis=0)
                                print("firstpart :\n",firstpart,"\n")
                                print("secondpart :\n",secondpart,"\n")
                                print("thirdpart :\n",thirdpart,"\n")
                            elif n==3:
                                break
                            else:
                                print("INVALID CHOICE")


                    #Question3(ASSI4B)
                    elif a==3:
                        import numpy as np
                        myarray4=np.arange(-1,9.5,0.25)
                        myarray4=myarray4.reshape(14,3)
                        print("myarray4 :\n",myarray4,"\n")
                        print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                        print("ALL choices are as follows :")
                        print("1.Find the sum of all elements")
                        print("2.Find the sum of all elements row wise")
                        print("3.Find the sum of all elements column wise")
                        print("4.Find the max of all elements")
                        print("5.Find the min of all elements in each row")
                        print("6.Find the mean of all elements in each row")
                        print("7.Find the standard deviation column wise")
                        print("8.Exit")
                        while True:
                            n=int(input("Enter choice :"))
                            if n==1:
                                print("sum of all elements : ",myarray4.sum())
                            elif n==2:
                                print("sum of all elements(row wise) : \n",myarray4.sum(axis=1))
                            elif n==3:
                                print("sum of all elements(column wise) :\n",myarray4.sum(axis=0))
                            elif n==4:
                                print("max of all elements : \n",myarray4.max())
                            elif n==5:
                                print("min of all elements(row wise) :\n ",myarray4.min(axis=1))
                            elif n==6:
                                print("mean of all elements(row wise) : \n",myarray4.mean(axis=1))
                            elif n==7:
                                print("standard deviation of all elements(column wise) :\n ",myarray4.std(axis=0))
                            elif n==8:
                                break
                            else:
                                print("INVALID CHOICE")
                        

                    #Exit
                    elif a==4:
                        break
                    else:
                        print("Invalid Choice")

            #Exit
            elif a==3:
                break
            else:
                print("Invalid Choice")
            


    #ASSIGNMENT 5
    elif n==5:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Open Question3")
            print("4.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            #question1(ASSI5)
            if a==1:
                import pandas as pd
                import numpy as np
                EngAlph = pd.Series(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
                print("series of EngAlph is:\n",EngAlph)
                Vowels = pd.Series(0,index=["a","e","i","o","u"])
                print("series of Vowels is:\n",Vowels)
                dict1={"Manan":23,"Suresh":15,"Akshet":43,"Rahul":52,"Arayan":11}
                Friends= pd.Series(dict1)
                print("series of Friends is:\n",Friends)
                MTseries= pd.Series(dtype = float)
                array1= np.array([31,28,31,30,31,30,31,31,30,31,30,31])
                MonthDays = pd.Series(array1,index= np.arange(1,13))
                print("series of MonthDays is:\n",MonthDays)
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1. set all values of Vowels to 10")
                print("2.Divide all values of Vowels by 2")
                print("3.To create another series Vowels1")
                print("4.To add Vowels and Vowels1 and assign to Vowels3")
                print("5.Substract,Multiply and Divide Vowels by Vowels1")
                print("6.Alter the lables of vowels1 to [A,E,I,O,U]")
                print("7.Exit")
                while True:
                    Vowels = pd.Series(0,index=["a","e","i","o","u"])
                    Vowels1 = pd.Series([2,5,6,3,8],index=["a","e","i","o","u"])      #Series of vowels1 
                    n=int(input("Enter the choice :"))
                    if n==1:
                        Vowels["a":"u"]=10
                        print("Series of Vowels is :\n" , Vowels)
                    elif n==2:
                        Vowels["a":"u"]=10
                        Vowels = Vowels/2
                        print("Series of Vowels is :\n" , Vowels)
                    elif n==3:
                        print("Series of Vowels1 is: \n",Vowels1)
                    elif n==4:
                        Vowels["a":"u"]=10
                        Vowels3 = Vowels.add(Vowels1, fill_value=0)
                        print("Series of Vowels3 is :\n" , Vowels3)
                    elif n==5:
                        print("5.1.substract vowels by vowels1")
                        print("5.2.multiply vowels by vowels1")
                        print("5.3.divide vowels by vowels1")
                        print("5.4.Exit")
                        while True:
                            b=float(input("enter choice"))
                            if b==5.1:
                                Vowels["a":"u"]=10
                                Vowels = Vowels/2
                                print("Series after substracting Vowels by Vowels1 is:\n",Vowels.sub(Vowels1, fill_value=0))
                            elif b==5.2:
                                Vowels["a":"u"]=10
                                Vowels = Vowels/2
                                print("Series after multiplying Vowels by Vowels1 is:\n",Vowels.mul(Vowels1, fill_value=0))
                            elif b==5.3:
                                Vowels["a":"u"]=10
                                Vowels = Vowels/2
                                print("Series after dividing Vowels by Vowels1 is:\n",Vowels.div(Vowels1, fill_value=0))
                            elif b==5.4:
                                break
                            else:
                                print("Invalid Choice")
                    elif n==6:
                        Vowels1.index=["A","E","I","O","U"]
                        print("Series of Vowels1 is: \n",Vowels1)
                    elif n==7:
                        break
                    else:
                        print("INVALID CHOICE")
                


            #question2(ASSI5)
            elif a==2:
                import pandas as pd
                import numpy as np
                print("\nALL series :\n")
                EngAlph = pd.Series(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
                print("series of EngAlph is:\n",EngAlph)
                Vowels = pd.Series(0,index=["a","e","i","o","u"])
                print("series of Vowels is:\n",Vowels)
                dict1={"Manan":23,"Suresh":15,"Akshet":43,"Rahul":52,"Arayan":11}
                Friends= pd.Series(dict1)
                print("series of Friends is:\n",Friends)
                MTseries= pd.Series(dtype = float)
                array1= np.array([31,28,31,30,31,30,31,31,30,31,30,31])
                MonthDays = pd.Series(array1,index= np.arange(1,13))
                print("series of MonthDays is:\n",MonthDays)
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1.To find dimensions,size and values of series")
                print("2.rename the series MTseries to seriesempty")
                print("3.To name the index of series Monthdays and Friends")
                print("4.To show 3rd and 2nd value of series friends")
                print("5.display the alphabates from e to p")
                print("6.Display the first 10 value of engAlph series")
                print("7.Display the last 10 value of engAlph series")
                print("8.Display MTseries")
                print("9.Exit")
                while True:
                    n=int(input("Enter choice :"))
                    if n==1:
                        print("To show dimensions,sizeand values of series")
                        print("1.1.  of EngAlph")
                        print("1.2.  of Vowels")
                        print("1.3.  of Friends")
                        print("1.4.  of MTseries")
                        print("1.5.  of MonthDays")
                        print("1.6.Exit")
                        while True:
                            choice=float(input("enter choice:"))
                            if choice==1.1:
                                print("Dimensions is :",EngAlph.ndim)
                                print("Size is :",EngAlph.size)
                                print("Values is :\n",EngAlph.values)
                            elif choice==1.2:
                                print("Dimensions is :",Vowels.ndim)
                                print("Size is :",Vowels.size)
                                print("Values is :\n",Vowels.values)
                            elif choice==1.3:
                                print("Dimensions is :\n",Friends.ndim)
                                print("Size is :",Friends.size)
                                print("Values is :\n",Friends.values)
                            elif choice==1.4:
                                print("Dimensions is :\n",MTseries.ndim)
                                print("Size is :",MTseries.size)
                                print("Values is :\n",MTseries.values)
                            elif choice==1.5:
                                print("Dimensions is :\n",MonthDays.ndim)
                                print("Size is :",MonthDays.size)
                                print("Values is :\n",MonthDays.values)
                            elif choice==1.6:
                                break
                            else:
                                print("INVALID CHOICE")
                    elif n==2:
                        MTseries.name = "Seriesempty"
                        print("series of MTseries is:\n",MTseries)
                    elif n==3:
                        MonthDays.index.name= "monthno"
                        Friends.index.name= "Fname"
                        print("Index name of Monthdays is set to monthno.")
                        print("Index name of Friends is set to Fname")
                    elif n==4:
                        print(Friends[2:0:-1])
                    elif n==5:
                        print("Alphabates from series EngAlph :\n",EngAlph[4:15])
                    elif n==6:
                        print("first 10 values are :\n",EngAlph.head(10))
                    elif n==7:
                        print("Last 10 values",EngAlph.tail(10))
                    elif n==8:
                        print("MTseries is:\n",MTseries)
                    elif n==9:
                        print("Program closed")
                        break
                    else:
                        print("INVALID CHOICE")


            #question3(ASSI5)
            elif a==3:
                import pandas as pd
                import numpy as np
                print("\nALL series :\n")
                array1= np.array([31,28,31,30,31,30,31,31,30,31,30,31])
                MonthDays = pd.Series(array1,index= np.arange(1,13))
                print("series of MonthDays is:\n",MonthDays)
                MonthDays.index=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1.Display the names of the months 3 through 7")
                print("2.Display series of month in reverse order")
                print("3.Exit")
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        print(MonthDays["March":"July"])
                    elif n==2:
                        print("Series MonthDays in reverse order :\n",MonthDays[::-1])
                    elif n==3:
                        print("Program closed")
                        break
                    else:
                        print("INVALID CHOICE")

            #Exit
            elif a==4:
                break
            else:
                print("Invalid Choice")

    #ASSIGNMENT 6
    elif n==6:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Open Question3")
            print("4.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            #question1(ASSI6)
            if a==1:
                import pandas as pd
                print("\n\n\n\t\t\t\t\t\t\t\t\t>>>>  WELCOME  TO  MY  PROGRAM  <<<<\t\t\t\t\t\t")
                #creating datafrae name sales(dictionary of series)
                data={"2014":[100.5,150.8,200.9,30000,40000],"2015":[12000,18000,22000,30000,45000],"2016":[20000,50000,70000,100000,125000],"2017":[50000,60000,70000,80000,90000]}
                Sales= pd.DataFrame(data,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL Choices are as follows")
                print("1.To display DataFrame Sales")
                print("2.Exit")
                while True:
                    n=int(input("Enter choice"))
                    if n==1:
                        print("DataFrame of sales is : \n",Sales)
                    elif n==2:
                        print("Program closed")
                        break
                    else:
                        print("INVALID CHOICE")


            #question2(ASSI6)
            elif a==2:
                import pandas as pd
                data={"2014":[100.5,150.8,200.9,30000,40000],"2015":[12000,18000,22000,30000,45000],"2016":[20000,50000,70000,100000,125000],"2017":[50000,60000,70000,80000,90000]}
                Sales= pd.DataFrame(data,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                print("DataFrame of sales is : \n",Sales)
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\n ALL choices are as follows:")
                print("1.Display the row labels of Sales")
                print("2.Display the column labels of Sales")
                print("3.Display the data types of each column of Sales")
                print("4.Display the dimensions, shape, size and values of Sales")
                print("5.Display the last two rows of Sales")
                print("6.Display the first two columns of Sales")
                print("7.Create a dataframe sales2 from dictionary")
                print("8.Check if sales2 is empty or not")
                print("9.Exit")
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        print("Row lables :\n",Sales.index)
                    elif n==2:
                        print("Column lables:\n",Sales.columns)
                    elif n==3:
                        print("Data types of columns:\n",Sales.dtypes)
                    elif n==4:
                        print("Dimensions of Sales is:\n",Sales.ndim)
                        print("Shape of Sales is:\n",Sales.shape)
                        print("Size of Sales is:\n",Sales.size)
                        print("Values of Sales is:\n",Sales.values)
                    elif n==5:
                        print("Last two rows of sales are:\n",Sales.tail(2))
                    elif n==6:
                        print("First two columns of sales are:\n",Sales.loc[:,"2014":"2015"])
                    elif n==7:
                        dict1={"2018":[160000,110000,500000,340000,900000]}
                        Sales2=pd.DataFrame(dict1,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                        print("Dataframe of sales2 :\n",Sales2)
                    elif n==8:
                        c=Sales2.empty
                        if c == True:
                            print("Sales2 is empty")
                        else:
                            print("sales2 to is not empty")
                    elif n==9:
                        print("Program closed")
                        break
                    else:
                        print("INVALID CHOICE")
    


            #question3(ASSI6)
            elif a==3:
                import pandas as pd
                data={"2014":[100.5,150.8,200.9,30000,40000],"2015":[12000,18000,22000,30000,45000],"2016":[20000,50000,70000,100000,125000],"2017":[50000,60000,70000,80000,90000]}
                Sales= pd.DataFrame(data,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                print("DataFrame of sales : \n",Sales,"\n\n")
                dict1={"2018":[160000,110000,500000,340000,900000]}
                Sales2=pd.DataFrame(dict1,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                print("DataFrame of sales2 :\n",Sales2)
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choice are as follows:")
                print("1.Append the DataFrame Sales2 to the Sales")
                print("2.Transpose of DataFrame Sales")
                print("3.Sales made by all sales persons in the year 2017")
                print("4.Sales made by Madhu and Ankit in the year 2017 and 2018")
                print("5.Sales made by Shruti in 2016")
                print("6.Add data to Sales for salesman Sumeet ")
                print("7.Delete the data for the year 2014 from the Sales")
                print("8.Delete the data for salesman Kinshuk from the DataFrame Sales")
                print("9.Change the name of the salesperson ")
                print("10.Update the sale made by Shailesh in 2018 to 100000")
                print("11.The values of DataFrame Sales to a CSV file SalesFigures.csv on the disk")
                print("12.Read the data in the file SalesFigures.csv into a DataFrame SalesRetrieved")
                print("13.Exit")
                while True:
                    data={"2014":[100.5,150.8,200.9,30000,40000],"2015":[12000,18000,22000,30000,45000],"2016":[20000,50000,70000,100000,125000],"2017":[50000,60000,70000,80000,90000]}
                    Sales= pd.DataFrame(data,index=["Madhu","Kusum","Kinshuk","Ankit","Shruti"])
                    Sales=(Sales.T.append(Sales2.T)).T
                    n=int(input("Enter choice:"))
                    if n==1:
                        print(Sales)
                    elif n==2:
                        print("Transpose of Datafarme Sales :\n",Sales.T)
                    elif n==3:
                        print("Sales in year 2017 :\n",Sales[["2017"]])
                    elif n==4:
                        print("Sales by Madhu and ankit in year 2017 and 2018 :\n",Sales.loc[["Madhu","Ankit"],["2017","2018"]])
                    elif n==5:
                        print("The sales made by Shruti in 2016:\n",Sales.loc[["Shruti"],["2016"]])
                    elif n==6:
                        Sales.loc["Sumeet"]=[196.2,37800,52000,78438,38852]
                        print("Sales after adding Sumeet  :\n",Sales)
                    elif n==7:
                        Sales=Sales.drop("2014",axis=1)
                        print("sales after deleting 2014 :\n",Sales)
                    elif n==8:
                        Sales=Sales.drop("Kinshuk",axis=0)
                        print("sales after deleting Kinshuk :\n",Sales)
                    elif n==9:
                        Sales=Sales.rename({"Ankit":"Vivaan","Madhu":"Shailesh"})
                        print("Sales after renaming :\n",Sales)
                    elif n==10:
                        Sales=Sales.rename({"Ankit":"Vivaan","Madhu":"Shailesh"})
                        Sales["2018"]["Shailesh"] = 100000
                        print(Sales)
                    elif n==11:
                        Sales.to_csv(path_or_buf='C:/PYTHON CSV/SalesFigures.csv',sep=',',header=False,index=False)
                        print("file is saved to C:/PYTHON CSV as SalesFigures.csv")
                    elif n==12:
                        SalesRetrieved=pd.read_csv('C:/PYTHON CSV/SalesFigures.csv',sep=',',names=['2014',  '2015',  '2016',  '2017','2018'])
                        print(SalesRetrieved,'\n')
                        SalesRetrieved.index=['Madhu','Kusum','Kinshuk','Ankit','Shruti']
                        print("SalesRetrieved after updating:\n",SalesRetrieved)
                    elif n==13:
                        print("Program closed")
                        break
                    else:
                        print("INVALID CHOICE")
    
                

            #Exit
            elif a==4:
                break
            else:
                print("Invalid Choice")

    #ASSIGNMENT 7
    elif n==7:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Open Question3")
            print("4.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            #question1(ASSI7)
            if a==1:
                import matplotlib.pyplot as plt
                import pandas as pd
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows:")
                print("1.NO. of courses in Delhi University")
                print("2.Exit")
                a=pd.Series([33,11,35],index=["Science","Commerce","Humanities"])
                while True:
                    n=int(input("Enter Choice:"))
                    if n==1:
                        a.plot(kind="barh",edgecolor=["orange","green","yellow"],fill=False,hatch=".",linewidth=2)
                        plt.xlabel("No. of courses")
                        plt.ylabel("Stream")
                        plt.title("No. of cousers in Delhi University")
                        plt.show()
                    elif n==2:
                        break
                    else:
                        print("INVALID CHOICE")
    


            #question2(ASSI7)
            elif a==2:
                import matplotlib.pyplot as plt
                import pandas as pd
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1.Plotting Graph of Students Screen Time")
                print("2.Exit")
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        df=pd.read_csv('C:/PYTHON CSV/Assign7 question12.csv')
                        df.plot(kind='bar',x="Name",legend=False,edgecolor='brown',fill=False,hatch='.')
                        plt.xlabel("Student Names")
                        plt.ylabel("Time in minutes")
                        plt.title("Screen time of Students")
                        plt.show()
                    elif n==2:
                        break
                    else:
                        print("INVALID CHOICE")


            #question3(ASSI7)
            elif a==3:
                import matplotlib.pyplot as plt
                import pandas as pd
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\n ALL choices are as follows:")
                print("1.Plotting Garph of minimum and maximum Temperature")
                print("2.Exit")
                data ={"Minimum Temperature" :[9,9,9, 9, 10, 10, 10, 10, 10, 9, 9, 10, 10, 11, 10, 10, 10, 12, 12, 12, 13, 13, 13, 14, 13, 14, 13, 14],
                      "Maximum Temperature": [23,23,23,24,24,25,24,23,23,24,23,24,32,26,25, 25, 25, 30, 26, 27, 28, 28,28,27,27,27,28,28]}
                df=pd.DataFrame(data)
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        df.plot(kind="hist",edgecolor="black",color=["red","blue"],linewidth=3)
                        plt.title("Maximum and Minimum Temprature")
                        plt.ylabel("No. of times")
                        plt.xlabel("Temperature")
                        plt.show()
                    elif n==2:
                        break
                    else:
                        print("INVALID CHOICE")
                

            #Exit
            elif a==4:
                break
            else:
                print("Invalid Choice")

    #ASSIGNMENT 8
    elif n==8:
        while True:
            print( )
            print( )
            print("1.Open Question1")
            print("2.Open Question2")
            print("3.Exit")
            print( )
            print( )
            a=int(input("Enter choice (Which Question want to select) :"))
            #question1(ASSI8)
            if a==1:
                import matplotlib.pyplot as plt
                import pandas as pd
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1.Ploting Graph of Students and Percentage(bar)")
                print("2.Ploting Graph of Students and Percentage(line)")
                print("3.Exit")
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        df=pd.read_csv('C:/PYTHON CSV/Assign8 question15.csv')
                        df.plot(kind="bar",legend=False,x="Students",edgecolor="black",color="cyan")
                        plt.ylabel("Percentage")
                        plt.title("Students Percantage")
                        plt.show()
                    elif n==2:
                        df=pd.read_csv('C:/PYTHON CSV/Assign8 question15.csv')
                        df.plot(marker='*',legend=False,x="Students",color="yellow")
                        plt.ylabel("Percentage")
                        plt.title("Students Percantage")
                        plt.show()
                    elif n==3:
                        break
                        
                    else:
                        print("INVALID CHOICE")



            #question2(ASSI8)
            elif a==2:
                import matplotlib.pyplot as plt
                import pandas as pd
                print("\n\n\t\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:MENU:-:-:-:-:-:-:-:-\t\t\t\t\t\t\n")
                print("\nALL choices are as follows")
                print("1.Ploting graph of Literacy rate and Population")
                print("2.Ploting graph of Average Literacy Rate for each region")
                print("3.Exit")
                while True:
                    n=int(input("Enter choice:"))
                    if n==1:
                        df=pd.read_csv('C:/PYTHON CSV/Assign8 question16.csv')
                        df.plot(marker="D",x="Population",color="brown",linewidth=3,linestyle="--")
                        plt.ylabel("Literacy rate")
                        plt.title("Literacy rate and Population")
                        plt.show()
                    elif n==2:
                        df=pd.read_csv('C:/PYTHON CSV/Assign8 question16.2.csv',index_col=0)
                        df.plot(kind='bar',color="red",edgecolor="black",linewidth=3,linestyle="--")
                        plt.ylabel("Literacy rate")
                        plt.xlabel("Region")
                        plt.title("Average Literacy Rate for each region")
                        plt.show()
                    elif n==3:
                        break
                    else:
                        print("INVALID CHOICE:")


            #Exit
            elif a==3:
                break
            else:
                print("Invalid Choice")
    elif n==9:
        break
    else:
        print("Invalid Choice")
        
        
        
                            
                              


                                        
                                        

                    

                    
               

                            

                             
                             

