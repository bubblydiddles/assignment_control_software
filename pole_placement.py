import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
A = np.array([[ 1, 1,]
              ,[0, 1]])
C = np.array([[1, 0]])
P = np.array([0.9, 0.8])
fsf1 = signal.place_poles(A.T, C.T, P, method='KNV0')
print(fsf1.gain_matrix)

t = np.linspace(0, 2*np.pi, 401)
plt.plot(np.cos(t), np.sin(t), 'k--')  # unit circle
plt.plot(fsf1.requested_poles.real, fsf1.requested_poles.imag,
         'wo', label='Desired')
plt.plot(fsf1.computed_poles.real, fsf1.computed_poles.imag, 'bx',
         label='Placed')
plt.grid()
plt.axis('image')
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, numpoints=1)
plt.show()