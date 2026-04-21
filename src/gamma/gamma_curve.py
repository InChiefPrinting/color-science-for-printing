import numpy as np
import matplotlib.pyplot as plt

def gamma_encode(x, gamma=2.2):
    return x ** (1/gamma)

x = np.linspace(0,1,100)

plt.plot(x, gamma_encode(x))
plt.title("Gamma Curve")
plt.show()