import numpy as np             
import pyrealsense2 as rs      

pipeline = rs.pipeline()
config = rs.config()
# Configuring streams at different rates
# Accelerometer available FPS: {63, 250}Hz
config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 250)  # acceleration
# Gyroscope available FPS: {200,400}Hz
config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)  # gyroscope
pipeline.start(config)
  
while True:
    frames = pipeline.wait_for_frames()      
    for frame in frames:       
        motion_data = frame.as_motion_frame().get_motion_data()
        print(np.array([motion_data.x, motion_data.y, motion_data.z]))

