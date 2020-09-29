import matplotlib.pyplot as plt
import numpy as np

def read_data(filename, data) :

    # Read in data from file line by line
    infile = open(filename, 'r')
    
    line = infile.readline()

    while line :
        line = line.strip()
        data.append(line.split(','))
        line = infile.readline()
    
    infile.close()

    # Convert continuous attributes to float and class labels to integers
    for i in range(0, len(data)) : 
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
        data[i][2] = float(data[i][2])
        data[i][3] = float(data[i][3])
        data[i][4] = int(data[i][4])

filename = 'iris.csv'

# make an empty data List
data = []

read_data(filename, data)

# Convert data into a numpy array for plotting
all_irises = np.array(data)

# Divide up the data set by type of iris and covert to numpy arrays for plotting
setosa = []
versicolor = []
virginica = []

for instance in data :
    if(instance[4] == 1) :
        setosa.append(instance)
    elif(instance[4] == 2) :
        versicolor.append(instance)
    else :
        virginica.append(instance)

setosa_arr = np.array(setosa)
versicolor_arr = np.array(versicolor)
virginica_arr = np.array(virginica)

# Sepal length all irises plot
plt.plot(all_irises[:, 0])
plt.ylabel('Sepal Length (cm)')
plt.xlabel('Instance')
plt.title('Sepal length of all irises')
plt.xlim(0,150)
plt.xticks(np.arange(0, 150, step=20))
plt.savefig('sepal_length.png')
plt.close()

# Sepal length by type plot
plt.plot(setosa_arr[:, 0], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 0], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 0], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.ylabel('Sepal Length (cm)')
plt.xlabel('Instance')
plt.title('Sepal length of irises by type')
plt.savefig('sepal_length_type.png')
plt.close()

# Sepal width by type plot
plt.plot(setosa_arr[:, 1], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 1], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 1], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.ylabel('Sepal Width (cm)')
plt.xlabel('Instance')
plt.title('Sepal width of irises by type')
plt.savefig('sepal_width_type.png')
plt.close()

# Petal length by type plot
plt.plot(setosa_arr[:, 2], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 2], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 2], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Instance')
plt.title('Petal length of irises by type')
plt.savefig('petal_length_type.png')
plt.close()

# Petal width by type plot
plt.plot(setosa_arr[:, 3], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 3], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 3], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.ylabel('Petal Width (cm)')
plt.xlabel('Instance')
plt.title('Petal width of irises by type')
plt.savefig('petal_width_type.png')
plt.close()

# Petal length and petal width scatter plot
plt.scatter(setosa_arr[:, 2], setosa_arr[:, 3], color='black', label='Setosa', marker='*')
plt.scatter(versicolor_arr[:, 2], versicolor_arr[:, 3], color='red', label='Versicolor', marker='+')
plt.scatter(virginica_arr[:, 2], virginica_arr[:, 3], color='blue', label='Virginica', marker='o')
plt.legend(loc='upper left')
plt.ylabel('Petal Width (cm)')
plt.xlabel('Petal Length (cm)')
plt.title('Petal length and petal width of irises by type')
plt.xlim(0,7)
plt.ylim(0,3)
plt.savefig('petal_length_width_scatter.png')
plt.close()
