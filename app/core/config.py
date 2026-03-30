from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    database_url: str = 'postgresql+psycopg2://postgres:root@localhost:5432/embarqueja'
    secret_key: str = 'dev-secret-key'
    debug: bool = True
    api_version: str = 'v1'

    class Config():
        env_file = '.env'

settings = Settings()
