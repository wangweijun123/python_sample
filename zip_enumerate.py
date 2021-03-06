x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
#for label,x,y,z in zip(labels, x_coord, y_coord, z_coord):
 #   points.append("{}:{},{},{}".format(label, x, y, z))

# zip
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}:{},{},{}".format(*point))

for point in points:
    print(point)



c = dict([('one', 1), ('two', 2), ('three', 3)])
print(c)



cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))

print(cast)




cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)





cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for index,value in enumerate(cast):
    cast[index] = value+str(heights[index])

print(cast)




data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
c1,c2,c3 = zip(*data);
print(c1)
print(c2)
print(c3)

data_transpose = tuple(zip(*data))
print(data_transpose)






