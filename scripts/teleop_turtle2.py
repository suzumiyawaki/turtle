#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

#クラスの定義
class Talker():
    #コンストラクタ(インスタンスを生成した際にまず自動的に呼び出すメソッド)の定義
    def __init__(self):
        #パブリッシャの生成
        #トピック名、メッセージの型、キューサイズ
        self.twist_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

    #メッセージをパブリッシュする関数 
    def publish(self):
        #送るメッセージの定義
        cmd_vel = Twist()
        cmd_vel.linear.x = 2.5
        cmd_vel.linear.y = 2.0
        cmd_vel.angular.z = 1.5

        #メッセージをパブリッシュする
        self.twist_pub.publish(cmd_vel)

        #画面に表示
        rospy.loginfo(f"Published linear.x:{cmd_vel.linear.x}, linear.y:{cmd_vel.linear.y}, angular.z:{cmd_vel.angular.z}")

if __name__ == "__main__":
    
    #ノードの生成
    rospy.init_node("teleop_turtle_node")

    #クラスのインスタンス化・クラス（設計図）を実際に使えるようにする
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

        #aキーを押したらプログラム終了
    #while True:
        #if keyboard.is_pressed('a'):
            #sys.exit()
        #time.sleep(2)