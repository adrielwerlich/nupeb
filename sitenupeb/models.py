from embed_video.fields import EmbedVideoField
from datetime import timedelta
from django_countries.fields import CountryField
from django.db import models
from datetime import datetime

################ MODELOS DE TEMPO ########################
class Periodo(models.Model):
    dataInicial = models.DateField(blank=True, default=datetime.now)
    dataFinal = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
      if self.dataInicial==None or self.dataFinal==None: 
        print('periodo none type ***********')
        return "ERROR-PERIODO NULL"
        
      return \
					str('Data Início: ' + str(self.dataInicial.strftime('%e %b %Y')) + \
				  '. Data Final: ' + str(self.dataFinal.strftime('%e %b %Y'))) \
					if self.dataInicial and self.dataFinal else 'periodo vazio'


class Ano(models.Model):
    ano = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
      if self.ano==None: 
        print('ano none type ***********')
        return "ERROR-ANO NULL"
			
      return str(self.ano.strftime('%b %e %Y')) if self.ano else 'ano'
				
          

################ MODELOS ATIVIDADES ########################
class AtividadesPorAno(models.Model):
    tituloDaAtividade = models.CharField(
        max_length=400, help_text='Título Atividade')
    ano = models.ForeignKey(Ano, related_name='anoDaAtividade', null=True, on_delete=models.SET_NULL,
                            help_text='ano vigente da atividade')
    dataAtividade = models.DateTimeField(
        null=True, blank=True, default=datetime.now)
    local = models.CharField(max_length=1200)
    descricao = models.TextField()
    periodo = models.ForeignKey(Periodo, related_name='periodoDaAtividade', null=True,
                                on_delete=models.SET_NULL, help_text='periodo vigente da atividade')

    def __str__(self):
        return self.tituloDaAtividade


class FotosDasAtividades(models.Model):
    atividade = models.ForeignKey(AtividadesPorAno, related_name='fotosDasAtividades',
                                  null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='fotos-das-atividades/')
    comentario = models.CharField(
        max_length=1200, blank=True, help_text='comentário o contexto da foto')

    def __str__(self):
        return self.atividade.tituloDaAtividade
				
    class Meta:
        verbose_name = "FotosDasAtividades"
        verbose_name_plural = "Fotos Das Atividades"

################# OBJETIVOS E LINHA DE PESQUISA - TELA INICIAL - APRESENTAÇÃO ###########################
class Objetivos(models.Model):
    objetivos = models.TextField(help_text='descrição dos objetivos do grupo')

    def __str__(self):
        return self.objetivos
				
    class Meta:
		    verbose_name = "Objetivos"
		    verbose_name_plural = "Objetivos"		


class LinhaDePesquisa(models.Model):
    # tituloLinha: models.CharField(max_length=800, verbose_name='Título da linha de pesquisa')
    # descricao: models.TextField(max_length=8000)
    nomeDaLinha = models.CharField(max_length=1200, null=True, blank=True, verbose_name='Título da linha de pesquisa')
    detalhes = models.TextField(max_length=12000, null=True, blank=True)
    def __str__(self):
        return self.nomeDaLinha
    class Meta:
		    verbose_name = "Linha de Pesquisa"
		    verbose_name_plural = "Linhas de Pesquisa"		

				
################## EVENTOS CINE DEBATE #################################3				
class CineDebate(models.Model):
    ano = models.ForeignKey(Ano, related_name='anoDoEvento',
                            null=True, on_delete=models.SET_NULL)
    periodo = models.ForeignKey(
        Periodo, related_name='periodoDosCineDebates', null=True, on_delete=models.SET_NULL)
    descricao = models.CharField(max_length=600)
    proximoFilme = models.ImageField(help_text="logo do próximo filme",
        upload_to='imagens-cinedebate', null=True, blank=True)

    #def __str__(self):
      #if self.descricao == None:
         # return "ERROR-CINEDEBATE NULL"
					
			
      #return str(self.descricao) if self.descricao else ''


class Filmes(models.Model):
    data = models.DateField(blank=True, default=datetime.now)
    titulo = models.CharField(max_length=400, blank=True, null=True)
    cinedebate = models.ForeignKey(
        CineDebate, related_name='cinedebate', null=True, on_delete=models.SET_NULL, blank=True)

    class Meta:
        verbose_name = "Filmes"
        verbose_name_plural = "Filmes"

    def __str__(self):
        return self.titulo

    def dataFormatada(self):
        return self.data.strftime('%d/%m/%Y')


class ProximoFilme(models.Model):
    sessao = models.ForeignKey(
        CineDebate, related_name='sessao', null=True, on_delete=models.CASCADE)
    filme = models.ForeignKey(
        Filmes, related_name='filme', null=True, on_delete=models.CASCADE)


