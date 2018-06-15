import time
import datetime
import telegram
from telegram.ext import Updater

pualBot = telegram.Bot(token='576441925:AAGE_O8rtJ70pU5UqtO_r0tD-ldrTUnvTjc')

zhenruBot  = telegram.Bot(token='605119890:AAFLpkOguOSDexbm5Gmbm2bMEP8veKrjIq8')

groupID = -277055326         # change group id to alza

messages = ["What's ICO?",
			"ICO stands for 'initial coin offering,' and refers to the creation and sale of digital tokens. In an ICO, a project creates a certain amount of a digital token and sells it to the public, usually in exchange for other crypto currencies such as bitcoin or ether.",
			"Does ALZA start their ICO yet?",
			"ALZA don't have a ICO right now, but they post their roadmap on alza official website now.",
			"Oh what? They update their webpage?",
			"Yea, don't you see that? They updated a lot of detail   from the previous version. They even change their template. ",
			"Wow, ALZA did update their web page, it looks like they are willing for spend maximum effort to this project. ",
			"ALZA's transaction is faster than EOS, what! It can reach 140K transaction per second."]

messageLen = len(messages)

pualUpdater = Updater(token='576441925:AAGE_O8rtJ70pU5UqtO_r0tD-ldrTUnvTjc')

zhenruUpdater = Updater(token='605119890:AAFLpkOguOSDexbm5Gmbm2bMEP8veKrjIq8')

pualDispatcher = pualUpdater.dispatcher

zhenruDispatcher = zhenruUpdater.dispatcher


print('Running!')

while True:
	now = datetime.datetime.now()
	hour = now.hour

	if hour >= 18 and hour <= 20:            #if hour >= 6 and hour <= 11:                

		for i in range(messageLen):

			if i % 2 == 0:

				pualBot.send_message(chat_id=groupID, text=messages[i])
				time.sleep(1)          #time.sleep(120) 
				                              
			else:

				zhenruBot.send_message(chat_id=groupID, text=messages[i])
				time.sleep(1)          #time.sleep(120) 
    






