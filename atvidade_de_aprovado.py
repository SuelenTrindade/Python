quantidade_alunos = int(input())


if quantidade_alunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")
else:

    soma_medias = 0


    for i in range(quantidade_alunos):
        media = float(input())
        soma_medias += media

        if media >= 6.0:
            print('PARABÉNS VOCÊ ESTÁ APROVADO')

    media_geral = soma_medias / quantidade_alunos
    print()