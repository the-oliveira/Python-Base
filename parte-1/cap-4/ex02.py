#Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
#Print out the type of np_baseball.
#Print out the shape attribute of np_baseball. Use np_baseball.shape.

# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball

np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123, 0])

# Print out addition of np_baseball and updated
updated = np.array(updated)
print(np_baseball + updated)

# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]
np.array(conversion)

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
