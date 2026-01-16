from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "From Zero To Prod"
    environment: str = "local"

settings = Settings()
