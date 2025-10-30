from setuptools import setup, find_packages
from glob import glob

package_name = 'perception_vslam'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='x',
    maintainer_email='x@example.com',
    description='Launch wrapper for RealSense + Isaac ROS Visual SLAM',
    license='MIT',
    entry_points={'console_scripts': []},
)
