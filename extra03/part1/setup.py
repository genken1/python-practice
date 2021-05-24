# Для установки собственного пакета выполните данные команды из текущей дирректории
# python setup.py build
# python setup.py install
from setuptools import setup

setup(
    name='own_package',
    version='0.0.1',
    description='own_package',
    package_data={'own_package': ['./own_package/data.json']},
    include_package_data=True,
    author='Chushkin Oleg',
    packages=['own_package']
)
