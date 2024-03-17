import telegram
import os
import random
from time import sleep


tg_token = os.environ['TG_TOKEN']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=tg_token)
while True:
  files = os.listdir("images")
  random.shuffle(files)
  for file in files:
    filepath = os.path.join("images", file)
    with open(filepath, 'rb') as f:
      # bot.send_document(chat_id=chat_id, document=f)
      # sleep(10)