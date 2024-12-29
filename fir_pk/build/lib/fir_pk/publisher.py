import rclpy


from std_msgs.msg import String

from rclpy.node import Node

class PublisherNode(Node):
    def __init__(self):
        super().__init__("node_publisher")
        self.publisher_ = self.create_publisher(String,'communication_node',15)
        commRate = 1
        
        self.timer = self.create_timer(commRate, self.callbackFunction)
        self.counter = 0
    def callbackFunction(self):
        messagePublisher = String()
        messagePublisher.data = 'Counter value: %d' %self.counter
        self.publisher_.publish(messagePublisher)
        self.get_logger().info('Publisher Node is Publishing: %s' % messagePublisher.data)
        self.counter = self.counter + 1
        
def main(args =    None):
    rclpy.init(args=args)
    node_publisher = PublisherNode()
    rclpy.spin(node_publisher)
    node_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()