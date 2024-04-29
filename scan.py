import csv
import nfc

clf = nfc.ContactlessFrontend("usb")
tag = clf.connect(rdwr={'on-connect': lambda tag: False})

# スキャンされたIDとPMMを取得
idm = tag.identifier.hex()
pmm = tag.pmm.hex()

# CSVファイルに既存のデータが存在するかチェック
existing_data = set()
filename = "tag_data.csv"

try:
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        existing_data = set(tuple(row) for row in reader)
except FileNotFoundError:
    pass

# データがCSVファイルに存在しない場合は追加
data = [(idm, pmm)]
new_data = [row for row in data if tuple(row) not in existing_data]

if new_data:
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_data)
        print("ID and PMM have been saved to the CSV file.")
else:
    print("Duplicate entry found. Data not added to the CSV file.")
