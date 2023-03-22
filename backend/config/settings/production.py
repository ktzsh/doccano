from .base import *  # noqa: F401,F403

DEBUG = False

MIDDLEWARE.append("api.middleware.RangesMiddleware")  # noqa: F405

DJANGO_DRF_FILEPOND_STORAGES_BACKEND = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_REGION_NAME = env("REGION_NAME", "us-east-1")
AWS_STORAGE_BUCKET_NAME = env("BUCKET_NAME", "doccano")
AWS_LOCATION = env("S3_LOCATION", "doccano")

CELERY_TASK_ACKS_LATE=False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s::%(funcName)s::%(lineno)d] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
