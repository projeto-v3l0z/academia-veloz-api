from django.db import models

class Curso(models.Model):
    tipos_curso = [
        ('PUBLICO', 'Público'),
        ('PRIVADO', 'Privado'),
        ('IMERSAO', 'Imersão'),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=tipos_curso, default='PUBLICO')
    alunos = models.ManyToManyField('accounts.User', related_name='cursos', blank=True)
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
    tipos_aula = [
        ('TEXTO', 'Texto'),
        ('VIDEO', 'Vídeo'),
        ('ARQUIVO', 'Arquivo'),
    ]

    modulo = models.ForeignKey(Modulo, related_name='aulas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    tipo_conteudo = models.CharField(max_length=20, choices=tipos_aula, default='VIDEO')
    conteudo = models.TextField(blank=True, null=True)  
    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Matricula(models.Model):
    curso = models.ForeignKey(Curso, related_name='matriculas', on_delete=models.CASCADE)
    aluno = models.ForeignKey('accounts.User', related_name='matriculas', on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.curso} - {self.aluno}'
    
class AulaConcluida(models.Model):
    aula = models.ForeignKey(Aula, related_name='conclusoes', on_delete=models.CASCADE)
    aluno = models.ForeignKey('accounts.User', related_name='conclusoes', on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.aula} - {self.aluno}'
    
class ArquivoAula(models.Model):
    aula = models.ForeignKey(Aula, related_name='arquivos', on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='arquivos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.arquivo.name