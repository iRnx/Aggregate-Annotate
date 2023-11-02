from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.aggregates import Avg, Sum, Count, Min, Max
from django.db.models import F, Sum
from django.db.models import Prefetch

from .models import Autor, Editora, Livro


def aggregate_annotate(request):

    # Topico 1: Aggregate() é utilizado de forma Global, quando voce quer pegar toda uma coluna e fazer alguma operação. e retorna um dicionario. #
    # A média de preços de todos os livros com Aggregate. #

    # precoh_medio = Livro.objects.all().aggregate(preco_medio=Avg('preco'))
    # print(f'{precoh_medio["preco_medio"]:.2f}')

    # avalicao_medio = Livro.objects.all().aggregate(avaliacao_media=Avg('avaliacao'))
    # print(f'{avalicao_medio["avaliacao_media"]:.2f}')

    # avalicao_precoh = Livro.objects.all().aggregate(avaliacao_media=Avg('avaliacao'), precoh_medio=Avg('preco'))
    # print(f'Avaliação media: {avalicao_precoh["avaliacao_media"]:.2f}, Preco Médio: {avalicao_precoh["precoh_medio"]}')
    # print()

    # mais_caro_avaliacao_e_preco_medio = Livro.objects.aggregate(mais_caro=Max('preco'), avaliacao_media=Avg('avaliacao'), preco_medio=Avg('preco'))
    # print(f'Avaliação media: {mais_caro_avaliacao_e_preco_medio["avaliacao_media"]:.2f}\nPreco Médio: {mais_caro_avaliacao_e_preco_medio["preco_medio"]:.3f}\nLivro mais caro: {mais_caro_avaliacao_e_preco_medio["mais_caro"]:.2f}')

    # preco_e_avaliacao_de_uma_categoria = Livro.objects.filter(categoria__icontains='Fantasia').aggregate(preco_medio=Avg('preco'), avaliacao_media=Avg('avaliacao'))
    # print(f'Avaliação media: {preco_e_avaliacao_de_uma_categoria["avaliacao_media"]:.2f}, Preco Médio: {preco_e_avaliacao_de_uma_categoria["preco_medio"]:.3f}')


    # # Topico 2: Agora vamos falar sobre o annotate() #
    # # A média das notas dos livros de cada autor #

    # autores = Autor.objects.all().annotate(nota_media=Avg('livros__avaliacao'))
    # for autor in autores:
    #     print(f'Nome: {autor.nome} - Nota Média: {autor.nota_media}')


    # autores = Autor.objects.filter(idade__gt=40).annotate(nota_media=Avg('livros__avaliacao'))
    
    # for autor in autores:
    #     print(f'Nome: {autor.nome} - Nota Média: {autor.nota_media}')
    

    # # Topico 3: Annotate com group by que no django é representado pelo values() #
    # # A média das notas dos livros agrupados por categoria #

    # livros = Livro.objects.values('categoria').annotate(nota_media=Avg('avaliacao'))
    # for livro in livros:
    #     print(livro)

    # teste = Livro.objects.annotate(number=Count('autores'))

    # for v in teste:
    
    #     print(v.number, v.nome)



    # Defina um Prefetch para os autores de cada livro

    livros_com_autores = Livro.objects.values('nome', 'autores').prefetch_related(
        # 'autores'
        Prefetch('autores', queryset=Autor.objects.only('nome'))
    )

    print(livros_com_autores)

    # Busque os livros e os nomes dos autores
    livros = livros_com_autores.values_list('nome', 'autores__nome')
    print(livros)


    # Crie um dicionário para agrupar os autores por livro
    livros_autores = {}
    for livro, autor in livros:
        if livro not in livros_autores:
            livros_autores[livro] = []
        livros_autores[livro].append(autor)



    # Itere sobre os resultados e imprima os nomes dos autores concatenados
    # for livro, autores in livros_autores.items():
    #     autores_concatenados = ", ".join(autores)
    #     print(f"Livro: {livro}")
    #     print(f"Autores: {autores_concatenados}")

    contexto = {
        'livros_autores': livros_autores  # Esta é a variável que contém os dados
    }

    return render(request, 'seu_template.html', contexto)













