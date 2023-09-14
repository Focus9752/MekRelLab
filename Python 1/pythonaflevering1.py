import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Masse/svingingstid
#
# Massen af loddet (i g)
m_lod = np.array([10, 20, 50, 100, 200, 500, 1000])
# Svingingstiden for 5 svinginger (i s)
Tm1 = np.array([7.80, 8.25, 8.33, 8.30, 8.58, 8.85, 8.86])
Tm2 = np.array([7.96, 8.15, 8.32, 8.65, 8.63, 8.88, 8.95])

# Gennemsnitlige svingingstider for forsøget med ændring af loddets masse
mean_svinginstider_m = np.zeros(len(Tm1))
for i in range(len(mean_svinginstider_m)):
    mean_svinginstider_m[i] = np.mean([Tm1[i], Tm2[i]])

# Snorlængde/sviningstid
#
# Længde af snor (i cm)
l_snor = np.array([51.5, 51.5, 47.5, 47.5, 35.1, 35.1, 25.1, 25.1, 15.7, 15.7, 3.4, 3.4])
# Svingingstiden for 5 svininger (i s)
Tl1 = np.array([8.40, 8.31, 7.13, 6.10, 4.93, 3.15])
Tl2 = np.array([8.33, 8.00, 7.13, 5.95, 5.13, 3.15])

# Gennemsnitlige svingingstider for forsøget med ændring af snorens længde
mean_svinginstider_l= np.zeros(len(Tl1))
for i in range(len(mean_svinginstider_l)):
    mean_svinginstider_l[i] = np.mean([Tl1[i], Tl2[i]])

# Usikkerhed for målinger af svinginstiden (i s)
T_usikkerhed = 0.6
# Usikkerhed for målinger af snorlængden (i cm)
L_usikkerhed = 0.05

# Plots
# Forsøg med ændring af m
plt.figure(1)
plt.scatter(m_lod, mean_svinginstider_m)
plt.errorbar(m_lod, mean_svinginstider_m, fmt="none", yerr=T_usikkerhed)
plt.plot()

