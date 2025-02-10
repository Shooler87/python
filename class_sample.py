class Entity:
    def __init__(self):
        self.__private_var = 0
        self._protected_var = 0
        self.public_var = 0

    @staticmethod
    def __private_method():
        print("Entity __private_method")

    @staticmethod
    def _protected_method():
        print("Entity __protected_method")

    def public_method_a(self):
        self.__private_var = 1
        self._protected_var = 1
        print("Entity public_method_a")

    def public_method_b(self):
        self.public_method_a()


e = Entity()
print(e.public_var)
e.public_method_b()
