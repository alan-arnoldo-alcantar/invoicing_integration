from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        # El pah es relativo respecto a donde se corre uv run
        # como nostros lo corremos desde la carpeta raiz entonces ".env"
        # Si corrieramos uv desde la carpeta app, seria "../.env"
        env_ignore_empty=True, # Variables en .env vacias
        extra="ignore" # Si hay variables en .env sin usar en config.py
    )
    API_VERSION: str 
    PROJECT_NAME: str
    FACTURAPI_USER_SECRET_KEY: str
    FACTURAPI_URL: str

settings = Settings()