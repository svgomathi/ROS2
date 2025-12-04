#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__("my_first_node")   # Node Name
        self.get_logger().info("Node has started!")  # Print message

def main(args=None):
    rclpy.init(args=args)           # Initialize ROS2
    node = MyFirstNode()            # Create node object
    rclpy.spin(node)                # Keep the node alive
    rclpy.shutdown()                # Shutdown when done

if __name__ == "__main__":
    main()
