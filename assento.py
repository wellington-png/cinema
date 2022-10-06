class Assento:
    def __init__(self, codigo_assento) -> None:
        self.__codigo_assento = codigo_assento

    @property
    def codigo_assento(self):
        return self.__codigo_assento

    def __str__(self) -> str:
        return f"{self.codigo_assento}"

if __name__ == "__main__":
    print(Assento("Tetxzdsd"))