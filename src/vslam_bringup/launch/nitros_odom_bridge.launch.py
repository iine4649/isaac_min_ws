from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # 注意: 実行には NITROS ブリッジ実装が必要です。
    # 実際の実行ファイル/パラメータは環境に合わせて調整してください。
    bridge = Node(
        package='isaac_ros_nitros',
        executable='nitros_odom_bridge',
        name='nitros_odom_bridge',
        output='screen'
    )

    return LaunchDescription([
        bridge
    ])


