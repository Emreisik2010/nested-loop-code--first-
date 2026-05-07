start=int(input("write a integer for a triangular start\t".expandtabs(10)))# "Enter a starting number for the triangle:"
finish=int(input("write a integer for a triangular finish\t".expandtabs(10)))#"Enter a finishing number for the triangle:"


for Vertical in range(start,finish + 1):# this for loop write vertical number in triangular

    for Horizontal in range(1,Vertical + 1):# this for loop write horizontal number in triangular
        print(f"{Horizontal}",end=" ")

    print()# this print the triangular