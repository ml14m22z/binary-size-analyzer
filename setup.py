from setuptools import setup, find_packages

setup(
    name='binary-size-analyzer',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/yourusername/binary-size-analyzer',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Linux binary program size analyzer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)