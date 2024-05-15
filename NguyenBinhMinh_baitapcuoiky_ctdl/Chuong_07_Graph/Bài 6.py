class DoThi:
    def __init__(self):
        self.do_thi = {}

    def them_dinh(self, v):
        if v not in self.do_thi:
            self.do_thi[v] = []

    def them_canh(self, u, v):
        if u in self.do_thi and v in self.do_thi:
            self.do_thi[u].append(v)

    def SoCungVao(self, v):
        if v in self.do_thi:
            return sum(v in self.do_thi[u] for u in self.do_thi)
        else:
            return None
