# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['app', 'app.pathfinding.finder']

package_data = \
{'': ['*'], 'app': ['pathfinding/core/*']}

install_requires = \
['bottle==0.12.13',
 'gevent==1.3.6',
 'greenlet==0.4.14',
 'gunicorn==19.9.0',
 'numpy==1.16.2',
 'pathfinding==0.0.3']

setup_kwargs = {
    'name': 'app',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
