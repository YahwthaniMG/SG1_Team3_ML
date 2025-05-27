from setuptools import setup, find_packages

setup(
    name="SG1_Team3_ML",
    version="1.0.0",
    author="Yahwthani Morales Gómez",
    author_email="0246038@up.edu.mx",
    description="Titanic Survival Prediction using Machine Learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YahwthaniMG/SG1_Team3_ML.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
    ],
)
