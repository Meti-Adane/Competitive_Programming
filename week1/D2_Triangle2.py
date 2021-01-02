def drawTriangle(n):
    no_stars = 1
    for i in range(n, 0, -1):
        for j in range(i):
            print (" ", end="")
        for k in range(no_stars):
            print("*", end="")
        no_stars += 2
        print()

