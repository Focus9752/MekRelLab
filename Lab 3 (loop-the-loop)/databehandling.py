import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages


# cm
dh = 0.5
dx = 2.5

# R = 18.5 (h_teoretisk = 46.25)

# h / cm
h_arr = np.array([46, 60, 55, 40, 62.5])
# afstand langs loopet / cm
x_arr = np.array([np.mean(np.array([6*5, 6*5, 6*5])) + 6, np.mean(np.array([9*5, 9*5, 9*5]) + 6), np.mean(np.array([8*5, 8*5, 9*5]) + 6), np.mean(np.array([6*5, 6*5, 6*5]) + 6), np.mean(np.array([109, 9*5 + 6, 10*5 + 6]))])


plt.figure(1)
plt.errorbar(h_arr, x_arr, xerr=dx, yerr=dh, fmt="o", color="blue", ecolor="red", label="usikkerhed på x")

# Legend
plt.scatter(h_arr, x_arr, label="h og x")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_title("Højde og afstand bevæget for r = 18.5 cm")
ax.set_xlabel("h / cm")
ax.set_ylabel("x / cm")
plt.plot()



# R = 22.5 (h_teoretisk = 56.25)

# h / cm
h_arr2 = np.array([56, 62.5, 70, 80])
# afstand langs loopet / cm (husk at lægge 6 cm til)
x_arr2 = np.array([np.mean(np.array([9*5, 8*5, 8*5 ]) + 6), np.mean(np.array([9*5, 9*5, 9*5]) + 6), np.mean(np.array([10*5, 10*5, 9*5]) + 6), np.mean(np.array([131.5, 131.5, 11*5]))])

plt.figure(2)
plt.errorbar(h_arr2, x_arr2, xerr=dx, yerr=dh, fmt="o", color="blue", ecolor="red", label="usikkerhed på x")

# Legend
plt.scatter(h_arr2, x_arr2, label="h og x")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_title("Højde og afstand bevæget for r = 22.5 cm")
ax.set_xlabel("h / cm")
ax.set_ylabel("x / cm")
plt.plot()


print(h_arr)
print(x_arr)

print("\n")

print(h_arr2)
print(x_arr2)



pdp = PdfPages(r"C:\Users\marcu\OneDrive\Documents\GitHub\MekRelLab\Lab 3 (loop-the-loop)\plots.pdf")
pdp.savefig(1)
pdp.savefig(2)
pdp.close()


