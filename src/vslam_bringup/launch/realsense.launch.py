from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import ThisLaunchFileDir
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterFile
import os


def generate_launch_description():
    cfg_file = LaunchConfiguration('config_file')
    declare_cfg = DeclareLaunchArgument(
        'config_file',
        default_value=os.path.join(os.path.dirname(__file__), '..', 'config', 'realsense.yaml')
    )

    camera = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node',
        name='realsense2_camera',
        output='screen',
        parameters=[ParameterFile(cfg_file, allow_substs=True)]
    )

    return LaunchDescription([
        declare_cfg,
        camera,
    ])


