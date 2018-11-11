import ipdb
from django.db.models import Prefetch
from django.shortcuts import render
from .models import *
# CineDebate,Filmes,HorarioExibicao,Ano,AtividadesPorAno,FotosDasAtividades,\
#     InformacoesTecnicas,LinhasDePesquisa,Periodo,ProximoFilme,Objetivos,\
#     LocalExibicao,fotosImagensDoCineDebate,EventosCineDebate

# Create your views here.


def loadModels():
    
    #********atividades*************
    atividades = AtividadesPorAno.objects.all()
    fotosDasAtividades = FotosDasAtividades.objects.all()
    #********filmes*************
    filmes = Filmes.objects.all()
    infoTecs = InformacoesTecnicas.objects.all()
    horariosExibicao = HorarioExibicao.objects.all()

    for filme in filmes:
        for horario in horariosExibicao:
            if horario.filme == filme:
                filme.horaExib = horario
								
    #********cinedebates*************

    eventosCineDebate = EventosCineDebate.objects.all()
    trailers = VideoTrailer.objects.all()
    fotosCineDebate = FotosDoCineDebate.objects.all()
    for evento in eventosCineDebate: 
        evento.trailer = trailers.filter(evento__exact=evento)
        evento.fotos = fotosCineDebate.filter(cinedebate__exact=evento)

    proximofilme = ProximoFilme.objects.all().first()
				
    #********integrantes,pesquisadores etc *************
    pesquisadores = Pesquisador.objects.all()
    integrantes = Integrante.objects.all()
    egressos = Egresso.objects.all()

    #********Linha de pesquisa e objetivo *************        
    objetivo = Objetivos.objects.all()
    linhas = LinhaDePesquisa.objects.all()

		
		#******** documentos *************
    docsInternacionais = DocumentosInternacionais.objects.all()
    docsNacionais = DocumentosNacionais.objects.all()
    subDocs = SubDocumento.objects.all()
    for dn in docsNacionais:
		    dn.subDocs = subDocs.filter(documentoPai__exact=dn)
				
    publicacoes = Publicacoes.objects.all()
    legisNacional = LegislacaoNacional.objects.all()
    docsEstaduais = DocumentosEstaduais.objects.all()
    legisEstadual = LegislacaoEstadual.objects.all()
		
		#*************** eventos ******************
    eventos = Eventos.objects.all()
    participantes = ParticipanteEvento.objects.all()
    ftEventos = FotosEvento.objects.all()
    for evt in eventos:
        evt.parts = participantes.filter(evento__exact=evt)
        evt.fotos = ftEventos.filter(evento__exact=evt)
		
		#*************** filmes temas ******************
    temasFilmes = TemaFilme.objects.all()
    filmesPorTema = FilmePorTema.objects.all()
    for temafilme in temasFilmes:
        temafilme.filmes = filmesPorTema.filter(tema__exact=temafilme)
		
		#*************** leituras temas ******************
    temasLeituras = TemaLeitura.objects.all()
    leiturasPorTema = LeituraPorTema.objects.all()
    for temaleitura in temasLeituras:
        temaleitura.leituras = leiturasPorTema.filter(tema__exact=temaleitura)
		
		
		#*************** materiais didáticos ******************
    materialdidatico = MaterialDidatico.objects.all()
    descricao_md = DescricaoMaterialDidatico.objects.all()
    for material in materialdidatico:
        material.desc = descricao_md.filter(material__exact=material)
		
		#*********** pesquisas realizadas e em andamento ***********
    pRealizadas = PesquisasRealizadas.objects.all()
    pemAndamento = PesquisasEmAndamento.objects.all()
		
		#***************** PPGE *****************
    ppge = Ppge.objects.all().first()
    ppge.linhasPpge = LinhaPpge.objects.all()
    docentes = DocentesPpge.objects.all()
    for linha  in ppge.linhasPpge:
		    linha.docentes = docentes.filter(linha__exact=linha)
    ppge.contato = ContatoPpge.objects.all().first()
    ppge.email = EmailPpge.objects.all()
		
		#************ referências e autores ************
    referencias = RefereciaCita.objects.all()
		
    #ipdb.set_trace()
    
    return {'atividades':atividades, 'docsInternacionais':docsInternacionais,
            'filmes':filmes, 'docsNacionais':docsNacionais,
            'fotos':fotosDasAtividades, 'legisNacional':legisNacional,
            'infoTecnicas':infoTecs, 'publicacoes':publicacoes,
            'horarios':horariosExibicao, 'docsEstaduais':docsEstaduais,
            'eventosCineDebate':eventosCineDebate, 'legisEstadual':legisEstadual,
            'pesquisadores':pesquisadores, 'eventos':eventos,
            'integrantes':integrantes, 'temasFilmes':temasFilmes,
            'egressos':egressos, 'temasLeituras':temasLeituras,
            'objetivo':objetivo, 'materialdidatico':materialdidatico,
            'linhas':linhas, 'pRealizadas': pRealizadas,
						'pAndamento':pemAndamento,'ppge':ppge,
						'referencias':referencias,
						'proximofilme':proximofilme
						}


def index(request):
    context = loadModels()

    return render(request, 'index.html', context=context)