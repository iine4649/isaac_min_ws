from setuptools import setup
import os

package_name = 'vslam_bringup'

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            paths.append(os.path.relpath(file_path, package_name))
    return paths

data_files = [
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
]

for sub in ['launch', 'config', 'rviz']:
    src_dir = os.path.join(package_name, sub)
    if os.path.isdir(src_dir):
        files = package_files(src_dir)
        if files:
            data_files.append(('share/' + package_name + '/' + sub, [os.path.join(package_name, f) for f in files]))

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='x',
    maintainer_email='x@example.com',
    description='Bringup for RealSense + Isaac ROS Visual SLAM',
    license='MIT',
)


