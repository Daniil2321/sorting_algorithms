from setuptools import setup, find_packages

setup(
    name='my_library',
    version='0.1.0',
    author='Ваше Имя',
    author_email='ваш_email@example.com',
    description='Краткое описание вашей библиотеки',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ваш_пользователь/my_library',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
