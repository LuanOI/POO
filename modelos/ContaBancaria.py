class ContaBancaria():
    def __init__(self, titular, saldo, ativo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self): #Metodo especial
        return f'{self._titular} | Saldo : R${self._saldo} | Ativo: {self._ativo}' 
    
titular = ContaBancaria ('Luan Oliveira', 4600, 'False')

print(titular)


@classmethod
def ativar_conta(cls, conta):
    conta._ativo = True

conta2 = ContaBancaria ('Carlos', 1000)
print(f"Antes de ativar: Conta ativa? {conta2._ativo}")
ContaBancaria.ativar_conta(conta2)
print(f"Depois de ativar: Conta ativa? {conta2._ativo}")

        