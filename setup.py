from setuptools import setup, find_packages
import bayes_opt

setup(
    name='bayesian-optimization',
    version=bayes_opt.__version__,
    url='https://github.com/fmfn/BayesianOptimization',
    packages=find_packages(),
    author='Fernando Nogueira',
    author_email="fmfnogueira@gmail.com",
    description='Bayesian Optimization package',
    long_description="A Python implementation of global optimization with gaussian processes.",
    install_requires=[
        "numpy >= 1.9.0",
        "scipy >= 1.6.0",
        "scikit-learn >= 0.18.0",
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)
