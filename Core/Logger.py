import os
import time

def logCommand(message, client, command):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    f = open(time.strftime("logs\VinnyLog %m-%d-%Y.txt"), "a+")
    f.write(time.strftime("[%H:%M:%S] ") + command + " called by: " + message.author.name + " in channel: " +
            message.channel.name + " in server: " + message.server.name + "\n")
    f.close()