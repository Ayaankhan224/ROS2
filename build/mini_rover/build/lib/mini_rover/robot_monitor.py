import rclpy
from rclpy.node import Node

class RobotMonitor(Node):

  def __init__(self):
    super().__init__('robot_monitor')
    self.get_logger().info('Robot Monitor Started')
    self.declare_parameter('timer_period', 2.0)
    timer_period = self.get_parameter('timer_period').value
    self.timer = self.create_timer(timer_period, self.timer_callback)

  def timer_callback(self):
    self.get_logger().info('Robot is running....')

def main(args=None):
  rclpy.init()
  node = RobotMonitor()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__=='__main__':
  main()