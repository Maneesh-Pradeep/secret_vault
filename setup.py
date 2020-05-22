from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='secret_vault',
    version='1.0.2',
    description='Python secret vault',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Maneesh Pradeep',
    author_email='manojshan2002@gmail.com',
    url='https://github.com/Manoj-Shan/secret_vault',
    license='MIT',
    py_modules=['secret_vault'],
    install_requires=['cryptography', 'pyAesCrypt'],
    entry_points={
        'console_scripts': [
            'secret_vault = secret_vault:main',
        ],
    },
    classifiers=[
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
    ],
)