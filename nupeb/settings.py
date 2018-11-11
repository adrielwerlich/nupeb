"""
Django settings for nupeb project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+aux1=^7mn+24gl0--pq=_j&@z+k)cg==l4x6-j7(0(7^ij_5f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
SITE_ID = 1
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'sitenupeb',
    'django_countries',
    'debug_toolbar',
    'template_debug',
    'embed_video',
		'admin_reorder',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
		'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'nupeb.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nupeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


INTERNAL_IPS = ['127.0.0.1', 'localhost']
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },

    # this cache backend will be used by django-debug-panel
    'debug-panel': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/debug-panel-cache',
        'OPTIONS': {
            'MAX_ENTRIES': 200
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'sitenupeb/static/media')
# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'sitenupeb/static/'),
# ]



ADMIN_REORDER = (
		######## CINEDEBATE #######
    {'app': 'sitenupeb', 'label': 'CineDebate',
     'models': ('sitenupeb.CineDebate',
								'sitenupeb.Filmes',
								'sitenupeb.InformacoesTecnicas',
								'sitenupeb.LocalExibicao',
								'sitenupeb.HorarioExibicao',
								'sitenupeb.EventosCineDebate',
								'sitenupeb.HorarioExibicao',
								'sitenupeb.VideoTrailer',
								'sitenupeb.FotosDoCineDebate',
								'sitenupeb.ProximoFilme',)
    },
		######## DOCUMENTOS  ########
    {'app': 'sitenupeb', 'label': 'Documentos',
     'models': ('sitenupeb.DocumentosInternacionais',
						 	  'sitenupeb.DocumentosNacionais',
					 		  'sitenupeb.SubDocumento',
				 			  'sitenupeb.Publicacoes',
			 				  'sitenupeb.LegislacaoNacional',
		 					  'sitenupeb.DocumentosEstaduais',
	 						  'sitenupeb.LegislacaoEstadual',)
    },
		######## EVENTOS #######
		{'app': 'sitenupeb', 'label': 'Eventos',
     'models': ('sitenupeb.Eventos',
						 	  'sitenupeb.ParticipanteEvento',
					 		  'sitenupeb.FotosEvento',)
    },
		######## FILMES #######
		{'app': 'sitenupeb', 'label': 'Filmes',
     'models': ('sitenupeb.TemaFilme',
						 	  'sitenupeb.FilmePorTema',)
    },
		######## LEITURAS  ######## 
    {'app': 'sitenupeb', 'label': 'Leituras',
     'models': ('sitenupeb.TemaLeitura',
						 	  'sitenupeb.LeituraPorTema',)
    }, 
		######## MODELOS DE TEMPO ########
    {'app': 'sitenupeb', 'label': 'Cadastro de período',
     'models': ('sitenupeb.Periodo',
						 	  'sitenupeb.Ano',)
    }, 
		######## MODELOS ATIVIDADES ########
    {'app': 'sitenupeb', 'label': 'Cadastro de atividades',
     'models': ('sitenupeb.AtividadesPorAno',
						 	  'sitenupeb.FotosDasAtividades',)
    },
		######## MODELOS LINHA DE PESQUISA ########
    {'app': 'sitenupeb', 'label': 'Cadastro Conteúdo Tela de Apresentação',
     'models': ('sitenupeb.Objetivos',
						 	  'sitenupeb.LinhaDePesquisa',)
    },
		######## MODELOS MATERIAL DIDÁTICO ########
    {'app': 'sitenupeb', 'label': 'Cadastro dos materiais didáticos',
     'models': ('sitenupeb.MaterialDidatico',
						 	  'sitenupeb.DescricaoMaterialDidatico',)
    },
		######## MODELOS LINHA DE PESQUISA ########
    {'app': 'sitenupeb', 'label': 'Cadastro das linhas de pesquisa',
     'models': ('sitenupeb.PesquisasEmAndamento',
						 	  'sitenupeb.PesquisasRealizadas',)
    },
		######## MODELOS LINHA DE PESQUISA ########
		{'app': 'sitenupeb', 'label': 'Cadastro da info do Ppge',
     'models': ('sitenupeb.Ppge',
						 	  'sitenupeb.LinhaPpge',
								'sitenupeb.DocentesPpge',
								'sitenupeb.ContatoPpge',
								'sitenupeb.EmailPpge',)
    },
		######## PRODUÇÃO ########
		{'app': 'sitenupeb', 'label': 'Cadastro das referências',
     'models': ('sitenupeb.RefereciaCita',
						 	  'sitenupeb.AutoresPesq',
								'sitenupeb.AutorRef',)
    },
		
		
		
		
		
		
		
		)
		
		
		
		
		
		
		
		
		
		
		
		