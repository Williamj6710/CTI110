#Calculate and display which rectangle has larger area
#10-04-19
#CTI-110 P3T1 - Areas Of Rectangles 
#Jacob Williams
#
#Get measurements of rectangle 1

r1_Length=int(input("Enter first rectangles Length:"))
r1_Width=int(input("Enter first rectangles Width:"))


#Get measurements of rectangle 2 
r2_Length=int(input("Enter second rectangles Length:"))
r2_Width=int(input("Enter second rectangles Width:"))

#Calculate area of rectangles
r1_Area=r1_Length*r1_Width
r2_Area=r2_Length*r2_Width

#Display which rectangle has greater area
if r1_Area>r2_Area:
    print("Rectangle 1 has the greater area")
elif r1_Area<r2_Area:
    print("Rectangle 2 has the greater area")
else:
    print("Both rectangles have the same area.")


#PsuedoCode
#Programs goal is to determine which rectangle has the greater area
#from user input data
#Have user input length and width for first rectangle
#Have user input length and width for second rectangle
#Calculate area of each rectangle
#If rectanlge one has greater area between the two print statement saying so
#If rectangle two has greater area print statement saying so
#If both rectangles have same area print statement saying so

