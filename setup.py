from setuptools import setup
from os import path
setup(
    name='lidar_lite_v2',
    version='1.0.0',
    description='Retrieve depth information from LidarLiteV2 over I2C.',
    author='David van der Pol',
    install_requires=[
        'smbus2',
    ],
    py_modules=['lidar_lite_v2'],
)
