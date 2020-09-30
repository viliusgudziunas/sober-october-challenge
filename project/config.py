import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess-string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://postgres:postgres@localhost:5432/sober-october"
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4


class StagingConfig(BaseConfig):
    """Staging configuration"""
    pass


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        ("postgres://oyyfyvqxgqjtyh:07275dba3adb231975b4a88a75c57e71828cabc02aa0d89f154"
         "b6094def4273f@ec2-54-160-161-214.compute-1.amazonaws.com:5432/d7mfmi9nol51tt")
