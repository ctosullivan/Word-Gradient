from setuptools import setup, find_packages

setup(
    package_dir={'':'src'},
    packages=find_packages('src'),
    name='wordgradient',
    entry_points={
       'console_scripts': [
           'wordgradient = wordgradient.command_line:main',
       ]},
    version='0.01',
    license='MIT',
    description = "Minimal CLI tool to create word frequency heatmap",
    author = "Cormac O' Sullivan",
    author_email= 'cormac@cosullivan.dev',
    url = "https://github.com/ctosullivan/Word-Gradient",
    install_requires=[
          'rich', 'rich-gradient',
      ],
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
)