import sys
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt


""" Below are the user inputs. """

inputImageName = sys.argv[1]    
a1 = sys.argv[2]
a2 = sys.argv[3]
a3 = sys.argv[4]
a4 = sys.argv[5]
a5 = sys.argv[6]
a6 = sys.argv[7]

img = Image.open(inputImageName)
img = ImageOps.grayscale(img)
Taffine = np.array([[a1,a2,a3],[a4,a5,a6],[0,0,1]], int) # Calculating the Affine matrix.
inputMatrix = np.array(img) # Converting the input image to a matrix.
coordinatesMatrix = np.empty([3, len(inputMatrix[0]) * len(inputMatrix)], dtype=int) # Creating an empty array that will store 
middleRow = (len(inputMatrix) - 1) / 2                                               # the coordinates of each pixel in relation
middleColumn = (len(inputMatrix[0]) - 1) / 2                                         # to the reference point (which is the central pixel).

for i in range(len(inputMatrix)):                                                    # Filling the coordinates array with the right
    for j in range(len(inputMatrix[0])):                                             # coordinates in relation to the input array size.
        coordinatesMatrix[0][(len(inputMatrix[0]) * i) + j] = j - middleColumn
        coordinatesMatrix[1][(len(inputMatrix[0]) * i) + j] = i - middleRow
        coordinatesMatrix[2][(len(inputMatrix[0]) * i) + j] = 1

newCoordinatesMatrix = Taffine @ coordinatesMatrix  # The transformation is the result of this calculation.
imin = min(newCoordinatesMatrix[1]) # It is possible that the transformation will result in a bigger matrix,
imax = max(newCoordinatesMatrix[1]) # therefore we calculate the maximum and minimum coordinates,
jmin = min(newCoordinatesMatrix[0]) # in order to determine the size of the result matrix.
jmax = max(newCoordinatesMatrix[0])
resultMatrix = np.full([(imax - imin) + 1, (jmax - jmin) + 1], -1, dtype=int) # Initially, we fill the result matrix with -1's.

for i in range(len(newCoordinatesMatrix[0])):
    resultMatrix[newCoordinatesMatrix[1][i]][newCoordinatesMatrix[0][i]] = inputMatrix[coordinatesMatrix[1][i]][coordinatesMatrix[0][i]]
# After the above loop, only the pixels whose value will be determined by the nearest neighbour policy will have the value of -1, and that's how we spot them.
resultMiddleRow = (len(resultMatrix) - 1) / 2
resultMiddleColumn = (len(resultMatrix[0]) - 1) / 2

for i in range(len(resultMatrix)):  # This double loop implements the nearest neighbour policy.
    for j in range(len(resultMatrix[0])): # I choose to use the neighbour with the lowest coordinates possible.
        if(resultMatrix[i,j] == -1):
            if((i - 1 > 0 and j - 1 > 0) and (resultMatrix[i - 1, j - 1] != -1)): # Python uses lazy evaluation, so if the first
                resultMatrix[i][j] = resultMatrix[i - 1][j - 1]                   # condition is false, the second won't be
            elif((i - 1 > 0) and (resultMatrix[i - 1, j] != -1)):                 # evaluated, so we won't go out of bounds.
                resultMatrix[i][j] = resultMatrix[i - 1][j]
            elif((j - 1 > 0) and (resultMatrix[i , j - 1] != -1)):
                resultMatrix[i][j] = resultMatrix[i][j - 1]
            elif((i - 1 > 0 and j + 1 < len(resultMatrix[0])) and (resultMatrix[i - 1, j + 1] != -1)):
                resultMatrix[i][j] = resultMatrix[i - 1][j + 1]
            elif((j - 1 > 0 and i + 1 < len(resultMatrix)) and (resultMatrix[i + 1, j - 1] != -1)):
                resultMatrix[i][j] = resultMatrix[i + 1][j - 1]
            elif((j + 1 < len(resultMatrix[0])) and (resultMatrix[i, j + 1] != -1)):
                resultMatrix[i][j] = resultMatrix[i][j + 1]
            elif((i + 1 < len(resultMatrix)) and (resultMatrix[i + 1, j] != -1)):
                resultMatrix[i][j] = resultMatrix[i + 1][j]
            elif((j + 1 < len(resultMatrix[0])) and (i + 1 < len(resultMatrix)) and (resultMatrix[i + 1, j + 1] != -1)):
                resultMatrix[i][j] = resultMatrix[i + 1][j + 1]

startRow = int(resultMiddleRow - (len(inputMatrix) // 2))
endRow = int(len(inputMatrix) + startRow - 1)
startColumn = int(resultMiddleColumn - (len(inputMatrix[0]) // 2))
endColumn = int(len(inputMatrix[0]) + startColumn - 1)
outputMatrix = resultMatrix[startRow : (endRow + 1), startColumn : (endColumn + 1)]
outputImage = Image.fromarray(outputMatrix)
outputImage.show()







