import numpy as np

petal_length1 = [1.2, 2.3, 3.1, 1.8, 2.5]
petal_length2 = [0.9, 1.5, 2.1, 1.7, 2.0]
petal_length3 = [1.1, 1.9, 2.8, 1.6, 2.2]
petal_length4 = [1.5, 2.2, 2.9, 1.4, 1.8]

petal_width1 = [0.3, 0.4, 0.2, 0.5, 0.4]
petal_width2 = [0.2, 0.3, 0.5, 0.4, 0.3]
petal_width3 = [0.4, 0.2, 0.3, 0.6, 0.5]
petal_width4 = [0.3, 0.5, 0.4, 0.2, 0.3]

sepal_length1 = [5.1, 5.8, 6.0, 5.4, 6.2]
sepal_length2 = [4.9, 5.7, 6.2, 5.5, 6.7]
sepal_length3 = [5.0, 5.5, 6.3, 5.6, 6.4]
sepal_length4 = [4.8, 5.9, 6.4, 5.7, 6.3]

sepal_width1 = [3.5, 3.0, 3.2, 3.1, 2.8]
sepal_width2 = [3.0, 2.8, 3.1, 2.9, 3.1]
sepal_width3 = [3.6, 3.1, 3.4, 3.0, 3.2]
sepal_width4 = [3.1, 2.7, 3.3, 3.2, 2.9]

# Ask for user input
petal_length = input("Enter petal length value: ")
petal_width = input("Enter petal width value: ")
sepal_length = input("Enter sepal length value: ")
sepal_width = input("Enter sepal width value: ")


# Convert input string to list of floats
petal_length = [float(x) for x in petal_length.split()]
petal_width = [float(x) for x in petal_width.split()]
sepal_length = [float(x) for x in sepal_length.split()]
sepal_width = [float(x) for x in sepal_width.split()]

flower_1 = np.concatenate((petal_length1, petal_width1, sepal_length1, sepal_width1))
flower_2 = np.concatenate((petal_length2, petal_width2, sepal_length2, sepal_width2))
flower_3 = np.concatenate((petal_length3, petal_width3, sepal_length3, sepal_width3))
flower_4 = np.concatenate((petal_length4, petal_width4, sepal_length4, sepal_width4))

array_length = len(petal_length1)

distance1 = np.zeros(array_length)
distance2 = np.zeros(array_length)
distance3 = np.zeros(array_length)
distance4 = np.zeros(array_length)




for i in range(array_length-1):
    distance1[i] = ((petal_length - flower_1[array_length*1]) ** 2 + (petal_width - flower_1[array_length*2]) ** 2 + (sepal_length - flower_1[array_length*3]) ** 2 + (sepal_width - flower_1[(array_length*4)-1]) ** 2) ** 0.5
    distance2[i] = ((petal_length - flower_2[array_length*1]) ** 2 + (petal_width - flower_2[array_length*2]) ** 2 + (sepal_length - flower_2[array_length*3]) ** 2 + (sepal_width - flower_2[(array_length*4)-1]) ** 2) ** 0.5
    distance3[i] = ((petal_length - flower_3[array_length*1]) ** 2 + (petal_width - flower_3[array_length*2]) ** 2 + (sepal_length - flower_3[array_length*3]) ** 2 + (sepal_width - flower_3[(array_length*4)-1]) ** 2) ** 0.5
    distance4[i] = ((petal_length - flower_4[array_length*1]) ** 2 + (petal_width - flower_4[array_length*2]) ** 2 + (sepal_length - flower_4[array_length*3]) ** 2 + (sepal_width - flower_4[(array_length*4)-1]) ** 2) ** 0.5


distance = np.concatenate((distance1, distance2, distance3, distance4))

distance_sorted = np.sort(distance)

distances_min_5 = distance_sorted[:5]

# Check where min_distance exists in data set
for dist in distances_min_5:
    if dist in distance1 :
        print("THIS IS FLOWER 1")
    elif dist in distance2 :
        print("THIS IS FLOWER 2")
    elif dist in distance3 :
        print("THIS IS FLOWER 3")
    elif dist in distance4 :
        print("THIS IS FLOWER 4")


    