from setuptools import setup


setup(
    name='Flask',
    version='0.1',
    url='http://github.com/mitsuhiko/flask/',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description='A microframework based on Werkzeug, Jinja2 and good intentions',
    modules=['flask'],
    zip_safe=False,
    platforms='any',
    install_requires=[ # yes, as of now we need the development versions
        'Werkzeug==dev',
        'Jinja2==dev',
    ]
)
