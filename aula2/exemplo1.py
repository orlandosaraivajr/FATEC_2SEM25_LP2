# s é um objeto do tipo string
s = 'oi mundo'

'''
Definindo as características e ações 
da classe Pessoa
'''
class Pessoa:
    # Atributos
    nome = None
    idade = None
    altura = None
    peso = None
    sexo = None
    # Método construtor: Método especial que executa assim que
    # o objeto é instanciado
    def  __init__(self):
        self.peso = 80
        self.altura = 1.70
    
    # Métodos
    def definir_nome(self, nome):
        self.nome = nome
    
    #Outro método
    def calcular_imc(self):
        if self.peso == None and self.altura == None:
            return "Deu ruim"
        imc = self.peso / (self.altura *self.altura )
        return imc
    
    
# Criando o objeto jose
jose = Pessoa()
jose.nome = "José da Silva"
jose.idade = 25

# Criando o objeto joao
joao = Pessoa()
joao.nome = "João da Silva"
joao.idade = 27

