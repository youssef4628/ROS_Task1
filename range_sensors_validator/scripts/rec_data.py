#!/usr/bin/env python3

import rospy
from range_sensors_validator.msg import sensor_properties
from range_sensors_validator.msg import array_of_accepted_sensors

# Create a global instance of array_of_accepted_sensors to persist valid messages
accepted_messages = array_of_accepted_sensors()

def call_back_node(msg: sensor_properties):
    """Callback function to process incoming sensor messages."""
    global accepted_messages
    value = int(msg.Quality)

    if 50 < value < 100:
        rospy.loginfo("Quality accepted")
        rospy.loginfo(f"Sensor values: {msg.sensor_values}")
        accepted_messages.valid_messages.append(msg)  # Add valid messages to the array
        pub.publish(accepted_messages)  # Publish updated list
    else:
        rospy.loginfo("Quality rejected")

def receiver():
    """Set up the subscriber."""
    rospy.Subscriber("sensor_quality", sensor_properties, callback=call_back_node)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("data")

    # Create the publisher
    pub = rospy.Publisher("accepted_sensors", array_of_accepted_sensors, queue_size=10)

    rospy.loginfo("Node is up and running. Waiting for messages...")
    receiver()
