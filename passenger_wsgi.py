# -*- coding: utf-8 -*-
import os, sys
sys.path.append('/home/p/playpbqj/playpbqj.beget.tech/university')
sys.path.append('/home/p/playpbqj/playpbqj.beget.tech/venv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'university.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
