class Pousada:
    def __init__(self):
        self.hospedes = []

    def check_in(self, nome, quarto):
        hospede = {"nome": nome, "quarto": quarto}
        self.hospedes.append(hospede)
        print(f"{nome} fez o check-in no quarto {quarto}.")

    def mostrar_hospedes(self):
        if self.hospedes:
            print("Hóspedes atualmente na pousada:")
            for hospede in self.hospedes:
                print(f"Nome: {hospede['nome']}, Quarto: {hospede['quarto']}")
        else:
            print("Nenhum hóspede na pousada no momento.")

pousada = Pousada()

pousada.check_in("João Silva", 101)
pousada.check_in("Maria Oliveira", 102)

pousada.mostrar_hospedes()
