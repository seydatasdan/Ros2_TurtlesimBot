import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist 
import time  
import math

class DrawCircleNode(Node): 
    def __init__(self, pNodeName):
        super().__init__("turtlebot_k_node_" + pNodeName)
        self.declare_parameter('turtleName', rclpy.Parameter.Type.STRING)
        self.declare_parameter('letter', rclpy.Parameter.Type.STRING)
        input_turtleName = self.get_parameter('turtleName')
        input_letter = self.get_parameter('letter')
        turtleName = str(input_turtleName.value)
        letter = str(input_letter.value).lower()
        print("turtleName: " + turtleName)
        print("letter: " + letter)
        
        self.publisher = self.create_publisher(Twist, f'/{turtleName}/cmd_vel', 10)
        self.get_logger().info(turtleName + " kaplumbagasi cizime basliyor...")
        
        if letter == "x":
            self.draw_x()
        elif letter == "h":
            self.draw_h()
        elif letter == "g":
            self.draw_g()
        elif letter == "w":
            self.draw_w()
        
        nodeName = self.get_name()
        print("NodeName: " + nodeName)

    def draw_h(self): 
        twist_msg = Twist() 
        twist_msg.linear.y = 2.0 
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.y = -4.0        
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.y = 2.0 
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = 2.0 
        twist_msg.linear.y = 0.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.y = 2.0 
        twist_msg.linear.x = 0.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.y = -4.0
        twist_msg.linear.x = 0.0
        self.publisher.publish(twist_msg) 
         
    def draw_x(self): 
        twist_msg = Twist() 
        twist_msg.linear.x = -2.0
        twist_msg.linear.y = 2.0  
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = 4.0
        twist_msg.linear.y = -4.0        
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = -2.0
        twist_msg.linear.y = 2.0  
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = 2.0 
        twist_msg.linear.y = 2.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.x = -4.0 
        twist_msg.linear.y = -4.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.x = 2.0
        twist_msg.linear.y = 2.0
        self.publisher.publish(twist_msg)
        
    def draw_w(self):
        time.sleep(12) 
        twist_msg = Twist() 
        twist_msg.linear.x = -1.5
        twist_msg.linear.y = -2.0  
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = -1.0
        twist_msg.linear.y = 4.0        
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = 1.0
        twist_msg.linear.y = -4.0  
        self.publisher.publish(twist_msg) 
        time.sleep(2) 
        twist_msg.linear.x = 1.5 
        twist_msg.linear.y = 2.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.x = 1.5
        twist_msg.linear.y = -2.0
        self.publisher.publish(twist_msg) 
        time.sleep(2)
        twist_msg.linear.x = 1.0
        twist_msg.linear.y = 4.0
        self.publisher.publish(twist_msg)
         
    def draw_g(self): 
    	twist_msg = Twist() 
    	twist_msg.linear.x = 1.0
    	self.publisher.publish(twist_msg)
    	time.sleep(2)

    	twist_msg.linear.y = -1.0
    	twist_msg.linear.x = 0.0
    	self.publisher.publish(twist_msg)
    	time.sleep(2)
    	
    	twist_msg.linear.x = 0.0
    	twist_msg.linear.y = -5.0
    	twist_msg.angular.z = -math.pi  
    	twist_msg.linear.x = -2.0
    	self.publisher.publish(twist_msg)
    	time.sleep(2)
    	
    	twist_msg.linear.x = 0.0
    	twist_msg.linear.y = -5.0
    	twist_msg.angular.z = -math.pi/2  
    	twist_msg.linear.x = -2.0
    	self.publisher.publish(twist_msg)  

def main(args=None): 
    rclpy.init(args=args) 
    print('x0 calisti') 
    node = DrawCircleNode("1")
    rclpy.spin(node) 
    print('iffff calisti')
    rclpy.shutdown()

if __name__ == '__main__':
    main()
