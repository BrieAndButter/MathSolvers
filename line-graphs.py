input("Enter the coordinates of two points on the line when prompted. The gradient and intersect will then be displayed (Press Enter)")

x1 = int(input("Input x1"))
y1 = int(input("Input y1"))

x2 = int(input("Input x2"))
y2 = int(input("Input y2"))

gradient = (y2-y1)/(x2-x1)
print("Gradient: " + str(gradient))

# y1 - (x1*gradient) =  + intersect
intersect = y1 - (x1*gradient)
print("Intersect: " + str(intersect))
