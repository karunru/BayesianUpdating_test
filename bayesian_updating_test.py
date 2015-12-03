import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

pi = [0.1,0.4,0.5]
theta = [0.8,0.6,0.3]

X = np.random.choice(["H","T"],size=100,p=[theta[1],1-theta[1]])

print(X)
