"""The Euclidean Distance
It represents the distance between 2 points in a 2d space"""

FirstPoint_X = input("Please enter the value of the X coordinate for the First pont: ")
FirstPoint_Y = input("Please enter the value of the Y coordinate for the First pont: ")
SecondPoint_X = input("Please enter the value of the X coordinate for the Second pont: ")
SecondPoint_Y = input("Please enter the value of the Y coordinate for the Second pont: ")

print("Coordinates for the points are: (" + str(FirstPoint_X) + ", " + str(FirstPoint_Y) + ") and (" + str(SecondPoint_X) + ", " + str(SecondPoint_Y) + ")")

#Calculate Euclidean Distance
Euclidean_Distance = (int(FirstPoint_X) - int(SecondPoint_X))^2 + (int(FirstPoint_Y) - int(SecondPoint_Y))^2

print("Euclidean_Distance(FirstPoint, SecondPoint) = " + str(Euclidean_Distance))