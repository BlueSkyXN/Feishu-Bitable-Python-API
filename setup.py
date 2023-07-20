from setuptools import setup, find_packages

setup(
    name='FeishuBitableAPI',
    version='3.3.3',
    packages=find_packages(),
    #py_modules=[],
    url='https://github.com/BlueSkyXN/Feishu-Bitable-Python-API',
    author='BlueSkyXN',
    author_email='bluesky@000714.xyz',
    description='A Python API for Feishu Bitable',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'pandas',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
