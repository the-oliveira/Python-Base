#Import the numpy package as np, so that you can refer to numpy with np.
#Use np.array() to create a numpy array from baseball. Name this array np_baseball.
#Print out the type of np_baseball to check that you got it right.

# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

#Create a numpy array from height_in. Name this new array np_height_in.
#Print np_height_in.
#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
#Print out np_height_m and check if the output makes sense.

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_heigh_m = np_height_in * 0.0254

# Print np_height_m
print(np_heigh_m)

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np.array(np_weight_kg / np_height_m ** 2)

# Print out bmi
print(bmi)

# Create the light array
light = np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])