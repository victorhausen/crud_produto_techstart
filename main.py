class Produto:
    __nome: str
    __descricao: str
    __valor: float

    def __init__(self, nome, descricao, valor):
        try:
            self.set_nome(nome)
            self.set_descricao(descricao)
            self.set_valor(valor)
        except:
            raise TypeError

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def get_valor(self) -> int:
        return self.__valor

    def set_valor(self, valor: float):
        if valor.replace(".", "").isdigit():
            self.__valor = float(valor)
        else:
            print("For value, type digits only.")
            raise TypeError


def createProduto():
    try:
        nome = input("What's the product's  name?")
        descricao = input("What's the product's las name?")
        valor = input("What's the product's value? $")
        memory['Produtos'].append(Produto(nome, descricao, valor))

        print('ok')
    except TypeError:
        main()


def showProdutos():
    print('These are the products.')
    for i, e in enumerate(memory["Produtos"]):
        print("id: {} | {} {} ($ {})".format(i, e.get_nome(), e.get_descricao(), str(e.get_valor())))
    print("")


def updateProduto():
    try:
        input_str = input("What is the product's id?")
        print(" > {} {} ({})".format(memory['Produtos'][int(input_str)].get_nome(),
                                 memory['Produtos'][int(input_str)].get_descricao(),
                                 str(memory['Produtos'][int(input_str)].get_valor())))

        nome = input("This product's  name is currently: {}. If you want to keep it just press enter.".format(
            memory['Produtos'][int(input_str)].get_nome()))
        descricao = input("This product's description is currently: {}. If you want to keep it just press enter.".format(
            memory['Produtos'][int(input_str)].get_descricao()))
        valor = input("This product's name is currently: {}. If you want to keep it just press enter.".format(
            str(memory['Produtos'][int(input_str)].get_valor())))

        if nome != "":
            memory['Produtos'][int(input_str)].set_nome(nome=nome)
        if descricao != "":
            memory['Produtos'][int(input_str)].set_descricao(descricao=descricao)
        if valor != "":
            memory['Produtos'][int(input_str)].set_valor(valor=valor)

    except:
        print("Opa, Valor invalido!")
        main()


def deleteProduto():
    try:
        input_str = input("What is the product's id?")
        print(" > {} {} ({})".format(memory['Produtos'][int(input_str)].get_nome(),
                                     memory['Produtos'][int(input_str)].get_descricao(),
                                     str(memory['Produtos'][int(input_str)].get_valor())))

        option = input("Are you sure you want to delete it? [y/n]")
        if option.casefold() == "y".casefold():
            memory['Produtos'].remove(memory['Produtos'][int(input_str)])
            print('Product deleted.')
        elif option.casefold() == "n".casefold():
            # not delete
            print("Nothing was deleted, going back to the start")
        else:
            print("error: invalid input")
            raise ValueError
    except:
        print("Opa")
        deleteProduto()

def main():
    print("Select an Option for Produto!")
    print("1 - Create")
    print("2 - Read")
    print("3 - Update")
    print("4 - Delete")
    print("0 - Quit")

    input_str = input()
    while input_str not in ["0", "1", "2", "3", "4"]:
        print("Not an valid option!")
        print("1 - Create")
        print("2 - Read")
        print("3 - Update")
        print("4 - Delete")
        input_str = input_str()

    if input_str == "1":
        createProduto()
        main()
    elif input_str == "2":
        showProdutos()
        main()
    elif input_str == "3":
        showProdutos()
        updateProduto()
        main()
    elif input_str == "4":
        showProdutos()
        deleteProduto()
        main()
    elif input_str == "0":
        exit()


memory = {
    "Produtos": []
}
main()
