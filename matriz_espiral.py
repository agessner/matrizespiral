def criar_matriz_espiral(n_linhas, n_colunas):
	matriz = criar_matriz_populada_com_zeros(n_linhas, n_colunas)
	return matriz


def criar_matriz_populada_com_zeros(n_linhas, n_colunas):
	return [_criar_linha_populada_com_zeros(n_colunas) for linha in range(n_linhas)]


def _criar_linha_populada_com_zeros(n_colunas):
	return [0 for coluna in range(n_colunas)]
