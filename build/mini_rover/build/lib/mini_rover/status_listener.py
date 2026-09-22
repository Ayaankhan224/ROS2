import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusListener(Node):

  def __init__(self):
    super().__init__('status_listener')

    self.subscriber = self.create_subscription(String, 'robot_status', self.status_callback, 10)

  def status_callback(self, msg):
    self.get_logger().info(f'Recieved: {msg.data}')

def main(args=None):
  rclpy.init()

  node = StatusListener()
  rclpy.spin(node)

  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()