#!/usr/bin/env python3

#モジュールのインポート
import rospy
from geometry_msgs.msg import Turtle

#クラスの定義
class Talker():
    #コンストラクタの定義
    def __init__(self):
        #パブリッシャの生成
        #トピック名、メッセージの型、キューサイズ
        self.turtle1/cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    #メッセージをパブリッシュする関数
    def publish(self):
        #送るメッセージの定義
        msg = Turtle()
        msg.name = "上田 隆一"
        msg.age = 45
        msg.hobbies = ["確率ロボティクス", "シェル芸"]
        
        #メッセージをパブリッシュする
        self.turtle1/cmd_vel_pub.publish(msg)

        #画面に表示
        rospy.loginfo(f"私は{msg.name}、{msg.age}歳！趣味は{hobbies}!")

if __name__ == "__main__":
    #ノードの生成
    rospy.init_node("turtle0_node")

    #クラスのインスタント化
    talker = Talker()

    #ループの周期
    #この場合1Hz、1秒に1回
    rate = rospy.Rate(1)

    #ROSが立ち上がっている間は...
    while not rospy.is_shutdown():
        #メッセージをパブリシュする
        talker.publish()

        #定義した周期になるように一定時間待つ
        rate.sleep()

    #Escapeキーを２秒以上押し続けたらプログラム終了
    while  True:
        if keyboard.is_pressed('escape'):
            messagebox.showinfo('メッセージ','処理を終了しました。')
            sys.exit()
        time.sleep(2)