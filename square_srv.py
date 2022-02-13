#!/usr/bin/env python3

import rospy
from turtlesim.srv import TeleportRelative
from math import pi
rospy.init_node("square", anonymous=True)


if __name__ == "__main__":
    rospy.wait_for_service("/turtle1/teleport_relative")
    tel = rospy.ServiceProxy("/turtle1/teleport_relative", TeleportRelative)
    
    tel.call(2,0)
    tel.call(4,pi/2)
    tel.call(4,pi/2)
    tel.call(4,pi/2)
    tel.call(2,pi/2)

