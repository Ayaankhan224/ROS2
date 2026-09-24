import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class MotionController(Node):
  def __init__(self):
    super().__init__('motion_controller')

    self. publisher = self.create_publisher(TwistStamped, 'cmd_vel', 10)

    self.counter = 0

    self.timer = self.create_timer(1.0, self.move_robot)

  def move_robot(self):
    self.counter += 1
    msg = TwistStamped()

    if self.counter <= 4:
      msg.twist.linear.x = 0.2
      msg.twist.angular.z = 0.0
    elif self.counter <=8:
      msg.twist.linear.x = 0.0
      msg.twist.angular.z = 0.5
      msg.twist.linear.y = 0.2
    elif self.counter <= 12:
      msg.twist.linear.x = 0.2
      msg.twist.angular.z = 0.0

    self.publisher.publish(msg)

def main(args=None):
  rclpy.init(args=args)

  node = MotionController()
  rclpy.spin(node)

  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()