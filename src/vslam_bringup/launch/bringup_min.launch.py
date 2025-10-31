from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
import os


def generate_launch_description():
    this_dir = os.path.dirname(__file__)

    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(this_dir, 'realsense.launch.py'))
    )

    vslam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(this_dir, 'visual_slam.launch.py'))
    )

    return LaunchDescription([
        realsense_launch,
        vslam_launch,
    ])


