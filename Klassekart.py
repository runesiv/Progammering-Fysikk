import numpy as np
from tabulate import tabulate

N = 31
class_arrangement = np.arange(1, N)
np.random.shuffle(class_arrangement)

# lab (2 group x 3)
#class_arrangement = class_arrangement.reshape((3,2,5))

# room (3 pair x 5)
class_arrangement = class_arrangement.reshape((5,3,2))

table = []
for row in class_arrangement:
    table.append([" ".join(map(str, block)) for block in row])

# Print the formatted table
print(tabulate(table, tablefmt="simple_grid"))
