import numpy as np

data = np.random.uniform(size=(6, 5))
print("Table 2")
for row in data:
    print("\t".join(["%.3f" % v for v in row]))

