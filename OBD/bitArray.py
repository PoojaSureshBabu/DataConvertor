
class bitarray:

    def __init__(self, _bytearray):
        self.bits = ""
        for b in _bytearray:
            v = bin(b)[2:]
            self.bits += ("0" * (8 - len(v))) + v # pad it with zeros

    def __getitem__(self, key):
        if isinstance(key, int):
            if key >= 0 and key < len(self.bits):
                return self.bits[key] == "1"
            else:
                return False
        elif isinstance(key, slice):
            bits = self.bits[key]
            if bits:
                return [ b == "1" for b in bits ]
            else:
                return []

    def num_set(self):
        return self.bits.count("1")

    def num_cleared(self):
        return self.bits.count("0")

    def value(self, start, stop):
        bits = self.bits[start:stop]
        if bits:
            return int(bits, 2)
        else:
            return 0

    def __len__(self):
        return len(self.bits)

    def __str__(self):
        return self.bits

    def __iter__(self):
        return [ b == "1" for b in self.bits ].__iter__()