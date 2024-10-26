import uproot
import awkward as ak
import matplotlib.pyplot as plt
import numpy as np

file=uproot.open("/home/public/data/ggH125/ZZ4lAnalysis.root")
Pt=file["ZZTree/candTree/LepPt"].array()
Eta=file["ZZTree/candTree/LepEta"].array()
Phi=file["ZZTree/candTree/LepPhi"].array()

px=Pt*np.cos(Phi)
py=Pt*np.sin(Phi)
pz=Pt*np.sinh(Eta)
E=np.sqrt(pow(px, 2)+pow(py, 2)+ pow(pz, 2))

E_H=ak.sum(E, axis=1)
px_H=ak.sum(px, axis=1)
py_H=ak.sum(py, axis=1)
pz_H=ak.sum(pz, axis=1)
m_H=np.sqrt(pow(E_H, 2)-pow(px_H, 2)-pow(py_H, 2)-pow(pz_H, 2))

E_Z1=ak.sum(E[:, :2], axis=1)
px_Z1=ak.sum(px[:, :2], axis=1)
py_Z1=ak.sum(py[:, :2], axis=1)
pz_Z1=ak.sum(pz[:, :2], axis=1)
m_Z1=np.sqrt(pow(E_Z1, 2)-pow(px_Z1, 2)-pow(py_Z1, 2)-pow(pz_Z1, 2))

plt.figure(figsize=(8, 6))
plt.hist(m_Z1, bins=100, range=(50,150), color='blue', alpha=0.7,label="Z1")
plt.hist(m_H, bins=100, range=(50,150), color='red', alpha=0.7, label="H")
plt.xlabel("m [GeV]")
plt.ylabel("Broj raspada")
plt.title("Raspad Higgsovog bozona")
plt.legend()
plt.savefig('Higgs')