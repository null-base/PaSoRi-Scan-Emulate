import csv
import nfc
import struct

def on_startup(target):
    with open('tag_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            idm = row[0]
            pmm = row[1]
            sys = '88B4'  
            break

    target.sensf_res = bytearray.fromhex('01' + idm + pmm + sys)

    target.brty = "212F"

    return target

def on_connect(tag):
    print("tag activated")
    return tag

with nfc.ContactlessFrontend('usb:054c:06c1') as clf:
    clf.connect(card={'on-startup': on_startup, 'on-connect': on_connect})
