class IntJoukko:
    def __init__(self, *args, **kwargs) -> None:
        self.ljono = kwargs.get("ljono", [])

    @property
    def alkioiden_lkm(self) -> int:
        return len(self.ljono)

    def kuuluu(self, n) -> bool:
        return n in self.ljono

    def lisaa(self, n) -> bool:
        if not self.kuuluu(n):
            self.ljono.append(n)
            return True
        return False

    def poista(self, n) -> bool:
        if self.kuuluu(n):
            self.ljono.pop(self.ljono.index(n))
            return True
        return False

    def mahtavuus(self) -> int:
        return self.alkioiden_lkm

    def to_int_list(self) -> list:
        return self.ljono

    @staticmethod
    def yhdiste(a, b) -> "IntJoukko":
        return IntJoukko(ljono=a.to_int_list() + b.to_int_list())

    @staticmethod
    def leikkaus(a, b) -> "IntJoukko":
        return IntJoukko(ljono=[i for i in a.to_int_list() if b.kuuluu(i)])

    @staticmethod
    def erotus(a, b) -> "IntJoukko":
        return IntJoukko(ljono=[i for i in a.to_int_list() if not b.kuuluu(i)])

    def __str__(self) -> str:
        return "{" + ", ".join([str(i) for i in self.to_int_list()]) + "}"
