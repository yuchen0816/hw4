# hw4
## hw4_1
首先輸入position還有d1,d2的距離，

輸入完之後，

連接電腦的xbee會傳送控制車子的訊號到車子上的xbee，

結果車子會根據輸入的資料完成倒退。

## hw4_2
這一部分是讓車子自行跟隨直線前進，

由openmv偵測地上的直線，

得知旋轉的角度後，

再將控制車子的訊號傳送到板子上，

結果車子會根據直線的位置前進。

## hw4_3
這題是偵測某處的apriltag控制車子朝向apriltag移動，

同時用ping測量到apriltag的距離，

由openmv偵測斜前方的apriltag，

得知車子到apriltag上y方向的旋轉角度，

接著再傳送控制車子的訊號，

最後可以看到車子朝著apriltag移動同時間看到車子到apriltag的距離。
