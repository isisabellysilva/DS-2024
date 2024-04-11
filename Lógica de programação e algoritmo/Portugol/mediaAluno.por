programa
{
	
	funcao inicio(){
	real nota_1
	real nota_2
	real nota_3 
	real resultado 
	
		escreva("digite a primeira nota: ")
		leia(nota_1)

		escreva("digite a segunda nota: ")
		leia(nota_2)

		escreva("digite a terceira  nota: ")
		leia(nota_3)

		resultado = (nota_1 + nota_2 + nota_3) / 3

		escreva("A soma dos números: ", resultado) 
		se (resultado >= 7) {

		escreva("\nAprovada :)")
	} senao se (resultado > 3 ){
          escreva("\nReprovada:(")
	} senao {
          escreva("\nRecuperação:(")
          
		}
	}

}
		

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 226; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */