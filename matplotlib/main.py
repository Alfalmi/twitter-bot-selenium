# importar pandas
import pandas as p
import matplotlib.pyplot as plt
from beakerx import *

# datos de RRSS 2020
fbk = ['Facebook', 2449, True, 2006]
twt = ['Twitter', 339, False, 2006]
ig = ['Instagram', 1000, True, 2010]
yt = ['YouTube', 2000, False, 2005]
lkn = ['LinkedIn', 663, False, 2003]
wsp = ['WhatsApp', 1600, True, 2009]

# lista con datos
lista_rrss = [fbk, twt, ig, yt, lkn, wsp]

# crear dataframe a partir de listas
df_rrss = pd.DataFrame(lista_rrss,
                       columns=['Nombre', 'Cantidad', 'ES_FBK', 'Año'])
df_rrss

# ejemplo super mega básico
x = [1, 2, 3, 4, 5]
y = [1, 8, 27, 64, 125]

plt.plot(x, y)
plt.show()
