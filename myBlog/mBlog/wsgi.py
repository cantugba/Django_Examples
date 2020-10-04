"""
WSGI config for mBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#django geliştirme sunucusu için WSGI uygulamasını içerir. Bu dosya içerisine herhangi bir şey yazılamaz.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mBlog.settings')

application = get_wsgi_application()
