#celery socket fail
#need for the further developing

from __future__ import absolute_import
from celery import Celery
__author__ = 'dengcanrong'
#app.import_name

def make_celery(app):
    celery = Celery('oldbirds', broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery