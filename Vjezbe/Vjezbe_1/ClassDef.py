import numpy as np

class Boson:
    isFermion=False
    def __init__(self, name, spin, momentum):
        self.name=name
        self.spin=spin
        self.momentum=momentum
    def PrintInfo(self):
        print("Name: " + str(self.name))
        print("Spin: " + str(self.spin))
        print("Momentum: " + str(self.momentum))
        if self.isFermion==True:
            print("Fermion")
        else:
            print("Boson")

class Higgs(Boson):
    def __init__(self, name, spin, momentum, MassMean):
        super().__init__(name, spin, momentum)
        self.MassSigma=1
        self.MassMean=MassMean

    def Energy(self):
        m=np.random.normal(self.MassMean, self.MassSigma)
        E=np.sqrt(m**2+self.momentum**2)
        return E