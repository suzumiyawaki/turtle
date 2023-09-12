#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#クラスの定義
class Talker():
    #コンストラクタの定義
    def __init__(self):
        #パブリッシャの生成
        #トピック名、メッセージの型、キューサイズ
        self.twist_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=100)
        self.twist_sub = rospy.Subscriber("turtle1/pose", Pose, self.callback)

    #メッセージをパブリッシュする関数 
    def publish(self):
        #送るメッセージの定義
        cmd_vel = Twist()
        cmd_vel.linear.x = 2.5
        cmd_vel.angular.z = -1.0

        #メッセージをパブリッシュする
        self.twist_pub.publish(cmd_vel)

        #画面に表示
        rospy.loginfo(f"Published linear.x:{cmd_vel.linear.x}, angular.z:{cmd_vel.angular.z}")

    def callback(self, data):
        now = rospy.Time.now()
        #rospy.loginfo("now: %f", now.to_sec())
        #画面に表示
        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)

        pose = Pose()
        pose.x = data.x
        pose.y = data.y
        #画面に表示
        rospy.loginfo(f"現在位置は,x:{pose.x},y:{pose.y}")

if __name__ == "__main__":

    #while True:
        #import keyboard
        #if keyboard.is_pressed('enter'):
            #sys.exit()
    
    #ノードの生成
    rospy.init_node("teleop_turtle_node")

    #クラスのインスタンス化
    talker = Talker()

    #ループの周期
    #この場合10Hz、1秒に10回
    rate = rospy.Rate(10)

       #if not key:
           

    #aキーを押したらプログラム終了
    #while True:
        #if keyboard.is_pressed('a'):
            #sys.exit()
        #time.sleep(2)

    #ROSが立ち上がってる間は、、
    while not rospy.is_shutdown():
        #メッセージをパブリッシュする
        talker.publish()

        #定義した周期になるように一定時間待つ
        rate.sleep()