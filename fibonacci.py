#get the user input
#declare values for n1 and n2 vars and a flag
#condition less than 0 as error
#return n1 if values is 1

val = int(input("Number: "))

n1,n2 = 0,1
flag = 0

if val <= 0:
    print("Poda bundha")

elif val == 1:
    print(n2)

else:
    while val > flag:
        print(n1)
        nth = n1 + n2

        #update values
        n1 = n2
        n2 = nth
        flag = flag + 1
