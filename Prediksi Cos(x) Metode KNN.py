# from aklearn import neural network
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Database
FileDB = 'cos_dataset.txt'
Database = pd.read_csv(FileDB, sep="\t")  # Sesuaikan separator dengan file txt Anda
print("----------------------------")
print(Database)

# x data, y target
x = Database[['x']]  # Sesuaikan nama kolom dengan header yang ada di file txt Anda
y = Database['cos(x)']  # Sesuaikan nama kolom dengan header yang ada di file txt Anda

# Create KNeighborsRegressor model
reg = KNeighborsRegressor(n_neighbors=1)
reg.fit(x, y)

# Display predicted data
xx = np.arange(1, 21, 1)
n = len(xx)
print("xx(i) K-NN")
for i in range(n):
    y_neighbor = reg.predict([[xx[i]]])
    print('{:.2f}'.format(xx[i]), y_neighbor)

# Plot the predicted data
y_neighbor2 = reg.predict(x)
plt.figure()
plt.plot(x, y_neighbor2, color='red')
plt.scatter(x, y, color='blue')
plt.title('Prediksi Data Menggunakan K-Nearest Neighbors')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend(['nearest neighbors', 'data'], loc=2)
plt.show()
