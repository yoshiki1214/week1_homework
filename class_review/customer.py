# Customerクラスの定義
class Customer:
    # 初期化メソッド
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # C-1.フルネームを返すメソッド
    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    # C-3.年令に応じた入場料を返すメソッド
    def entry_fee(self):
        if self.age <= 3:
            return 0  # 3歳以下無料(C-5)
        elif 3 < self.age < 20:
            return 1000  # 4~19歳は1,000円
        elif 20 <= self.age < 65:
            return 1500  # 20~64歳は1,500円
        elif 65 <= self.age < 75:
            return 1200  # 65~74歳は1,200円
        elif self.age >= 75:
            return 500  # 75歳以上は500円(C-6)

    # C-4.CSV形式で返すメソッド
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    # C-7.顧客情報をタブ区切りで返すメソッド
    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    # C-8.顧客情報をパイプ区切りで返すメソッド
    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)  # C-5追加データ

# C-1. フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

# C-2. 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

"""
C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円
"""
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力


# C-7. 単一顧客の情報取得形式の追加その1
# 単一顧客の情報取得をタブ区切りにも対応させてください
# 下記は出力の例
print(ken.info_tab())  # Ken Tanaka      15      1000
print(tom.info_tab())  # Tom Ford        57      1500
print(ieyasu.info_tab())  # Ieyasu Tokugawa 75      500
print(michelle.info_tab())  # Michelle Tanner 3       0


# C-8. 単一顧客の情報取得形式の追加その2
# 単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください
# 下記は出力の例
print(ken.info_pipe())  # Ken Tanaka|15|1000
print(tom.info_pipe())  # Tom Ford|57|1500
print(ieyasu.info_pipe())  # Ieyasu Tokugawa|75|500
print(michelle.info_pipe())  # Michelle Tanner|3|0
