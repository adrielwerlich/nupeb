from django.utils.html import  format_html
from django.contrib import admin
from .models import *

# os últimos adicionados vão empilhando acima, estilo lifo/stack


##################### FILMES POR TEMA ABAIXO #####################	

class FilmePorTemaInline(admin.StackedInline):
    model = FilmePorTema

class TemaFilmeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tema do filme', {'fields': ['tema']}),
				('Comentários sobre o tema/contexto', {'fields': ['comentario']}),
    ]
    inlines = [FilmePorTemaInline]
    list_filter = ['tema']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/temafilme/{}/delete/">Delete</a>', obj.id)

##################### FILMES POR TEMA ABAIXO #####################
	
##################### EVENTOS ABAIXO #####################	
class FotosEventoInline(admin.TabularInline):
    model = FotosEvento
    extra = 2

class ParticipantesEventoInline(admin.TabularInline):
    model = ParticipanteEvento
	
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo','realizacao','local', 'data','delete_button')
    fieldsets = [
        ('Título do evento', {'fields': ['titulo']}),
				('Quem promoveu o evento?', {'fields': ['realizacao']}),
        ('Local do evento', {'fields': ['local']}),
				('Qual atividade realizada?', {'fields': ['participacao']}),
				('Data do evento', {'fields': ['data']}),
				('Horário do evento', {'fields': ['horario']}),
				('Informações adicionais - evento', {'fields': ['adicionais']}),
    ]
    inlines = [ParticipantesEventoInline,FotosEventoInline]
    search_fields = ['titulo','realizacao','local','data']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/eventos/{}/delete/">Delete</a>', obj.id)
