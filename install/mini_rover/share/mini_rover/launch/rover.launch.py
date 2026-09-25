from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    Node(
      package='mini_rover',
      executable='lidar_processor',
      name='lidar_processor',
      output='screen'
    ),
    Node(
      package='mini_rover',
      executable='motion_controller',
      name='motion_controller',
      output='screen'
    )
  ])