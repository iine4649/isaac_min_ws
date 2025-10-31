from setuptools import setup
from glob import glob
import os

package_name = 'vslam_bringup'

data_files = [
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ('share/' + package_name + '/config', glob('config/*.yaml')),
    ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
]

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shunski Honjonov',
    maintainer_email='shunsuke20070602honjo@gmail.com',
    description='VSLAM + Mapper + QR Bringup',
    license='MIT',
)


