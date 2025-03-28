from .celery_app import app as celery_app

__all__ = ('celery_app',)  #Чтобы celery_апка стартанула вместе с приложением django
