import uproot
import awkward as ak
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

file=uproot.open("/home/public/data/ggH125/ZZ4lAnalysis.root")
w_eve=file["ZZTree/candTree/overallEventWeight"].array()
sigma=file["ZZTree/candTree/xsec"].array()
sumw_eve=file["ZZTree/Counters"].values()[39]
w_gg=137000*sigma*w_eve/sumw_eve
p_gg=file["ZZTree/candTree/p_GG_SIG_ghg2_1_ghz1_1_JHUGen"].array()
p_qq=file["ZZTree/candTree/p_QQB_BKG_MCFM"].array()
D_gg=1/(1+p_qq/p_gg)

file=uproot.open("/home/public/data/qqZZ/ZZ4lAnalysis.root")
w_eve=file["ZZTree/candTree/overallEventWeight"].array()
sigma=file["ZZTree/candTree/xsec"].array()
sumw_eve=file["ZZTree/Counters"].values()[39]
w_qq=137000*sigma*w_eve/sumw_eve
p_gg=file["ZZTree/candTree/p_GG_SIG_ghg2_1_ghz1_1_JHUGen"].array()
p_qq=file["ZZTree/candTree/p_QQB_BKG_MCFM"].array()
D_qq=1/(1+70*p_qq/p_gg)

plt.figure(1)
counts_ggH125, bins_ggH125, _ = plt.hist(D_gg, bins=100, color='blue',density=True,label="ggH125", weights = w_gg, alpha=0.7, range=[0,1])
counts_qqZZ, bins_qqZZ, _ = plt.hist(D_qq, bins=100, color='red',density=True,label="qqZZ", weights = w_qq, alpha=0.7, range=[0,1])
plt.xlabel("$D_{kin}^{bkg}$")
plt.legend()

plt.savefig("D.jpg")

plt.figure(2)
sig_eff=[]
bkg_eff=[]   
x=np.linspace(0, 1 ,1001)
for k in x:
    sig_eff.append(np.sum(w_gg[D_gg>k])/np.sum(w_gg))
    bkg_eff.append(np.sum(w_qq[D_qq>k])/np.sum(w_qq))

plt.ylim(0.95,1.002)
plt.xlabel("Background Efficiency")
plt.ylabel("Signal Efficiency")
plt.plot(bkg_eff, sig_eff)
plt.savefig("ROC_unbinned.jpg")

area = simpson(sig_eff, dx=1/(len(x)-1))
print(f"AUC (unbinned) = {area}")


plt.figure(3)
sig_eff=[]
bkg_eff=[]
bin_width=bins_ggH125[1]-bins_ggH125[0]
for index, _ in enumerate(bins_ggH125):
    sig_eff.append(np.sum(counts_ggH125[index:])*bin_width)
    bkg_eff.append(np.sum(counts_qqZZ[index:])*bin_width)

plt.ylim(0.95,1.002)
plt.xlabel("Background Efficiency")
plt.ylabel("Signal Efficiency")
plt.plot(bkg_eff, sig_eff)
plt.savefig("ROC_binned.jpg")

area = simpson(sig_eff, dx=bin_width)
print(f"AUC (binned) = {area}")
