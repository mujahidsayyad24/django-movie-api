from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movierater.settings')

application = get_asgi_application()
