from setuptools import setup, find_packages

setup(
    name="ganabosques_orm",
    version="0.1.0",
    description="ORM package for Ganabosques project using MongoEngine",
    author="Ciencia de Datos GPT",
    author_email="h.sotelo@cgiar.org",
    packages=find_packages(),
    install_requires=[
        "mongoengine>=0.27.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)