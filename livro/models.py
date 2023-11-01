from django.db import models

class Autor(models.Model): 

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()


    def __str__(self) -> str:
        return self.nome


class Editora(models.Model):

    nome = models.CharField(max_length=300)


    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):

    nome = models.CharField(max_length=300)
    categoria = models.CharField(max_length=30)
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    avaliacao = models.FloatField()
    autores = models.ManyToManyField(Autor, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name='livros')


    def __str__(self) -> str:
        return self.nome












