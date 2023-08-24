# hayate_motor_ros

Using 9axis-imu hayate_imu in this project to evaluate whether the A/B phase pulses of the encoder, which is the basis for calculating the rotation speed of motor output shaft, are correctly measured or not, and to evaluate the accuracy and accuracy of DC motor PID control.

# Required ROS packages or LIBs

rosserial
hayate_motor_ros
hayate_imu_ros
ros_lib by rosserail_arduino with Arduino IDE
Adafruit-Motor-Shield-library-leonardo
arduino_node(ino) on Leonardo with Arduino IDE 

# ROS node interaction status

<img src="https://github.com/soarbear/hayate_motor_ros/blob/master/rqt_graph_hayate_motor.png" alt="hayate_motor_ros ROS node interaction status" title="hayate_motor_ros ROS node interaction status" />

# Launch

roslaunch hayate_imu_ros hayate_imu.launch
roslaunch hayate_motor_ros hayate_motor.launch

# Evaluation environment

DC motor PID control evaluation environment using hayate_imu.

<img src="https://github.com/soarbear/hayate_motor_ros/blob/master/motor_pid_control_evaluation_environment.jpg" alt="motor_pid_control_evaluation_environment" title="motor_pid_control_evaluation_environment" />

# PID control curve

Target value of PID control, rotation speed by encoder, rotation speed curve measured by hayate_imu.

<img src="https://github.com/soarbear/hayate_motor_ros/blob/master/pid_anguler_velocity_by_hayate_imu_encoder_counter.png" alt="pid_anguler_velocity_by_hayate_imu_encoder_counter" title="pid_anguler_velocity_by_hayate_imu_encoder_counter" />

# PWM pulse

PWM pulse by oscilloscope.

<img src="https://github.com/soarbear/hayate_motor_ros/blob/master/pid_pwm_wave_by_oscilloscope.jpg" alt="pid_pwm_wave_by_oscilloscope" title="pid_pwm_wave_by_oscilloscope" />

# For more information...

<a href="https://memo.soarcloud.com/encoder-motor-pid-control-with-hayate_imu/">https://memo.soarcloud.com/encoder-motor-pid-control-with-hayate_imu/</a>
