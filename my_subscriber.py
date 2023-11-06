#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose 

def pose_callback(msg):
    rospy.loginfo("Received pose: x=%f, y=%f, z=%f", 
                msg.position.x, msg.position.y, msg.position.z)
    

if __name__ == '__main__':
    rospy.init_node("pose_subscriber")
    rospy.loginfo("Node started...")
    rate = rospy.Rate(10)
    subscriber = rospy.Subscriber("/turtle1/cmd_vel", Pose, callback=pose_callback)
    rospy.spin()


