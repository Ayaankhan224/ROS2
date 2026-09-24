import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class LidarProcessor(Node):
  def __init__(self):
    super().__init__("lidar_processor")

    self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

  def scan_callback(self, msg):
    ranges = msg.ranges

    front_index = round((0.0 - msg.angle_min) / msg.angle_increment)
    front_ranges = ranges[-10:] + ranges[:11]
    valid_ranges = [r for r in front_ranges if math.isfinite(r)]
    if valid_ranges:
      front_distance = min(valid_ranges)
    else:
      front_distance = float('inf')

    if front_distance <= 0.5:
      self.get_logger().info("OBSTACLE AHEAD!")
    else:
      self.get_logger().info("PATH CLEAR!")

def main(args=None):
  rclpy.init(args=args)

  node = LidarProcessor()
  rclpy.spin(node)

  node.destroy_node()
  rclpy.shutdown

if __name__ == '__main__':
  main()