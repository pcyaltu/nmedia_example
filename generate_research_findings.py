import numpy as np

data = np.random.normal(size=(10, 5))
print("Table 1")
for row in data:
    print("\t".join(["%.3f" % v for v in row]))

