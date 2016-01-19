import irclib
import ircbot
import json
from sseclient import SSEClient

print "Bot started"

class BotGamesurge(ircbot.SingleServerIRCBot):
    def __init__(self):
        ircbot.SingleServerIRCBot.__init__(self, [('irc.gamesurge.net', 6667)],
                                           'ActionFPS_BOT', 'ActionFPS inter bot')
    def on_welcome(self, serv, ev):
	channels = ['#million'];
	for i in range(0,len(channels)):
    		print 'Bot joined ' + channels[i]
        	serv.join(channels[i])
	while True:
	        messages = SSEClient('http://woop.ac:81/actionfps/inters/')
        	for message in messages:
                	if message.data:
                        	data = json.loads(message.data)
	                        serverName = str(data['serverName'])
        	                playerName = data['playerName']
                	        serverConnect = data['serverConnect']
                        	event = message.event
	                        msg = playerName + ' started an ' + event + ' and is looking for players on ' + serverName
        	                msg = str(msg)
                	        print msg
				for i in range(0,len(channels)):
			                serv.privmsg(channels[i], msg)

BotGamesurge().start()
