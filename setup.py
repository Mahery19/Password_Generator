from setuptools import setup, find_packages

setup(
    name='password-generator-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'password-generator=password_generator.generator:main',
        ],
    },
    description="A command-line tool for generating secure passwords.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/password-generator",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
