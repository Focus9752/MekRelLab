import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

# Importer data fra Excel filen
WS = pd.read_excel(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 4 (katapult)\data.xlsx")
WS_np = np.array(WS)

# Indlæs afstand i X og Y / cm
X_arr = [WS_np[i][1] for i in range(len(WS_np))]
Y_arr = [WS_np[i][2] for i in range(len(WS_np))]

# Usikkerhed for alle målinger med linealen / cm
usikkerhed = 0.05

# Bestem middelværdi og usikkerhed på middelværdien
X_mean = np.mean(X_arr)
Y_mean = np.mean(Y_arr)

print(X_mean, Y_mean)

# Standardafvigelse
sigma_X = np.std(X_arr)
sigma_Y = np.std(Y_arr)

print(sigma_X, sigma_Y)

# Usikkerhed på middelværdien
d_X_mean = sigma_X / np.sqrt(len(X_arr))
d_Y_mean = sigma_Y / np.sqrt(len(Y_arr))

print(d_X_mean, d_Y_mean)

# Plot
plt.figure(1)

# Scatter
plt.scatter(X_arr, Y_arr, label="Scatterplot af skytsene")
plt.errorbar(X_arr, Y_arr, xerr=usikkerhed, yerr=usikkerhed, label="Måleusikkerhed", fmt=" ", color="red")

# Middelværdi
plt.errorbar(X_mean, Y_mean, marker='*', color="green", ls='none', label="Middelværdi for X og Y")
plt.errorbar(X_mean, Y_mean, xerr=d_X_mean, yerr=d_Y_mean, fmt=" ", color="red")
plt.legend(loc="lower right")

ax = plt.gca()
ax.set_title("Scatterplot af skytsene")
ax.set_xlabel("x [cm]")
ax.set_ylabel("y [cm]")
plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 4 (katapult)\scatter.png", dpi=300)

plt.figure(2)
plt.hist(X_arr, int(len(X_arr)/2), label="Histogram for X [cm]")
plt.axvline(X_mean - d_X_mean, label=r"$\mu_x \pm \sigma_\mu X$" + "[cm]", color="red")
plt.axvline(X_mean + d_X_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("x [cm]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 4 (katapult)\histogramX.png", dpi=300)

plt.figure(3)
plt.hist(Y_arr, int(len(Y_arr)/2), label="Histogram for Y [cm]")
plt.axvline(Y_mean - d_Y_mean, label=r"$\mu_y \pm \sigma_\mu Y$" + "[cm]", color="red")
plt.axvline(Y_mean + d_Y_mean, color="red")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xlabel("y [cm]")
ax.set_ylabel("n")

plt.plot()
plt.savefig(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 4 (katapult)\histogramY.png", dpi=300)

pdp = PdfPages(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 4 (katapult)\plots.pdf")
pdp.savefig(1)
pdp.savefig(2)
pdp.savefig(3)
pdp.close()

