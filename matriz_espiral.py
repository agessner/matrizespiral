def criar_matriz_populada_com_zeros(n_linhas, n_colunas):
	return [_criar_linha_populada_com_zeros(n_colunas) for linha in range(n_linhas)]


def _criar_linha_populada_com_zeros(n_colunas):
	return [0 for coluna in range(n_colunas)]


class MatrizEspiral(object):
	def __init__(self, numero_de_linhas, numero_de_colunas):
		self._numero_de_linhas = numero_de_linhas
		self._numero_de_colunas = numero_de_colunas
		self._indice_da_linha = 0
		self._indice_da_coluna = 0
		self._contador = 1
		self._ultimo_numero_possivel_do_contador = numero_de_linhas * numero_de_colunas
		self._matriz = criar_matriz_populada_com_zeros(numero_de_linhas, numero_de_colunas)

	def executar(self):
		while self._matriz_nao_esta_completa():
			self._preencher_linha_da_esquerda_para_direita()
			self._ir_para_proxima_linha()
			self._preencher_coluna_de_cima_para_baixo()
			self._voltar_para_coluna_anterior()
			self._preencher_linha_da_direita_para_esquerda()
			self._voltar_para_linha_anterior()
			self._preencher_coluna_de_baixo_para_cima()
			self._ir_para_proxima_coluna()
		return self._matriz
	
	def _matriz_nao_esta_completa(self):
		return self._contador < self._ultimo_numero_possivel_do_contador + 1
		
	def _preencher_linha_da_esquerda_para_direita(self):
		while self._existe_coluna() and self._deve_preencher_celula():
			self._preencher_celula()
			self._indice_da_coluna = self._indice_da_coluna + 1

		self._indice_da_coluna = self._indice_da_coluna - 1
	
	def _preencher_coluna_de_cima_para_baixo(self):
		while self._existe_linha() and self._deve_preencher_celula():
			self._preencher_celula()
			self._indice_da_linha = self._indice_da_linha + 1
		
		self._indice_da_linha = self._indice_da_linha - 1

	def _preencher_linha_da_direita_para_esquerda(self):
		while self._existe_coluna() and self._deve_preencher_celula():
			self._preencher_celula()
			self._indice_da_coluna = self._indice_da_coluna - 1

		self._indice_da_coluna = self._indice_da_coluna + 1

	def _preencher_coluna_de_baixo_para_cima(self):
		while self._existe_linha() and self._deve_preencher_celula():
			self._preencher_celula()
			self._indice_da_linha = self._indice_da_linha - 1
			
		self._indice_da_linha = self._indice_da_linha + 1

	def _ir_para_proxima_linha(self):
		self._indice_da_linha = self._indice_da_linha + 1

	def _ir_para_proxima_coluna(self):
		self._indice_da_coluna = self._indice_da_coluna + 1

	def _voltar_para_linha_anterior(self):
		self._indice_da_linha = self._indice_da_linha - 1

	def _voltar_para_coluna_anterior(self):
		self._indice_da_coluna = self._indice_da_coluna - 1

	def _existe_coluna(self):
		return len(self._matriz[self._indice_da_linha]) > self._indice_da_coluna \
			and self._indice_da_coluna >= 0
	
	def _existe_linha(self):
		return len(self._matriz) > self._indice_da_linha \
			and self._indice_da_linha >= 0

	def _deve_preencher_celula(self):
		return self._matriz[self._indice_da_linha][self._indice_da_coluna] == 0

	def _preencher_celula(self):
		self._matriz[self._indice_da_linha][self._indice_da_coluna] = self._contador
		self._contador = self._contador + 1
