from django.db import models


class TipoCurso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Tipo_Curso(models.TextChoices):
    PUBLICO = 'Público', 'Público'
    ASSINATURA = 'Assinatura', 'Assinatura'
    IMERSAO = 'Imersão', 'Imersão'



class Curso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TipoCurso.choices, default=Tipo_Curso.PUBLICO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    class TipoConteudo(models.TextChoices):
        VIDEO = 'Vídeo', 'Vídeo'
        TEXTO = 'Texto', 'Texto'
        ARQUIVO = 'Arquivo', 'Arquivo'

    modulo = models.ForeignKey(Modulo, related_name='aulas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    tipo_conteudo = models.CharField(max_length=20, choices=TipoConteudo.choices, default=TipoConteudo.TEXTO)
    conteudo = models.TextField(blank=True, null=True)  
    arquivo = models.FileField(upload_to='aulas/', blank=True, null=True)

    def __str__(self):
        return self.titulo