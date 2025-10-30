from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    rs = Node(
      package='realsense2_camera', executable='realsense2_camera_node', name='d455f',
      parameters=[{'enable_color': True,'enable_depth': True,'enable_gyro': True,'enable_accel': True,
                   'unite_imu_method': 2,'publish_odom_tf': False,'align_depth.enable': True,
                   'rgb_camera.profile': '640x480x30','depth_module.profile': '640x480x30','enable_sync': True}],
      output='screen')
    vslam = Node(
      package='isaac_ros_visual_slam', executable='visual_slam_node', name='visual_slam',
      remappings=[('stereo_camera/left/image','/d455f/infra1/image_raw'),
                  ('stereo_camera/right/image','/d455f/infra2/image_raw'),
                  ('stereo_camera/left/camera_info','/d455f/infra1/camera_info'),
                  ('stereo_camera/right/camera_info','/d455f/infra2/camera_info'),
                  ('imu','/d455f/imu'),
                  ('visual_slam/tracking/pose','/visual_slam/tracking/pose')],
      parameters=[{'enable_rectified_pose': True,'enable_slam_visualization': False,'denoise_input_images': False}]
    )
    return LaunchDescription([rs, vslam])
