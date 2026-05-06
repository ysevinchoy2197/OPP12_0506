class Laptop:
    def __init__(self, brand, ram, storage, serial):
        self.brand = brand
        self._ram = ram
        self._storage = storage
        self.__serial = serial

    def upgrade_ram(self, x):
        self._ram += x

    def upgrade_storage(self, x):
        self._storage += x

    def info(self):
        print(f"RAM:{self._ram} Storage:{self._storage}")
