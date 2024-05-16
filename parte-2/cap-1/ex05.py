import matplotlib.pyplot as plt

#variavel life_exp e life_exp1950 criadas no db do curso.

# Histogram of life_exp, 15 bins
plt.hist(life_exp, 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, 15)

# Show and clear plot again
plt.show()
plt.clf()
