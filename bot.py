import irclib
import ircbot
 
channels = ['#million', '#million_test']

class Bot(ircbot.SingleServerIRCBot):

    def __init__(self):
        ircbot.SingleServerIRCBot.__init__(self, [('euroserv.fr.quakenet.org', 6667)],
                                           'ActionFPS_BOT', 'ActionFPS inter bot')
    def on_welcome(self, serv, ev):
	for i in range(0,len(channels)):
    		print 'Bot joined ' + channels[i]
        	serv.join(channels[i])
 
Bot().start()

