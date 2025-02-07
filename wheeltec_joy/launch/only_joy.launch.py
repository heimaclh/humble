import os
from pathlib import Path
from launch import LaunchDescription
import launch_ros.actions
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
def generate_launch_description():

    axis_linear = LaunchConfiguration('axis_linear', default='1')
    axis_angular = LaunchConfiguration('axis_angular', default='0')  
    v_linear = LaunchConfiguration('v_linear', default='0.3')
    v_angular = LaunchConfiguration('v_angular', default='0.5')  
      
    return LaunchDescription([
        launch_ros.actions.Node(
            package='joy', 
            executable='joy_node',
            name='joy_node', 
            output="screen",),

        launch_ros.actions.Node(
            package='wheeltec_joy', 
            executable='wheeltec_joy',
            name='wheeltec_joy',  
            parameters=[{'axis_linear': axis_linear, 
                         'axis_angular': axis_angular, 
                         'v_linear': v_linear,
                         'v_angular': v_angular}],
            output="screen",)

  ])
