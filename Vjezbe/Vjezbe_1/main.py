import ClassDef as cd

a=cd.Higgs("Higgs boson", 0, 200, 125)
b=cd.Boson("Photon", 1, 50)
b.PrintInfo()
print(a.Energy())