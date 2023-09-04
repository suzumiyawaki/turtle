#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

cmd_vel = Twist()
cmd_vel.linear.x = 3.0
cmd_vel.angular.z = 5.0

pose = Pose()
nowRotating = False

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

def update_cmd_vel():
    global cmd_vel
    global nowRotating
    boundary = 1.0
    if (pose.x < boundary or pose.x > 11.08-boundary or pose.y < boundary or pose.y > 11.08-boundary) and not nowRotating:
        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 5.0
        nowRotating = True
    else:
        cmd_vel.linear.x = 3.0
        cmd_vel.angular.z = 0.0
        nowRotating = False

#def teleop_turtle():
if __name__ == '__main__':    
    #ノードの生成
    rospy.init_node('teleop_turtle_node')
    #トピック名、メッセージの型、キューサイズ
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    sub = rospy.Subscriber('pose', Pose, update_pose)

    #ループの周期
    #この場合10Hz、1秒に10回
    rate = rospy.Rate(10)

    #ROSが立ち上がっている間は...
    while not rospy.is_shutdown():

        update_cmd_vel()

        #メッセージをパブリシュする
        pub.publish(cmd_vel)

        #定義した周期になるように一定時間待つ
        rate.sleep()


        key  = input() # 標準入力からキーを読み込む
        print(key)     # 読み込んだキーの値を標準出力へ出力

if key == 'f': # fキーが押されていたら
    break
#while True:
       #if get_key == "":
          # break
#Enterキーを押したらプログラム終了
#while True:
    #if keyboard.is_pressed('a'):
        #sys.exit()
    #time.sleep(2)
            #autonomous_controller

#if __name__ == '__main__':
   # try:
     #   teleop_turtle()
    #except rospy.ROSInterruptException:  
     #   pass

    #import keyboard
#Enterキーを2秒以上押したらプログラム終了
    #while True:
     #   if keyboard.is_pressed('enter'):
      #     sys.exit()
       # time.sleep(2)
            #autonomous_controller