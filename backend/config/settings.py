# backend/config/settings.py

import os

class Settings:
    PROJECT_NAME = "HormigasAIS Video Intelligence Checker"
    API_VERSION = "v1"
    DEBUG = True

    # CORS ORIGINS
    ALLOWED_ORIGINS = ["*"]  # Para producción, se puede restringir esto.

    # Otros parámetros que se pueden agregar aquí:
    # - API_KEYS
    # - Base de datos
    # - Logging levels, etc.

settings = Settings()
