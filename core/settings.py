SECRET_KEY='dev-secret-key-change-in-prod'
DEBUG=True
ALLOWED_HOSTS=['*']

INSTALLED_APPS=[
'django.contrib.staticfiles',
'django.contrib.sessions',
'django.contrib.messages',
'app'
]

MIDDLEWARE=[
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF='core.urls'

TEMPLATES=[{
'BACKEND':'django.template.backends.django.DjangoTemplates',
'DIRS':['templates'],
'APP_DIRS':True,
'OPTIONS': {
    'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
    ],
},
}]

STATIC_URL='/static/'
STATICFILES_DIRS=['static']

SESSION_ENGINE='django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_AGE = 86400 * 7
