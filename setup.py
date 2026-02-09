from setuptools import setup, find_packages

setup(
    name="ganabosques_orm",
    version="0.0.33",
    description="ORM package for Ganabosques project using MongoEngine",
    author="Steven Sotelo",
    author_email="h.sotelo@cgiar.org",
    packages=find_packages(),
    install_requires=[
        "mongoengine>=0.27.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)