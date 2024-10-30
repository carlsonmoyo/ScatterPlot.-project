import matplotlib.pyplot as plt
def plot_data():
   my_file = open('C:/Users/USER/Documents/x_y_coordinates.txt', 'r')
   # creating two empty lists , one for x and the other for y coordinates
   my_file.readline()
   x_coordinates = []
   y_coordinates = []
    #reading the first line to skip the file header
    # reading the remaining lines with coordinates
   for line in my_file.readlines():
         x_coordinates.append(float(line.split(', ')[0]))
         y_coordinates.append(float(line.split(', ')[1]))
         print(type(x_coordinates[0]))
   plt.scatter(x_coordinates ,y_coordinates)
   plt.ylabel('Y Coordinates')
   plt.xlabel('X Coordinates')
   plt.title('Scatter Plot of Coordinates')
   plt.grid(True)
   plt.show()
plot_data()