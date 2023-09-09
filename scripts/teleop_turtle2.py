#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

#クラスの定義
class Talker():
    #コンストラクタの定義
    def __init__(self):
        #パブリッシャの生成
        #トピック名、メッセージの型、キューサイズ
        self.twist_pub = rospy.Publisher("cmd_vel", Twist, queue_size=100)

    #メッセージをパブリッシュする関数
    def publish(self):
        #送るメッセージの定義
        cmd_vel = Twist()
        cmd_vel.linear.x = 3.0
        cmd_vel.angular.z = 2.0

        #メッセージをパブリッシュする
        self.twist_pub.publish(cmd_vel)

if __name__ == "__main__":
    #ノードの生成
    rospy.init_node("teleop_turtle_node")

    #クラスのインスタンス化
    talker = Talker()

    #ループの周期
    #この場合10Hz、1秒に10回
    rate = rospy.Rate(10)

    #ROSが立ち上がってる間は、、
    while not rospy.is_shutdown():
        #メッセージをパブリッシュする
        talker.publish()

        #定義した周期になるように一定時間待つ
        rate.sleep()