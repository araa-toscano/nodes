#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 


if __name__ == '__main__':
    rospy.init_node("my_publisher_1")
    rospy.loginfo("Node started...")
    rate = rospy.Rate(10)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    msg = Twist()
        
    

    while not rospy.is_shutdown():
        msg.linear.x = 3.1
        msg.angular.z = 1.2
        pub.publish(msg)
        rospy.loginfo("Hello0...")
        rate.sleep()


