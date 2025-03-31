from .celery_app import app as celery_app
# Чтобы celery-апка стартанула вместе с нашим приложением django
__all__ = ('celery_app',)