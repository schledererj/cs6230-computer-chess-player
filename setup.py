from setuptools import setup, find_packages

setup(name='computer-chess-player',
      version='1.0',
      description='A computer chess player made for CS6230',
      author='Jack Schlederer',
      author_email='schlederer3@gmail.com',
      packages=find_packages(),
      install_requires=[
          "python-chess==1.999",
          "termcolor==1.1.0",
          "numpy==1.21.4"
      ],
      entry_points={
          "console_scripts": [
              "play-chess = computer_chess_player.cli:main"
          ]
      }
      )
