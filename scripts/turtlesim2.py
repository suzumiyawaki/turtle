#!/usr/bin/env python3

import rospy 
from turtlesim.msg import Pose

pose = Pose()

#クラスの定義
class Turtlesim():
    #コンストラクタの定義
    def __init__(self):
        #サブスクライバの生成
        #トピック名、メッセージの型、データを受け取ったら実行する関数
        self.twist_sub = rospy.Subscriber("turtle1/pose", Pose, self.callback)

    #コールバック関数の定義
    def callback(self, data):
        now = rospy.Time.now()
        #rospy.loginfo("now: %f", now.to_sec())
        #画面に表示
        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
        pose.x = data.x
        pose.y = data.y
        #画面に表示
        rospy.loginfo(f"現在位置は,x:{pose.x},y:{pose.y}")

if __name__ == "__main__":
    #ノードの生成、初期化
    rospy.init_node("turtlesim_node")#, anonymous=True) 

    #クラスのインスタンス化
    turtlesim = Turtlesim()

    # Ctrl-Cが押されるまで実行
    rospy.spin()

    


    #try:
        #teleop_turtle()
    #except rospy.ROSInterruptException:
        #pass
#if __name__ == "__main__":
    #ノードの生成
    #rospy.init_node('turtlesim_node', anonymous=True) # ノードの初期化
    #subscriber(pose)
    #pose = "/turtle1/pose"

    #pose_subscriber = rospy.Subscriber('pose', Pose, callback)
 
    # Ctrl-Cが押されるまで実行
    #rospy.spin()

    #rospy.loginfo("node subscribed")
#pose = Pose()
#SnowRotating = False

#def update_pose(data):
    #global pose
    #pose.x = data.x
    #pose.y = data.y
    
    #rospy.init_node('turtlesim_node', anonymous=True)    
    #subscriberの作成。トピックを購読する。    
    #sub = rospy.Subscriber('pose', Pose, callback)
    #rospy.Subscriber('pose', Twist, callback)