import os
from django.core.asgi import get_asgi_application

# Default Django settings for ASGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_asgi_application()
