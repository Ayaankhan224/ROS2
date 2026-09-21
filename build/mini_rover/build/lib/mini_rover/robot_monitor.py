import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotMonitor(Node):

  def __init__(self):
    super().__init__('robot_monitor')
    self.get_logger().info('Robot Monitor Started')

    self.create_timer(1.0, self.timer_callback)

    self.publisher = self.create_publisher(String, 'robot_status', 10)

  def timer_callback(self):
    self.get_logger().info('Robot alive...')
    msg = String()
    msg.data = 'Robot saying hello....'
    self.publisher.publish(msg)

def main(args=None):
  rclpy.init()
  node = RobotMonitor()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__=='__main__':
  main()