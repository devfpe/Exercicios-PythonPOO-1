class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, preco: float):
        self._marca: str = marca
        self._modelo: str = modelo
        self._ano: str = ano
        self.preco: str = preco

    def __str__(self) -> str:
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Ano: {self._ano} | Preco: {self.preco} dabloons'
    
    def depreciacao_ano(self, ano_atual: int) -> float:
        idade_do_carro: float = ano_atual - self._ano
        valor_revenda: float = self.preco * (0.9 ** idade_do_carro)
        return valor_revenda


carro1 = Carro('Skibidi Toilet', 'Rizz', 2020, 69000)
print(carro1)
valor_revenda = carro1.depreciacao_ano(2024)
print(f'O valor de revenda do carro é: {valor_revenda}')