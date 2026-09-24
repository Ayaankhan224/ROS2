import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarProcessor(Node):
  def __init__(self):
    super().__init__("lidar_processor")

    self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

  def scan_callback(self, msg):
    ranges = msg.ranges

    front_index = round((0.0 - msg.angle_min) / msg.angle_increment)
    front_distance = ranges[front_index]

    self.get_logger().info(f'FRONT DISTANCE: {front_distance}')

def main(args=None):
  rclpy.init(args=args)

  node = LidarProcessor()
  rclpy.spin(node)

  node.destroy_node()
  rclpy.shutdown

if __name__ == '__main__':
  main()