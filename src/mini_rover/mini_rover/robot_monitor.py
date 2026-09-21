import rclpy
from rclpy.node import Node

class RobotMonitor(Node):

  def __init__(self):
    super().__init__('robot_monitor')
    self.get_logger().info('Robot Monitor Started')

def main(args=None):
  rclpy.init()
  node = RobotMonitor()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__=='__main__':
  main()