programa{
	
	funcao inicio(){
		real tx, moeda, resultado 
	inteiro opcao 

	escreva("Como está a cotação do Dólar hoje?") 
	leia(tx)

	escreva("Escolha uma opção: \n") 
	escreva("[1] - Fazer a converção do Dólar para o Real \n")
	escreva("[2] - Fazer a converção do real para o Dólar \n") 
	escreva("Escolha uma opção para a converção: ") 
	leia(opcao)

	se(opcao == 1){
		escreva("Qual o valor em Dólar que será convertido para Real: ") 
		leia(moeda)
		resultado = moeda * tx
	} senao {
		escreva("Qual o valor em Real a ser convertido para Dólar: ")
		leia(moeda) 
		resultado = moeda / tx 
		
	}
	   escreva("O valor é: ", resultado) 
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 0; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */