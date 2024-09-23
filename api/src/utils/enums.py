from enum import Enum


class Modes(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    STAGING = "staging"


class Tags(str, Enum):
    HEALTH = "Health Check"
    AUTH = "Authentication & Authorization"
