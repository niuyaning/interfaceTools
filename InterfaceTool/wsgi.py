#用于运行开发服务器和把项目部署到生产环境的一个python脚本

"""
WSGI config for InterfaceTool project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InterfaceTool.settings')

application = get_wsgi_application()
