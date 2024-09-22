import numpy as np
import matplotlib.pyplot as plt


# Calcolo della tensione termica

q = 1.602E-19
T = 300
k_boltzman = 1.38E-23

V_termica = k_boltzman*T/q
print("V_T=", V_termica)

I_sat = 1E-14

V_start = 0
V_stop = 0.77
punti_di_calcolo = 1000

# Creo una sequenza di mille valori di tensione equispaziati per il calcolo della corrente

V_diodo = np.linspace(V_start, V_stop, punti_di_calcolo)

I_diodo = I_sat * np.exp(V_diodo/V_termica)

print("\n\nCaratteristica corrente - tensione")
print("Corrente[mA]", "Tensione[V]")

count = 0
for i in V_diodo:
    print(np.round(i, 3), "\t", 1000*np.round(I_sat * np.exp(i/V_termica),3))


# disegno la risposta nel tempo y(t)

plt.plot(V_diodo, I_diodo*1000, "Orange")
plt.title("Caratteristica Corrente - Tensione")
plt.xlabel('V_diodo')
plt.ylabel('I_diodo')
plt.grid()
plt.show()
