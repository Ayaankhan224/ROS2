import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Bool

class MotionController(Node):
  def __init__(self):
    super().__init__('motion_controller')

    self.obstacle_detected = False
    self.subscription = self.create_subscription(Bool, 'obstacle_detection', self.obstacle_callback, 10)
    self. publisher = self.create_publisher(TwistStamped, 'cmd_vel', 10)
    self.timer = self.create_timer(1.0, self.move_robot)
    self.turn_count = 0

  def obstacle_callback(self, msg):
    self.obstacle_detected = msg.data

  def move_robot(self):
    msg = TwistStamped()

    if self.obstacle_detected:
      msg.twist.linear.x = 0.0

      if self.turn_count < 5:
        msg.twist.angular.z = 0.5
      else:
        msg.twist.angular.z = -0.5
      self.turn_count += 1

    else:
        msg.twist.linear.x = 0.35
        msg.twist.angular.z = 0.0
        self.turn_count = 0

    self.publisher.publish(msg)

def main(args=None):
  rclpy.init(args=args)

  node = MotionController()
  rclpy.spin(node)

  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()