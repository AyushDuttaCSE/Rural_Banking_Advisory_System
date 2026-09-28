 

import os
from datetime import timedelta

AUTH_USER_MODEL = "core.User"

INSTALLED_APPS = [
    # ...django defaults...
    "django.contrib.gis",          
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "core",                        
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # ...rest of Django default middleware...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",       
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=12),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
}

DATABASES = {
    "default": {
        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "gramsetu"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]   
