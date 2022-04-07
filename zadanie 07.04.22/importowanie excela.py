import pandas as pd
import matplotlib.pyplot as plt


var = pd.read_excel("zadanko2.xlsx")
print(var)

x = list(var['X values'])
y = list(var['Y values'])


plt.bar(x, y, color = 'g', width = 0.72, label = "średnia")
plt.xlabel('Imiona')
plt.title('Średnia')
plt.legend()
plt.show()
