import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# These variables are used for the convergence plot at the end
iteration_amount = 100
centroid_amount = 6
iterations = []
convergence = []
error = 1

# Load the data and initialize the required variables
data = np.loadtxt("kmeans/data.txt", delimiter=',')
numberOfRows = data.reshape(int(data.size/3), 3).astype(int)
middlePoints = np.random.uniform(0, np.amax(data), (centroid_amount, 3)).astype(int)
centerPointCumulativeSum = np.zeros([centroid_amount, 3], dtype=int)
counts = np.zeros([1, centroid_amount], dtype=int)
distances = np.zeros([numberOfRows.shape[0], centroid_amount], dtype=int)
oldMiddlePoints = np.copy(middlePoints)

# Loop through all the data points while calculating distance to 
# each of the randomly selected points the selected amount of times
t = 0
while error != 0:
    for x in range(numberOfRows.shape[0]):
        for y in range(middlePoints.shape[0]):
            distances[x, y] = np.linalg.norm(numberOfRows[x] - middlePoints[y])
        index = np.argmin(distances[x])
        counts[0, index] += 1
        centerPointCumulativeSum[index] += numberOfRows[x]

    # Converging by taking the mean of the distance to the 'hit' points
    for row in range(middlePoints.shape[0]):
        if counts[0, row] <= 10:
            middlePoints[row] = np.random.uniform(np.amin(data), np.amax(data), (1, 3)).astype(int)
        else:
            for col in range(3):
                middlePoints[row, col] = centerPointCumulativeSum[row, col] / counts[0, row]
    
    error = np.linalg.norm(middlePoints - oldMiddlePoints).astype(int)
    convergence.append(error)
    oldMiddlePoints = np.copy(middlePoints)
    print(error)

    # Reset the variables used for the convergence
    # If check to see if on last loop to keep values for debugging
    if error != 0:
        centerPointCumulativeSum *= 0
        counts *= 0
    t += 1
    iterations.append(t)

print(counts)

# find the indices of the max and min values of each column
max_x = np.argmax(middlePoints[:, 0])
min_x = np.argmin(middlePoints[:, 0])
max_y = np.argmax(middlePoints[:, 1])
min_y = np.argmin(middlePoints[:, 1])
max_z = np.argmax(middlePoints[:, 2])
min_z = np.argmin(middlePoints[:, 2])
# extract the corresponding rows from the array
max_x_row = np.take(middlePoints, max_x, axis=0)
min_x_row = np.take(middlePoints, min_x, axis=0)
max_y_row = np.take(middlePoints, max_y, axis=0)
min_y_row = np.take(middlePoints, min_y, axis=0)
max_z_row = np.take(middlePoints, max_z, axis=0)
min_z_row = np.take(middlePoints, min_z, axis=0)
# stack the rows vertically in the desired order
sorted_array = np.vstack((max_x_row, min_x_row, max_y_row, min_y_row, max_z_row, min_z_row))
print(sorted_array)

formatted_middlePoints = "int CP[6][3] = {\n"
for x in sorted_array:
    formatted_middlePoints += "    {" + ", ".join(map(str, x)) + "},\n"
formatted_middlePoints += "};\n"

with open("TL_Project_Week6/src/datapoints.h", 'w') as file:
    file.write(formatted_middlePoints)

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')

# Plot data points in each cluster
for i in range(data.shape[0]):
    ax1.scatter(numberOfRows[i, 0], numberOfRows[i, 1], numberOfRows[i, 2], c='g')

# Plot centroids
for i in range(4):
    ax1.scatter(middlePoints[i, 0], middlePoints[i, 1], middlePoints[i, 2], c='k', s=100)

# Creates a convergence plot
ax2 = fig.add_subplot(122)
ax2.plot(iterations, convergence)
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Sum of Distances')
ax2.set_title('Convergence Plot')

plt.tight_layout()
plt.show()