class InformacoesTecnicas(models.Model):
    direcao = models.CharField(max_length=500)
    ano = models.DateField(blank=True, default=datetime.now)
    pais = CountryField()
    duracao = models.DurationField(blank=True, default=timedelta)
    filme = models.OneToOneField(Filmes, null=True, on_delete=models.CASCADE)

    def anoFormatado(self):
        return self.ano.strftime('%Y')
				
    class Meta:
		    verbose_name = "Informações Técnicas"
		    verbose_name_plural = "Informações Técnicas"		
		


class LocalExibicao(models.Model):
    local = models.CharField(max_length=250)
    # horarioDaExibicao = models.ForeignKey(Filmes, related_name='filmeExibido', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.local


class HorarioExibicao(models.Model):
    horario = models.TimeField(blank=True)
    filme = models.ForeignKey(Filmes, related_name='filmeAserExibido',
                              null=True, blank=True, on_delete=models.CASCADE)
    localExibicao = models.ForeignKey(LocalExibicao, related_name='localDaExibicao', blank=True,
                                      null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.horario.strftime('%H:%M')
				
    class Meta:
		    verbose_name = "Horário Exibicao"
		    verbose_name_plural = "Horários de Exibicao"		


class EventosCineDebate(models.Model):
    cine = models.ForeignKey(CineDebate, default=None, blank=True,
                             related_name='cineDebate', on_delete=models.CASCADE)
    tituloDaExibicao = models.CharField(max_length=800, blank=True)
    data = models.DateTimeField(
        null=True, blank=True, default=datetime.now, help_text='data do evento')
    logo = models.ImageField(
        upload_to='imagens-cinedebate', null=True, blank=True)
    local = models.ForeignKey(LocalExibicao, default=None, blank=True,
                              related_name='localExibicao', null=True, on_delete=models.SET_NULL)
    endereco = models.CharField(max_length=800, blank=True)

    def dataFormatada(self):
        return self.data.strftime('Data : %d/%m/%Y - Horário - %H:%M')
				
    class Meta:
		    verbose_name = 'EventosCineDebate'
		    verbose_name_plural = 'Eventos CineDebate'


class VideoTrailer(models.Model):
    # linkDoVideo = models.CharField(max_length=3200,blank=True, null=True)
    # link = models.URLField(blank=True, null=True)
    evento = models.ForeignKey(EventosCineDebate, related_name='eventoDoLink',
                               blank=True, null=True, on_delete=models.CASCADE)
    video = EmbedVideoField(verbose_name='Link do Video', max_length=5000, default=None, null=True, blank=True,
                            help_text='Geralmente é um trailer ou apresentação do vídeo')

    def __unicode__(self):
        return self.tituloDaExibicao

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})


class FotosDoCineDebate(models.Model):
    images = models.ImageField(upload_to='imagens-cinedebate')
    cinedebate = models.ForeignKey(EventosCineDebate, related_name='imagensDoCineDebate', null=True,
                                   blank=True, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=300, null=True, blank=True)

########################## PESQUISADORES E INTEGRANTES ########################
class Pesquisador(models.Model):
    nomeAmostrar = models.CharField(max_length=300, verbose_name='Nome a mostrar')
    curriculo = models.URLField(
        blank=True, null=True, help_text='link do lattes')
    def __str__(self):
        return self.nomeAmostrar
    

class Integrante(models.Model):
    nomeAmostrar = models.CharField(max_length=300, verbose_name='Nome a mostrar')
    def __str__(self):
        return self.nomeAmostrar

class Egresso(models.Model):
    nomeAmostrar = models.CharField(max_length=300, verbose_name='Nome a mostrar')
    def __str__(self):
        return self.nomeAmostrar
		
############### DOCUMENTOS ######################

