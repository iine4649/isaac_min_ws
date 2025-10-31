from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile
import os


def generate_launch_description():
    cfg_file = LaunchConfiguration('config_file')
    declare_cfg = DeclareLaunchArgument(
        'config_file',
        default_value=os.path.join(os.path.dirname(__file__), '..', 'config', 'visual_slam.yaml')
    )

    vslam = Node(
        package='isaac_ros_visual_slam',
        executable='visual_slam_node',
        name='visual_slam',
        output='screen',
        remappings=[
            ('stereo_camera/left/image', '/realsense2_camera/infra1/image_raw'),
            ('stereo_camera/right/image', '/realsense2_camera/infra2/image_raw'),
            ('stereo_camera/left/camera_info', '/realsense2_camera/infra1/camera_info'),
            ('stereo_camera/right/camera_info', '/realsense2_camera/infra2/camera_info'),
            ('imu', '/realsense2_camera/imu'),
            ('visual_slam/tracking/pose', '/visual_slam/tracking/pose'),
        ],
        parameters=[ParameterFile(cfg_file, allow_substs=True)]
    )

    return LaunchDescription([
        declare_cfg,
        vslam,
    ])


