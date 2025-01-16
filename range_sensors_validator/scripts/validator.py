#!/usr/bin/env python3

import rospy
import random
# from sensor_msgs.msg import Range
from range_sensors_validator.msg import sensor_properties

if __name__=="__main__":
    rospy.init_node("validator_node")
    rospy.loginfo("node has been started")
    pub=rospy.Publisher("sensor_quality",sensor_properties, queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        msg=sensor_properties()
        msg.Quality= random.randint(1,100)
        msg.sensor_values.min_range = random.uniform(0.1, 1.0)  
        msg.sensor_values.max_range = random.uniform(1.1, 5.0)  
        msg.sensor_values.range = random.uniform(msg.sensor_values.min_range, msg.sensor_values.max_range)  
        pub.publish(msg)
        rate.sleep()