class DocumentosInternacionais(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link do documento')
	def __str__(self):
	    return self.titulo
		
		
	class Meta:
		  verbose_name = "DocumentosInternacionais"
		  verbose_name_plural = "Documentos Internacionais"

		
class DocumentosNacionais(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)		
	link = models.URLField(blank=True, null=True, help_text='link do documento')
	
	def __str__(self):
	    return self.titulo
			
	class Meta:
		  verbose_name = "DocumentosNacionais"
		  verbose_name_plural = "Documentos Nacionais"

	
class SubDocumento(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link do sub-documento')
	documentoPai = models.ForeignKey(DocumentosNacionais, blank=True, null=True,
		help_text='link do sub-documento', on_delete=models.CASCADE)	
	
	def __str__(self):
	    return self.titulo
		
class Publicacoes(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link da publicação')
	
	def __str__(self):
		return self.titulo
		
	class Meta:
		  verbose_name = "Publicacoes"
		  verbose_name_plural = "Publicacoes"
		
class LegislacaoNacional(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link do documento')
	
	def __str__(self):
		return self.titulo
		
	class Meta:
		  verbose_name = "LegislacaoNacional"
		  verbose_name_plural = "Legislacao Nacional"	
			
class DocumentosEstaduais(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link do documento')	
	
	def __str__(self):
		return self.titulo
		
	class Meta:
		  verbose_name = "DocumentosEstaduais"
		  verbose_name_plural = "Documentos Estaduais"
		
		
class LegislacaoEstadual(models.Model):
	titulo = models.CharField(max_length=1500, null=True, blank=True)
	descricao = models.CharField(max_length=1500, null=True, blank=True)
	link = models.URLField(blank=True, null=True, help_text='link do documento')		
	
	def __str__(self):
		return self.titulo
		
	class Meta:
		  verbose_name = "LegislacaoEstadual"
		  verbose_name_plural = "Legislacao Estadual"
		
##################### EVENTOS #####################		

class Eventos(models.Model):	
		titulo = models.CharField(max_length=890, null=True, blank=True)
		realizacao = models.CharField(max_length=890, null=True, blank=True)
		local = models.CharField(max_length=890, null=True, blank=True)
		participacao = models.CharField(max_length=1290, null=True, blank=True)
		data = models.DateField(null=True, blank=True, help_text='data do evento')
		horario = models.CharField(max_length=100, null=True, blank=True)
		adicionais = models.TextField(null=True, blank=True, help_text="informações adicionais. Pode ser editado com html")
		
		class Meta:
			verbose_name = "Eventos"
			verbose_name_plural = "Eventos"

		def __str__(self):
				return self.titulo
		
		def dataFormatada(self):
			if (self.data != None):
					return self.data.strftime('%d/%m/%Y')
			else:
					return "sem data cadastrada"
				
				
  			
#	def dataFormatada(self):
 #       return self.data.strftime('%d/%m/%Y')
	
class ParticipanteEvento(models.Model):
		nome = models.CharField(max_length=490, null=True, blank=True)
		evento = models.ForeignKey(Eventos, related_name='participantesDoEvento', null=True,
                                   blank=True, on_delete=models.CASCADE)
		
class FotosEvento(models.Model):
		foto = models.ImageField(upload_to='fotos-dos-eventos/')
		comentario = models.CharField(max_length=1290, null=True, blank=True)
		evento = models.ForeignKey(Eventos, related_name='fotosDoEvento', null=True,
                                   blank=True, on_delete=models.CASCADE)
		
#################### LISTA DE FILMES #########################

class TemaFilme(models.Model):		
    tema = models.CharField(max_length=5000, null=True, blank=True, help_text='tema do filme')
    comentario = models.CharField(max_length=15000, null=True, blank=True, help_text='comentário sobre o contexto')
    def __str__(self):
		    return self.tema
		
class FilmePorTema(models.Model):
    titulo = models.CharField(max_length=5000, null=True, blank=True, help_text='titulo/descrição do filme')
    link = models.URLField(blank=True, null=True, help_text='link do filme')
    tema = models.ForeignKey(TemaFilme, related_name='temaDofilme', 
										 null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
		
#################### LISTA DE LEITURAS #########################		
		
class TemaLeitura(models.Model):		
    tema = models.CharField(max_length=5000, null=True, blank=True, help_text='tema da leitura')
    comentario = models.CharField(max_length=15000, null=True, blank=True, help_text='comentário sobre o contexto')
    def __str__(self):
		    return self.tema
		
class LeituraPorTema(models.Model):
    titulo = models.CharField(max_length=5000, null=True, blank=True, help_text='titulo/descrição da leitura')
    link = models.URLField(blank=True, null=True, help_text='link da leitura')
    tema = models.ForeignKey(TemaLeitura, related_name='temaDaleitura', 
										 null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
				
    class Meta:
		    verbose_name = "LeituraPorTema"
		    verbose_name_plural = "Leituras por Tema"

####################### MATERIAL DIDÁTICO #######################

class MaterialDidatico(models.Model): 
    titulo = models.CharField(max_length=5000, null=True, blank=True, help_text='contexto do material didático')
		
    def __str__(self):
        return self.titulo
				
class DescricaoMaterialDidatico(models.Model):		
    descricao = models.CharField(max_length=5000, null=True, blank=True, help_text='descrição e temas do material didático')
    link = models.URLField(blank=True, null=True, help_text='link do material didático')
    material = models.ForeignKey(MaterialDidatico, related_name='descricaoDoMaterialDidatico', 
										 null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao
		
####################### PESQUISAS #######################

class PesquisasEmAndamento(models.Model): 
    titulo = models.CharField(max_length=500, null=True, blank=True, help_text='título da pesquisa')
    aluno = models.CharField(max_length=500, null=True, blank=True, help_text='aluno da pesquisa')
    modalidade = models.CharField(max_length=500, null=True, blank=True, help_text='tipo da pesquisa')
    periodo = models.CharField(max_length=500, null=True, blank=True, help_text='periodo da pesquisa')
		
    def __str__(self):
        return self.titulo
				
    class Meta:
        verbose_name = "PesquisasEmAndamento"
        verbose_name_plural = "Pesquisas em Andamento"		
				
class PesquisasRealizadas(models.Model):		
    titulo = models.CharField(max_length=500, null=True, blank=True, help_text='título da pesquisa')
    aluno = models.CharField(max_length=500, null=True, blank=True, help_text='aluno da pesquisa')
    modalidade = models.CharField(max_length=500, null=True, blank=True, help_text='tipo da pesquisa')
    periodo = models.CharField(max_length=500, null=True, blank=True, help_text='periodo da pesquisa')
            
    def __str__(self):
        return self.titulo		
		
    class Meta:
        verbose_name = "PesquisasRealizadas"
        verbose_name_plural = "Pesquisas Realizadas"
		
#################### PPGE #######################

class Ppge(models.Model):
    descricao = models.CharField(max_length=1500, null=True, blank=True, help_text='descrição do mestrado')
    rodape = models.CharField(max_length=1500, null=True, blank=True, help_text='descrição do mestrado')
    areadeconcentracao = models.CharField(max_length=100, null=True, blank=True, help_text='área de concentração',
		    verbose_name="Área de concentração")
    def __str__(self):
        return self.descricao
				
class LinhaPpge(models.Model):
    nome =   models.CharField(max_length=500, null=True, blank=True, help_text='descrição da linha')
    descricao = models.CharField(max_length=500, null=True, blank=True, help_text='descrição da linha')
		
    def __str__(self):
        return self.nome
				
class DocentesPpge(models.Model):
    nome = models.CharField(max_length=500, null=True, blank=True, help_text='nome do docente')
    linha = models.ForeignKey(LinhaPpge, related_name='linhaPpge', blank=True, null=True, 
                            on_delete=models.CASCADE, help_text='linha do docente')
    def __str__(self):
        return self.nome
				
class ContatoPpge(models.Model):
    link = models.URLField(blank=True, null=True, help_text='link do mestrado')
    linkFace = models.URLField(blank=True, null=True, help_text='link do mestrado no face')
    telefone = models.CharField(max_length=500, null=True, blank=True, help_text='telefone contato mestrado')
		
    def __str__(self):
        return "Contato PPGE"
		
class EmailPpge(models.Model):		
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True, default=None)
    # protect the db from saving any blank fields (from admin or your app form)
    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == "":
            self.email = None
        models.Model.save(self, *args, **kwargs)	

    def __str__(self):
        return self.email
		
		
####################  PRODUÇÃO  ##################
		

class RefereciaCita(models.Model):
    titulo = models.CharField(max_length=500, null=True, blank=True, help_text='título da pesquisa')
    link = models.URLField(blank=True, null=True, help_text='link da pesquisa')
    #pesquisador = models.ForeignKey('AutorPesquisa',null=True, blank=True, 
		    #help_text='pesquisadores que participam da pesquisa', on_delete=models.SET_NULL)
    pesq = models.ManyToManyField('AutoresPesq', related_name='autoresDaPesquisa',through='AutorRef', verbose_name='pesquisador')		
    def __str__(self):
        return self.titulo
    class Meta:
		    verbose_name = "Referência bibliográfica"
		    verbose_name_plural = "Referências bibliográficas"
				
class AutoresPesq(models.Model):
    nome = models.CharField(max_length=500, null=True, blank=True, help_text='nome do pesquisador')
    link = models.URLField(blank=True, null=True, help_text='link do currículo do pesquisador')
    pesquisa = models.ManyToManyField('RefereciaCita', through='AutorRef', verbose_name='pesquisador',
        related_name='pesquisaDoAutor', help_text='pesquisa que o autor participa')
		
    def __str__(self):
        return self.nome
    class Meta:
		    verbose_name = "Autores Pesquisa"
		    verbose_name_plural = "Autores Pesquisa"

class AutorRef(models.Model):
    pesquisa = models.ForeignKey(RefereciaCita, null=True, related_name='pesquisarn',
		    help_text='pesquisa que o autor participa', on_delete=models.CASCADE)
    pesquisador = models.ForeignKey(AutoresPesq, null=True, related_name='autorDaPesquisa',
  	    help_text='pesquisadores que participam da pesquisa', on_delete=models.CASCADE)
		
    def __str__(self):
        return self.pesquisador.nome + ", " + self.pesquisa.titulo[:100]
		
    class Meta:
		    verbose_name = "Autor Pesquisa"
		    verbose_name_plural = "Autor Pesquisa"