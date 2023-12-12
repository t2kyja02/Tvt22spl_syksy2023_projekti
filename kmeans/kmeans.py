import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# These variables are used for the convergence plot at the end
iteration_amount = 100
centroid_amount = 4
iterations = []
convergence = []
error = 1

# Load the data and initialize the required variables
data = np.loadtxt("kmeans/putty.log")
numberOfRows = data.reshape(int(data.size/3), 3).astype(int)
middlePoints = np.random.uniform(0, max(data), (centroid_amount, 3)).astype(int)
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
        if counts[0, row] <= 0:
            middlePoints[row] = np.random.uniform(min(data), max(data), (1, 3)).astype(int)
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

print(distances)
print(counts)

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')

# Plot data points in each cluster
for i in range(40):
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