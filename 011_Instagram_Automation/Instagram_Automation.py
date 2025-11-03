from instabot import Bot 

bot = Bot()

bot.login(username= "",
          password = "")
bot.follow("username") 
bot.upload_photo("path")
bot.unfollow("username")

bot.send_message("I love message",["username"])


followers = bot.get_user_followers("username")
for i in followers:
    print(bot.get_user_info(i))