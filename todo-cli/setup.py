from setuptools import setup

setup(
    name='todo_cli',
    version="0.1.0",
    packages=["todo_cli"],
    entry_points={
        'console_scripts': [
            'todo = todo_cli.__main__:main'
        ]
    }
)
