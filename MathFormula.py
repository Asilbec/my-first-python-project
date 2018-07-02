import math
choiceA = "| Pythagorean theorem | Square Area of a shape | Volume |"
print(choiceA)
choice = input("Which would you like to solve for?  ")
if choice == "math" or choice == "Pythagorean theorem   ":
    choiceOfChoice = (input("Which side would you like to solve for?    "))
    if choiceOfChoice == "A " or choiceOfChoice == "a " or choiceOfChoice == "c":
        choiceBA = float(input("What number is B?  "))
        choiceCA = float(input("What number is C?  "))
        answerA = float(choiceCA**2 - choiceBA**2)
        import math
        realAnswerA = math.sqrt(answerA)
        print(realAnswerA)
    if choiceOfChoice == "B " or choiceOfChoice == "b " or choiceOfChoice == "b":
        choiceAB = float(input("what number is A?" ))
        choiceCB = float(input("What number is C?" ))
        answerB = float(choiceCB**2 - choiceAB)
        import math
        realAnswerB = math.sqrt(answerB)
        print(realAnswerB)
    if choiceOfChoice == "C " or choiceOfChoice == "c " or choiceOfChoice == "c":
        choiceAC = float(input("What number is A?"  ))
        choiceBC = float(input("What number is B?"  ))
        answerC = float(choiceAC**2 + choiceBC**2)
        realAnswerC = math.sqrt(float(answerC))
        print(realAnswerC)
if choice == "Square Area for a shape" or choice == "square area for a shape" or choice == "area":
    shapeCal = input("What shape do you want to find the area of?")
    if shapeCal == "Square" or shapeCal == "square":
        squareShape = int(input("What is the length or the width of the square? "))
        squareArea = +squareShape**2
        print(squareArea)
    if shapeCal == "Triangle" or shapeCal == "triangle":
        baseTri = int(input("What is the base of the triangle?"))
        Trheight = int(input("What is the height of the triangle? "))
        trishape = (baseTri/2)*Trheight
        print(trishape)
    if shapeCal == " Trapezoid" or shapeCal == "trapezoid":
        trapBaseS = float(input("What is the size of the base of the trapezoid?   "))
        trapBaseB = float(input("What is the other base's size?     "))
        trapHeight = float(input("What is the height of the trapezoid?  "))
        trapAnswer = float((trapBaseS + trapBaseB)/2*trapHeight)
        print(trapAnswer)
    if shapeCal == "Circle" or "circle":
        ciRad = int(input("What i the radius of the circle?  "))
        ciarea =math.pi*(ciRad**2)
        print(ciarea)
if choice == "Volume" or choice == "volume":
    volShape = input("What shape would you like to find the volume of?  ")
    if volShape == "Cube " or volShape == "cube " or volShape == "cube" or volShape == "Cube ":
        cubeVol = float(input("What is the length,height, or the width of the cube? "))
        cubeAnswer = cubeVol**3
        print(cubeAnswer)
    if volShape == "sphere" or volShape == "Sphere" or volShape == "sphere " or volShape == "Sphere ":
        sphereRad = float(input("What is the radius of the sphere?  "))
        import math
        sphereAnswer = (sphereRad**3)*math.pi * 1.3333333333
        print(sphereAnswer)
    if volShape == "pyramid" or volShape == "Pyramid":
        aprBaseLen = float(input("What is the length of the base? "))
        aprBaseWid = float(input("What is the width of the base? "))
        aprHeight = float(input("What is the height of the base?  "))
        aprAnser = aprBaseLen*aprBaseWid*aprHeight*0.33333333333
        print(aprAnser)
    if volShape == "cylinder" or volShape == "Cylinder":
        cyRad = float(input("What is the radius of the cylinder?    "))
        cyHeight = float(input("What is the heigh of the cylinder?  "))
        cyAnswer = cyRad*(cyHeight**2)*math.pi
        print(cyAnswer)
    if volShape == "cone" or volShape == "Cone" :
        cnRad = float(input("What is the radius of the cone?    "))
        cnHg = float(input("what is the height of the cone?  "))
        cnAnswer = math.pi*cnRad**2*cnHg/3
        print(cnAnswer)
