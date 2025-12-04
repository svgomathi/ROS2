# ROS2 Python Node – Minimal Example

This repository contains a simple ROS2 Python node written using **rclpy**.  
It is designed as a beginner-friendly example to understand how nodes work in ROS2.

---

## File Included
### **my_first_node.py**
A minimal ROS2 node that:
- Initializes ROS2  
- Creates a node named `my_first_node`  
- Prints a log message when started  
- Spins until shutdown  

# Build and run
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run my_py_pkg my_first_node

# setup.py
'my_first_node = my_py_pkg.my_first_node:main',
