from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    CHANNELS: dict[str, int]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="TG_",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
config = Settings()