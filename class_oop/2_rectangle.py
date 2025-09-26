import math  # 計算のためのモジュールをインポート


# 次のコードが正しく動作するような Rectangle クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):  # 面積
        return round(float(self.height * self.width), 2)  # 小数点第二位まで表示

    def diagonal(self):  # 対角線
        return round(math.sqrt(self.height**2 + self.width**2), 2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
