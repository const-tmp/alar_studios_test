from setuptools import setup, find_packages

setup(
    name='alar-studios-test',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'psycopg2',
        'python-dotenv'
    ],
)
