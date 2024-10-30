import uproot
import awkward as ak
import matplotlib.pyplot as plt
import numpy as np

file=uproot.open("/home/public/data/Lifetime/Lifetime.root:Tree")
A=file["t"].array()

plt.figure(figsize=(8, 6))
plt.hist(A, bins=100, range=(0, 8), color='blue', alpha=0.7)
plt.xlabel("t [s]")
plt.ylabel("Vrijeme raspada")
plt.savefig('traspad')