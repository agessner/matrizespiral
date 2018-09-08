import unittest

from matriz_espiral import criar_matriz_populada_com_zeros, criar_matriz_espiral


class CriarMatrizPopuladaComZerosTests(unittest.TestCase):
	def test_retorna_uma_linha_com_o_numero_de_colunas_informado(self):
		n_linhas = 1
		n_colunas = 5

		resultado = criar_matriz_populada_com_zeros(n_linhas, n_colunas)

		esperado = [[0, 0, 0, 0, 0]]
		self.assertEqual(esperado, resultado)
	

	def test_retorna_multiplas_linhas_com_o_numero_de_colunas_informado(self):
		n_linhas = 5
		n_colunas = 5

		resultado = criar_matriz_populada_com_zeros(n_linhas, n_colunas)

		esperado = [
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0]
		]
		self.assertEqual(esperado, resultado)


class CriarMatrizEspiralTests(unittest.TestCase):
	def test_cria_matriz_espiral_com_uma_linha(self):
		n_linhas = 1
		n_colunas = 5

		resultado = criar_matriz_espiral(n_linhas, n_colunas)

		esperado = [
			[1, 2, 3, 4, 5]
		]
		self.assertEqual(esperado, resultado)

	def test_cria_matriz_espiral_com_duas_linhas(self):
		n_linhas = 2
		n_colunas = 5

		resultado = criar_matriz_espiral(n_linhas, n_colunas)

		esperado = [
			[1,  2, 3, 4, 5],
			[10, 9, 8, 7, 6]
		]
		self.assertEqual(esperado, resultado)

	def test_cria_matriz_espiral_com_cinco_linhas(self):
		n_linhas = 5
		n_colunas = 5

		resultado = criar_matriz_espiral(n_linhas, n_colunas)

		esperado = [
			[1,  2,  3,  4,  5],
			[16, 17, 18, 19, 6],
			[15, 24, 25, 20, 7],
			[14, 23, 22, 21, 8],
			[13, 12, 11, 10, 9]
		]
		self.assertEqual(esperado, resultado)