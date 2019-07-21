from PIL import Image
import pytesseract
from aip import AipOcr
import sys, getopt
import datetime

pytesseract.pytesseract.tesseract_cmd = r"D:\App\Tesseract-OCR\tesseract.exe"

""" 你的 APPID AK SK """
APP_ID = '15995096'
API_KEY = 'Wj2GyYgC750YD38H6YakUlqb'
SECRET_KEY = 'KXxV52SNuxYimiojwDNy3kbtlp73WWIl'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
  
opts,args = getopt.getopt(sys.argv[1:], "hi:o:")

input_file=""
output_file=""
for op, value in opts:
    if op == "-i":
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        sys.exit()

""" 如果有可选参数 """
options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "false"
# options["probability"] = "true"

options["recognize_granularity"]="small"

now = datetime.datetime.now()  
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print("--------图片转文字开始--------")
print(otherStyleTime)
with open(input_file,'rb') as f:
    img = f.read()
    msg = client.handwriting(img,options)
    for i in msg.get('words_result'):
        print(i.get('words'))
print("--------图片转文字结束--------")