#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header, Float32

rear_vel = 0
front_rot = 0

#Throttle
def callback_throttle(throt):
    global rear_vel
    rear_vel = rear_vel + throt.data*0.01

#Steering
def callback_steering(steer):
    global front_rot
    front_rot = steer.data*-0.4

def talker():
    global rear_vel
    global front_rot

    #Initialize node and publisher
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('racecar_joint_state')
    rate = rospy.Rate(10) # 10hz

    #Create joint state message
    joint = JointState()
    joint.header = Header()
    joint.name = ['fl_holder_joint', 'fr_holder_joint','rl_wheel_joint', 'rr_wheel_joint'\
	, 'fl_wheel_joint', 'fr_wheel_joint']
    joint.velocity = [0, 0, 0, 0, 0, 0]
    joint.effort = []

    while not rospy.is_shutdown():
        #Get throttle and steering
        rospy.Subscriber("throttle", Float32, callback_throttle)
        rospy.Subscriber("steering", Float32, callback_steering)

        #Pubblish joint state for Rviz
        joint.header.stamp = rospy.Time.now()
        joint.position = [front_rot, front_rot, rear_vel, rear_vel, rear_vel, rear_vel]
        pub.publish(joint)

        rate.sleep()

if __name__ == '__main__':
    try:
        print("Running joint_state.py...")
        talker()
    except rospy.ROSInterruptException:
        pass
