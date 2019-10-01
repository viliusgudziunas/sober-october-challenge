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
        "postgresql://postgres:123456@localhost/sober-october"
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
        "postgres://xjcxnevjniqnfl:23610365df41885ab81b1a1ed895efe564f69f8b35622756563ef10274d877f4@ec2-107-22-222-161.compute-1.amazonaws.com:5432/d54r43ajqah3rn"
