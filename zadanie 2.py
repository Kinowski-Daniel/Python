import matplotlib.pyplot as plt
import numpy as np

z = ["Włochy","Węgry","Szwecja","Słowenia","Słowacja","Rumunia","Portugalia","Polska","Niemcy","Malta","Łotwa","Luksemburg","Litwa","Irlandia","Holandia","Hiszpania","Grecja","Francja","Finlandia","Estonia","Dania","Czechy","Cypr","Chorwacja","Bułgaria","Belgia","Austria"]
w = [1672438,112399,462057,39769,80958,169578,184931,424269,3134070,9898,25021,54195,38637,265835,697219,1113851,175888,2228857,214062,20916,276805,174412,17901,45557,47364,421611,349344]


fig, ax = plt.subplots()
plt.bar(z, w)
plt.show()

