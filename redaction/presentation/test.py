import matplotlib.pyplot as plt

#data = {
#        "Inversión": {"Equipamiento": 6123.5, "Operación": 3086},
#        "Operación": {"Insumos": 6172.7, "Electricidad": 106.3, "Sueldos":1428.6}
#        }

data = {
        "EtOH Entero": [3.08],
        "EtOH Molido": [2.84],
        "n-Hex Entero": [2.29],
        "n-Hex Molido": [2.31]
        }

for label in data:
    plt.bar(label, data[label], width=0.7, color='blue')

#min_height = 0
#for label in data:
#    min_height = 0
#    x = dict(sorted(data[label].items(), key=lambda item: item[1]))
#    max_height = sum(x.values())
#    for origin in x:
#        plt.bar(label, max_height-min_height, width = 0.3, alpha = 0.8)
#        plt.annotate(origin, (max_height-min_height, 1))
#        min_height = x[origin]

plt.rcParams['figure.figsize'] = 5,7

plt.ylabel('Porcentaje respecto hoja')
plt.xlabel('Solvente')
plt.savefig('figs/experimental-seleccion-solvente.png',dpi=200)
plt.show()
    