##################### ACIMA EVENTOS #####################	
#################### ABAIXO DOCUMENTAÇÃO #############################
class LegislacaoEstadualAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
		('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link', {'fields': ['link']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/legislacaoestadual/{}/delete/">Delete</a>', obj.id)

class DocEstaduaisAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
		('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link', {'fields': ['link']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/documentosestaduais/{}/delete/">Delete</a>', obj.id)

class LegislacaoNacionalAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
		('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link', {'fields': ['link']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/legislacaonacional/{}/delete/">Delete</a>', obj.id)
		

class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
		('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link', {'fields': ['link']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/publicacoes/{}/delete/">Delete</a>', obj.id)
	

class SubDocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo','link','documentoPai','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
        ('Link', {'fields': ['link']}),
	    ('Vinculado ao documento', {'fields': ['documentoPai']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/subdocumento/{}/delete/">Delete</a>', obj.id)
		
class SubDocumentoInline(admin.TabularInline):
	model = SubDocumento	
	
class DocsNacionaisAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
        ('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link para o documento', {'fields': ['link']}),
    ]
    inlines = [SubDocumentoInline]
    search_fields = ['titulo','descricao']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/documentosnacionais/{}/delete/">Delete</a>', obj.id)


class DocsInternacionaisAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','link','delete_button')
    fieldsets = [
        ('Nome do documento', {'fields': ['titulo']}),
        ('Detalhes e descrição', {'fields': ['descricao']}),
        ('Link', {'fields': ['link']}),
    ]
    search_fields = ['titulo','descricao','link']
    def delete_button(self, obj):
	    return format_html('<a class="btn" href="/admin/sitenupeb/documentosinternacionais/{}/delete/">Delete</a>', obj.id)

#################### DOCUMENTAÇÃO ACIMA #############################




class LinhaDePesquisaAdmin(admin.ModelAdmin):    
    # list_display = ('Título da linha de pesquisa','descricao')  
    # fieldsets = [
    #     ('Nome da linha de pesquisa', {'fields': ['tituloLinha']}),
    #     ('Descrição da linha de pesquisa', {'fields': ['descricao']}),
    # ]
    # search_fields = ['titulo']
    # list_filter = ['nomeAmostrar']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/linhadepesquisa/{}/delete/">Delete</a>', obj.id)    

class EgressoAdmin(admin.ModelAdmin):    
    # list_display = ('nomeAmostrar')  
    fieldsets = [
        ('Identificação do Pesquisador', {'fields': ['nomeAmostrar']}),
    ]
    search_fields = ['nomeAmostrar']
    list_filter = ['nomeAmostrar']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/egresso/{}/delete/">Delete</a>', obj.id)


class IntegranteAdmin(admin.ModelAdmin):    
    # list_display = ('nomeAmostrar')  
    fieldsets = [
        ('Identificação do Integrante', {'fields': ['nomeAmostrar']}),
    ]
    search_fields = ['nomeAmostrar']
    list_filter = ['nomeAmostrar']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/integrante/{}/delete/">Delete</a>', obj.id)

class PesquisadorAdmin(admin.ModelAdmin):    
    list_display = ('nomeAmostrar','curriculo')  
    fieldsets = [
        ('Identificação do Pesquisador', {'fields': ['nomeAmostrar']}),
        ('Link do currículo no lattes', {'fields': ['curriculo']}),
    ]
    search_fields = ['nomeAmostrar']
    list_filter = ['nomeAmostrar']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/pesquisador/{}/delete/">Delete</a>', obj.id)

class IframesLinksInline(admin.StackedInline):
    model = IframesLinks

class ImagensDoCineDebate(admin.TabularInline):
    model = fotosImagensDoCineDebate    

class EventosCineDebateAdmin(admin.ModelAdmin):
    list_display = ('tituloDaExibicao','data','local','endereco','delete_button')  
    fieldsets = [
        ('Vinculado ao período', {'fields': ['cine']}),
        ('Nome da exibição', {'fields': ['tituloDaExibicao']}),
        ('Quando foi exibido?', {'fields': ['data']}),
        ('Onde?', {'fields': ['local']}),
        ('Endereço ', {'fields': ['endereco']}),
        ('Se houver insira o logo do trailer do vídeo', {'fields': ['logo']}),
    ]
    inlines = [IframesLinksInline, ImagensDoCineDebate]
    search_fields = ['tituloDaExibicao','data','local','endereco']
    list_filter = ['tituloDaExibicao','data','local','endereco']
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/eventoscinedebate/{}/delete/">Delete</a>', obj.id)

class AtividadesPorAnoInline(admin.TabularInline):
    model = AtividadesPorAno
    extra = 2

class CineDebateInline(admin.TabularInline):
    model = CineDebate
    extra = 2

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('dataInicial','dataFinal')
    fieldsets = [
        ('Período dos eventos a serem cadastrados', {'fields': ['dataInicial', 'dataFinal']}),
    ]
    inlines = [AtividadesPorAnoInline, CineDebateInline]

class AnoAdmin(admin.ModelAdmin):
    # list_display = ('ano')
    fieldsets = [
        ('Ano dos eventos a serem cadastrados', {'fields': ['ano']}),
    ]
    inlines = [AtividadesPorAnoInline, CineDebateInline]

class InformacoesTecnicasInline(admin.StackedInline):
    model = InformacoesTecnicas


class HorarioExibicaoInline(admin.StackedInline):
    model = HorarioExibicao

class LocalExibicaoInline(admin.StackedInline):
    model = LocalExibicao

class FilmesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data','titulo','cinedebate', 'delete_button')
    # list_display = ('__str__', 'change_button', 'delete_button')
    fieldsets = [
        ('Nome do filme', {'fields': ['titulo']}),
        ('Quando será exibido?', {'fields': ['data']}),
        ('Vinculado ao cinedebate ', {'fields': ['cinedebate']}),
    ]
    list_filter = ['data']
    inlines = [InformacoesTecnicasInline, HorarioExibicaoInline]
    search_fields = ['titulo']

    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/filmes/{}/delete/">Delete</a>', obj.id)

class FotosDasAtividadesAdmin(admin.ModelAdmin):
    list_display = ('atividade','image','comentario', '__str__', 'delete_button')        
    search_fields = ['atividade']

    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/sitenupeb/fotosdasatividades/{}/delete/">Delete</a>', obj.id)

class FilmesInline(admin.TabularInline):
    model = Filmes

class ImagensCineDebateInline(admin.TabularInline):
    model = fotosImagensDoCineDebate
    extra = 2

class EventosCineDebateInline(admin.StackedInline):
    model = EventosCineDebate

class CineDebateAdmin(admin.ModelAdmin):
    list_display = ('ano','periodo', 'descricao')
    inlines = [FilmesInline, EventosCineDebateInline]
    list_filter = ['ano','periodo']
    search_fields = ['tituloDaAtividade', 'local']

class CineDebateEventoAdmin(admin.ModelAdmin):
    list_display = ('tituloDaExibicao','data', 'cine','local')
    inlines = [ImagensCineDebateInline]

class FotosInline(admin.TabularInline):
    model = FotosDasAtividades
    extra = 1

class AtividadesPorAnoAdmin(admin.ModelAdmin):
    list_display = ('tituloDaAtividade','dataAtividade','local','descricao')
    # fieldsets = ['tituloDaAtividade','dataAtividade','local','descricao']
    fieldsets = [
        ('O que foi feito', {'fields': ['tituloDaAtividade']}),
        ('Datas do evento', {'fields': ['dataAtividade', 'ano','periodo']}),
        ('Onde?', {'fields': ['local']}),
        ('Como foi?', {'fields': ['descricao']})
    ]
    list_filter = ['dataAtividade']
    inlines = [FotosInline]
    search_fields = ['tituloDaAtividade','local']

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horario','filme','localExibicao')
    list_filter = ['horario','filme','localExibicao']
    search_fields = ['filme','localExibicao']

# class FotosInline(admin.TabularInline):
#     model = FotosDasAtividades
#     extra = 1


admin.site.register(AtividadesPorAno, AtividadesPorAnoAdmin)

##########registro de período################
admin.site.register(Ano, AnoAdmin)
admin.site.register(Periodo, PeriodoAdmin)

##########eventos cinema###################
admin.site.register(CineDebate, CineDebateAdmin)
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(FotosDasAtividades,FotosDasAtividadesAdmin)
admin.site.register(HorarioExibicao, HorarioAdmin)
admin.site.register(EventosCineDebate, EventosCineDebateAdmin)

#################integrantes e pesquisadores########
admin.site.register(Pesquisador,PesquisadorAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(Egresso, EgressoAdmin)


#############linha de pesquisa################
admin.site.register(LinhaDePesquisa, LinhaDePesquisaAdmin)

##########documentação abaixo##################
admin.site.register(DocumentosNacionais, DocsNacionaisAdmin)
admin.site.register(DocumentosInternacionais, DocsInternacionaisAdmin)
admin.site.register(Publicacoes, PublicacoesAdmin)
admin.site.register(LegislacaoEstadual, LegislacaoEstadualAdmin)
admin.site.register(DocumentosEstaduais, DocEstaduaisAdmin)
admin.site.register(LegislacaoNacional, LegislacaoNacionalAdmin)
admin.site.register(SubDocumento, SubDocumentoAdmin)


############# EVENTOS ################
admin.site.register(Eventos, EventosAdmin)


############# FILMES POR TEMA ###########
admin.site.register(TemaFilme, TemaFilmeAdmin)

    
############sem personalização de admin###########
admin.site.register(FilmePorTema)
admin.site.register(IframesLinks)
admin.site.register(LocalExibicao)
admin.site.register(Objetivos)
admin.site.register(ProximoFilme)
admin.site.register(InformacoesTecnicas)

admin.site.site_header = 'NuPEB'
admin.site.site_title = 'Gerenciador NuPEB'
#admin.site.index_title = 'Features area'  

