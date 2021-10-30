from setuptools import setup, find_packages

setup(
    name='alar-studios-test',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={
        '': [
            'assets/css/*.css',
            'assets/js/*.js',
            'assets/html/*.html',
            'assets/html/templates/*.html',
            'assets/json/*.json'
        ],
        'alar_studios_test.app.auth': ['templates/login.html'],
        'alar_studios_test.app.users': ['templates/users.html'],
    },
    install_requires=[
        'flask',
        'sqlalchemy',
        'psycopg2',
        'python-dotenv',
        'requests'
    ],
)
