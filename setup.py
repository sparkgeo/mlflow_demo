from setuptools import setup, find_packages

setup(
    name='mlflow_simple_aws',
    version='0.0.1',
    author='Greg Nieuwenhuis',
    author_email='gnieuwenhuis@sparkgeo.com',
    description='Simple MLFlow Server in AWS',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)