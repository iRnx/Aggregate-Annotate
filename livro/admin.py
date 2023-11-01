from django.contrib import admin
from .models import Autor, Editora, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade')


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'paginas', 'preco', 'avaliacao', 'autoress')

    def autoress(self, obj):
        return [autor.nome for autor in obj.autores.all()]
