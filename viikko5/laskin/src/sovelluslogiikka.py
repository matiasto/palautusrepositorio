class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tulokset = []

    # make a wrapper for each method that adds the current value to the history
    def tulos_history(method):
        def wrapper(self, *args, **kwargs):
            self.tulokset.append(self.tulos)
            method(self, *args, **kwargs)
        return wrapper

    @tulos_history
    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    @tulos_history
    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    @tulos_history
    def nollaa(self, *args):
        self.tulos = 0

    @tulos_history
    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self, *args):
        if self.tulokset:
            self.tulos = self.tulokset.pop()
        else:
            self.tulos = 0
