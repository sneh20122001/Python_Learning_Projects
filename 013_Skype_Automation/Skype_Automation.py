from skpy import Skype
import os.path

slogin = Skype("MAILID","PASSWORD")

contact = slogin.contacts["live:"]
with open("Image Path","rb") as f:
    contact.chat.sendFile()


# contact = slogin.contacts
# contact = slogin.contacts["live:"]
# contact.chat.sendMsg("hello")

# for i in contact:
#     print(i)


group = slogin.chats.create(["",""])