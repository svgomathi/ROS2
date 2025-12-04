# ROS 2 Hello World Publisher & Subscriber (Python)

This package contains a simple ROS 2 example showing how to create a **Publisher** and **Subscriber** in Python using `rclpy` and the `std_msgs/msg/String` message type.  
It is beginner-friendly and demonstrates the basic communication flow in ROS 2.

---

## Files Included

### **publisher.py**
A ROS 2 node that publishes `"Hello World <counter>"` every 0.5 seconds on the topic `/hello_world`.  
Source: publisher.py

### **subscriber.py**
A ROS 2 node that subscribes to `/hello_world` and prints each received message.  
Source: subscriber.py

---

## How It Works

### **Publisher Node**
- Node name: `hello_world_pub_node`
- Publishes `std_msgs/String`
- Topic: `/hello_world`
- Publishes every **0.5 seconds**

```python
self.pub = self.create_publisher(String, "hello_world", 10)
self.timer = self.create_timer(0.5, self.publish_hello_world)

---

## Run the nodes
ros2 run my_py_pkg publisher
ros2 run my_py_pkg subscriber

## useful commands
ros2 topic list
ros2 node info hello_world_pub_node
ros2 topic echo /hello_world
