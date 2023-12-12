try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'quiz system',
    'author': 'Water Chen',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'Waterchen188@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['quiz_system'],
    'scripts': [],
    'name': 'quiz_system'
}

setup(**config)