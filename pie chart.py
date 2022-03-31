import matplotlib.pyplot as plt
import numpy as np

y = np.array([206, 196, 118, 92, 83, 39, 1])
mylabels = ["SPD", "CDU/CSU", "Greens", "FDP", "AFD", "Left Party","Inne"]

plt.pie(y, labels = mylabels, autopct='%1.1f%%')
plt.show() 