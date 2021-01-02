def draw_traiangle(n):
    for i in range(n):
        for i in range (i+1):
            print("*", end="")
        print()
n = int(input("Enter a number"))
draw_traiangle(n)