#This program filters even and odd numbers inside a given limit
#---------------------------

print("""\n♪ ♫ ♩ ♬ ♭ ♮ ♯""","Welcome to Even/Odd number Sorter","""♪ ♫ ♩ ♬ ♭ ♮ ♯""")

#asking the user whether he want to sort even or odd number
choice=int(input("\nTo sort even number press 1 and to sort odd number press 2:"))


#checking the choice of the user
if(choice==1):

    #asking the user for upper limit
    upper_limit=int(input("\nEnter an upper limit:"))
    print("\nThe even numbers smaller than ",upper_limit," is:")

    for i in range(1,upper_limit) :
        if(i%2==0):
            print(i)


elif(choice==2):

    #asking the user for upper limit
    upper_limit=int(input("\nEnter an upper limit:"))
    print("\nThe odd numbers smaller than ",upper_limit," is:")

    for i in range(1,upper_limit):
        if(i%2!=0):
            print(i)
else:
    print("\nInvalid Choice")


