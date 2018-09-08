def criar_matriz_populada_com_zeros(n_linhas, n_colunas):
	return [_criar_linha_populada_com_zeros(n_colunas) for linha in range(n_linhas)]


def _criar_linha_populada_com_zeros(n_colunas):
	return [0 for coluna in range(n_colunas)]


def criar_matriz_espiral(n_linhas, n_colunas):
	contador_inicial = 1
	indice_da_linha_inicial = 0
	posicao_inicial = 0
	limite = n_linhas * n_colunas

	matriz = criar_matriz_populada_com_zeros(n_linhas, n_colunas)
	_preencher_linha_da_esquerda_para_direita(
		matriz, 
		contador_inicial,
		indice_da_linha_inicial,
		posicao_inicial,
		limite
	)
	return matriz


def _preencher_linha_da_esquerda_para_direita(matriz, contador, indice_da_linha, posicao, limite):
	linha = matriz[indice_da_linha]
	for _ in linha:
		if not _coluna_ja_foi_preenchida(linha, posicao):
			matriz[indice_da_linha][posicao] = contador
			contador = contador + 1
			posicao = posicao + 1
		else:
			break

	if _matriz_nao_esta_completa(contador, limite) and _existe_promixa_linha(matriz, indice_da_linha):
		indice_da_coluna = posicao - 1
		if _deve_preencher_linha(matriz, indice_da_linha + 1, indice_da_coluna):
			_preencher_coluna_de_cima_para_baixo(matriz, indice_da_linha, indice_da_coluna, contador, posicao, limite)


def _preencher_coluna_de_cima_para_baixo(matriz, indice_da_linha_de_origem, indice_da_coluna, contador, posicao, limite):
	indice_da_ultima_linha_preenchida = indice_da_linha_de_origem
	for indice_da_linha, _ in enumerate(matriz):
		if indice_da_linha > indice_da_linha_de_origem:
			if _deve_preencher_linha(matriz, indice_da_linha, indice_da_coluna):
				matriz[indice_da_linha][indice_da_coluna] = contador
				contador = contador + 1
				indice_da_ultima_linha_preenchida = indice_da_ultima_linha_preenchida + 1

	if _matriz_nao_esta_completa(contador, limite):
		posicao = posicao - 2
		_preencher_linha_da_direita_para_esquerda(matriz, contador, indice_da_ultima_linha_preenchida, posicao, limite)


def _matriz_nao_esta_completa(contador_atual, limite_da_matriz):
	return contador_atual < limite_da_matriz + 1


def _proximo_elemento_ja_foi_preenchido(array, posicao):
	return len(array) > posicao and array[posicao] != 0


def _ultimo_valor_da_linha_ja_foi_preenchido(linha):
	return linha[len(linha) - 1] != 0


def _existe_promixa_linha(matriz, indice_da_linha):
	return len(matriz) > indice_da_linha + 1


def _deve_preencher_linha(matriz, indice_da_linha, indice_da_coluna):
	return matriz[indice_da_linha][indice_da_coluna] == 0 


def _deve_preencher_proxima_linha(matriz, indice_da_linha, indice_da_coluna):
	if _existe_promixa_linha(matriz, indice_da_linha):
		return matriz[indice_da_linha + 1][indice_da_coluna] == 0 
	return False


def _preencher_linha_da_direita_para_esquerda(matriz, contador, indice_da_linha, posicao, limite):
	linha = matriz[indice_da_linha]
	for _ in linha:
		if posicao < 0 or _coluna_ja_foi_preenchida(linha, posicao):
			break
		matriz[indice_da_linha][posicao] = contador
		contador = contador + 1
		posicao = posicao - 1

	if _matriz_nao_esta_completa(contador, limite):
		indice_da_coluna = posicao + 1
		_preencher_coluna_de_baixo_para_cima(matriz, indice_da_linha, indice_da_coluna, contador, posicao, limite)	


def _coluna_ja_foi_preenchida(array, posicao):
	return posicao >= 0 and array[posicao] != 0


def _preencher_coluna_de_baixo_para_cima(matriz, indice_da_linha_de_origem, indice_da_coluna, contador, posicao, limite):
	indice_da_linha = indice_da_linha_de_origem
	indice_da_ultima_linha_preenchida = indice_da_linha_de_origem
	while _deve_preencher_linha_anterior(matriz, indice_da_linha, indice_da_coluna) == True:
		indice_da_linha = indice_da_linha - 1
		if indice_da_linha < indice_da_linha_de_origem:
			if _deve_preencher_linha(matriz, indice_da_linha, indice_da_coluna):
				matriz[indice_da_linha][indice_da_coluna] = contador
				contador = contador + 1
				indice_da_ultima_linha_preenchida = indice_da_ultima_linha_preenchida - 1
	
	if _matriz_nao_esta_completa(contador, limite):
		_preencher_linha_da_esquerda_para_direita(
			matriz, 
			contador,
			indice_da_ultima_linha_preenchida,
			posicao + 2,
			limite
		)


def _deve_preencher_linha_anterior(matriz, indice_da_linha, indice_da_coluna):
	return matriz[indice_da_linha - 1][indice_da_coluna] == 0 