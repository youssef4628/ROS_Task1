#!/usr/bin/env python3
import rospy
from range_sensors_validator.msg import array_of_accepted_sensors
import os
import subprocess
num=0
def call_back(msg:array_of_accepted_sensors):
    global num
    if num<=len(msg.valid_messages) :
        num = len(msg.valid_messages)
        print(f"No. Accepted msgs {num}")
    if num ==100:
        nodes=subprocess.check_output("rosnode list", shell= True).decode().splitlines()
        for i in nodes:
            if i != "/rosout":
                os.system(f"rosnode kill {i}")

if __name__=="__main__":
    rospy.init_node("z_manager_node")
    rospy.loginfo("node has been started")
    sub=rospy.Subscriber("accepted_sensors",array_of_accepted_sensors,callback=call_back)
    rospy.spin()