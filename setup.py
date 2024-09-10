from setuptools import setup, find_packages

setup(
    name='p2p_network',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'twisted',
    ],
    entry_points={
        'console_scripts': [
            'p2p-server=p2p_server:main',
            'p2p-client=p2p_client:main',
        ],
    },
    python_requires='>=3.6',
)
