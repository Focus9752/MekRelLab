import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

# Importer data fra Excel filen
WS = pd.read_excel(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\labuge 5.xlsx")
WS_np = np.array(WS)

print(WS_np)

# Indlæs afstand i X og Y / cm
h_fast_arr = [WS_np[i][1] for i in range(len(WS_np))]
# Fjern alle tomme felter fra h_slip
h_slip_arr = np.array([WS_np[i][2] for i in range(len(WS_np))])
h_slip_arr = h_slip_arr[~np.isnan(h_slip_arr)]

print(h_slip_arr)

# Usikkerhed for alle målinger med linealen / cm
usikkerhed_d = 0.5

# Bestem middelværdi, standardafvigelse og usikkerhed på middelværdien
h_fast_mean = np.mean(h_fast_arr)
h_slip_mean = np.mean(h_slip_arr)

print("h_fast_mean, h_slip_mean")
print(h_fast_mean, h_slip_mean)

# Standardafvigelse
sigma_h_fast = np.std(h_fast_arr)
sigma_h_slip = np.std(h_slip_arr)

# Usikkerhed på middelværdien
d_h_fast_mean = sigma_h_fast / np.sqrt(len(h_fast_arr))
d_h_slip_mean = sigma_h_slip / np.sqrt(len(h_slip_arr))

print("d_h_fast_mean, d_h_slip_mean")
print(d_h_fast_mean, d_h_slip_mean)

plt.figure(1)
plt.hist(h_fast_arr, int(len(h_fast_arr)/1.5), label="Histogram for pendulets h_maks ved skud der sad fast [cm]")
plt.axvline(h_fast_mean - d_h_fast_mean, label=r"$\mu h_{fast} \pm \sigma_\mu h_{fast}$" + "[cm]", color="red")
plt.axvline(h_fast_mean + d_h_fast_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("h_fast [cm]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\histogram_h_fast.png", dpi=300)

plt.figure(2)
plt.hist(h_slip_arr, int(len(h_slip_arr)/1.5), label="Histogram for pendulets h_maks ved skud der ikke sad fast [cm]")
plt.axvline(h_slip_mean - d_h_slip_mean, label=r"$\mu h_{slip} \pm \sigma_\mu h_{slip}$" + "[cm]", color="red")
plt.axvline(h_slip_mean + d_h_slip_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("h_slip [cm]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\histogram_h_slip.png", dpi=300)

# Masse af projektil og lod [kg]
m = 0.00045
M = 0.029

# Tyngdeacceleration [m/s^2]
g = 9.82

# Mundingsenergi [J]
def E_munding(h):
    return ((m+M)**2/m)*g*(h/100)

# Mundingsenergier
E_fast_arr = [E_munding(h_fast_arr[i]) for i in range(0,len(h_fast_arr))]
E_slip_arr = [E_munding(h_slip_arr[i]) for i in range(0,len(h_slip_arr))]

# Bestem middelværdi, standardafvigelse og usikkerhed på middelværdien
E_fast_mean = np.mean(E_fast_arr)
E_slip_mean = np.mean(E_slip_arr)

print("\n")
print("E_fast_mean, E_slip_mean")
print(E_fast_mean, E_slip_mean)

# Standardafvigelse
sigma_E_fast = np.std(E_fast_arr)
sigma_E_slip = np.std(E_slip_arr)

# Usikkerhed på middelværdien
d_E_fast_mean = sigma_E_fast / np.sqrt(len(E_fast_arr))
d_E_slip_mean = sigma_E_slip / np.sqrt(len(E_slip_arr))

print("dEfast")
print(d_E_fast_mean)

plt.figure(3)
plt.hist(E_fast_arr, label="Histogram for projektilets mundingsenergi ved skud der sad fast")
plt.axvline(E_fast_mean - d_E_fast_mean, label=r"$\mu E_{munding} \pm \sigma_\mu E_{munding}$" + "[J]", color="red")
plt.axvline(E_fast_mean + d_E_fast_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("E_munding [J]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\histogram_Energi_fast.png", dpi=300)

plt.figure(4)
plt.hist(E_slip_arr, label="Histogram for projektilets mundingsenergi ved skud der ikke sad fast")
plt.axvline(E_slip_mean - d_E_slip_mean, label=r"$\mu E_{munding} \pm \sigma_\mu E_{munding}$" + "[J]", color="red")
plt.axvline(E_slip_mean + d_E_slip_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("E_munding [J]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\histogram_Energi_slip.png", dpi=300)

pdp = PdfPages(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 5 (ballistisk pendul)\plots.pdf")
pdp.savefig(1)
pdp.savefig(2)
pdp.savefig(3)
pdp.savefig(4)
pdp.close()

