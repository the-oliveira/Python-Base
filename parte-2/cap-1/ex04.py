#Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
#Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()
plt.clf()

# Build histogram with 5 bins
plt.hist(life_exp, 5)

# Show and clean up plot
plt.show()
plt.clf() #clf = limpa o grafico para que possa mostrar mais chamadas.

# Build histogram with 20 bins
plt.hist(life_exp, 20)

# Show and clean up again
plt.show()
plt.clf()