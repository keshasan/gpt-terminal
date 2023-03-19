from setuptools import setup

setup(
    name='gpt',
    version='1.0.0',
    description='Ask GPT in terminal',
    url='https://github.com/Keshasan/gpt-terminal.git',
    author='Aleksandr Holoborodko',
    author_email='kesha3084@gmail.com',
    license='MIT',
    entry_points={'console_scripts': ['gpt = gpt-terminal.gpt-terminal:main']}
)