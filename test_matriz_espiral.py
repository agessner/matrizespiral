import unittest

from matriz_espiral import criar_matriz_populada_com_zeros


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