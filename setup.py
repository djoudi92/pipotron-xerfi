from setuptools import setup, find_packages

setup(
    name="pipotron",
    version="0.1",
    description="Vérificateur de phrases pipotron",
    author="Abdessalem Djoudi",
    packages=find_packages(),
    install_requires=[],
)
from pipotron.core import my_function