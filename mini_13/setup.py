from setuptools import Extension, setup


setup(
    name='matrix_power',
    version='1.0',
    description='C extension for matrix exponentiation',
    ext_modules=[
        Extension(
            name='matrix_power',
            sources=['matrix_power.c'],
        ),
    ]
)
