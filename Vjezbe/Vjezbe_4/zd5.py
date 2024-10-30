import numpy as np
import uproot
import awkward as ak
from scipy.stats import expon

file=uproot.open("/home/public/data/Lifetime/Lifetime.root:Tree")
A=file["t"].array()

loc, tau= expon.fit(A, floc=0)

n_bootstraps = 1000
tau_bootstrap_samples = []
for _ in range(n_bootstraps):
    sample = np.random.choice(A, size=len(A), replace=True)
    _, tau_sample = expon.fit(sample, floc=0)
    tau_bootstrap_samples.append(tau_sample)
sigma = np.std(tau_bootstrap_samples)

print("Tau=", tau)
print("sigma=", sigma)