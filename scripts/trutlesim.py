#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import rospy #  rosで必要はモジュール
from geometry_msgs.msg import Twist


def callback(vel):
    rospy.loginfo("Liner:%f",vel.linear.x)
    rospy.loginfo("Angular:%f",vel.angular.z)
    
    
def subscriber():
    rospy.init_node('my_subscriber', anonymous=True) # ノードの初期化

    # subscriberの作成。トピック/cmd_vel_mux/input/teleopを購読する。    
    rospy.Subscriber("/cmd_vel_mux/input/teleop", Twist, callback)

    # コールバック関数を繰り返し呼び出す。
    rospy.spin()
        
if __name__ == '__main__':
    subscriber()
