#!/usr/bin/env python
import rospy
from hayate_motor_ros.msg import *
from hayate_imu_ros.msg import *
from std_msgs.msg import Float32

PI = 3.1415926

#
# Callback for subscribing /arduino_msg, also publishing pid_params
#
def arduino_info_cb(arduino_msg):
    global pid_params, pub_pid_params, only_3_times

    if(only_3_times):
        pub_pid_params.publish(pid_params)
        #only_3_times -= 1
    rospy.loginfo("[python-node] Kp Ki Kd: %.3f %.3f %.3f, target_velocity: %.2f, current_velocity: %.2f, pwm: %d", pid_params.Kp, pid_params.Ki, pid_params.Kd, pid_params.target_velocity, arduino_msg.current_velocity, arduino_msg.pwm)

#
# Callback for subscribing /imu_data, also publishing angular_velocity.z
#
def imu_data_cb(imu_msg):
    pub_z.publish(-imu_msg.angular_velocity.z * 180.0 / PI)
    #pub_z.publish(-imu_msg.angular_velocity.z)
    #rospy.loginfo("[python-node] imu_data/angular_velocity/z: %.2f", imu_msg.angular_velocity.z)

#
# main for python node
#
def main():
    global pid_params, pub_pid_params, only_3_times, pub_z

    rospy.init_node('hayate_motor_node')
    only_3_times = 3
    pid_params = PidMsgs()
    pid_params.Kp = rospy.get_param('/hayate_motor_node/Kp')
    pid_params.Ki = rospy.get_param('/hayate_motor_node/Ki')
    pid_params.Kd = rospy.get_param('/hayate_motor_node/Kd')
    pid_params.target_velocity = rospy.get_param('/hayate_motor_node/target_velocity')
    pub_pid_params = rospy.Publisher('/pid_params', PidMsgs, queue_size = 1)
    pub_z = rospy.Publisher('/hayate_angular_velocity_z', Float32, queue_size = 1)
    rospy.Subscriber('/arduino_msg', ArduinoMsgs, arduino_info_cb)
    rospy.Subscriber('/imu_data', ImuData, imu_data_cb)
    rospy.loginfo("[python-node] hayate_motor_node started up")
    rospy.spin()

if __name__ == '__main__':
    main()