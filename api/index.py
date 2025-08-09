import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mentorship_site.settings")
from mentorship_site.asgi import application as app