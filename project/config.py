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
        ("postgres://ryrtidxzalvgjm:527404a459e83c728d9b69a4477b297837c398f07b684dc2168"
         "9c0c548933651@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/d3b8pr3i"
         "khcl9b")
