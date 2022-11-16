import telebot,requests
from telebot import types
bot = telebot.TeleBot('5765648378:AAE_ucNFr0rcasowVTG90Q9RKNsdbItdSxM')
@bot.message_handler(commands=['start'])
def huks(message):
     
         req = requests.get(f'https://api.telegram.org/bot5345560978:AAEkugO1LnnH0iw4e68hcU1xNgdoE_xYh8g/getchatmember?chat_id=@huks_3&user_id={message.from_user.id}')
         req1 = requests.get(f'https://api.telegram.org/bot5345560978:AAEkugO1LnnH0iw4e68hcU1xNgdoE_xYh8g/getchatmember?chat_id=@huks_4&user_id={message.from_user.id}')
         sudo_id = '1887927704'
         idd = message.from_user.id
         if idd == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text :
             if idd == sudo_id or 'member' in req1.text or 'creator' in req1.text or 'administartor' in req1.text :
                 bb = open("ban.txt","r")
                 b = open('user.txt').read()
                 bo = open('ban.txt').read()
                 if str(message.from_user.id) in b:
                   
                     if message.from_user.id == 1887927704:
                         ooi = open("user.txt","r")
                         o =len(ooi.readlines())
                         oi = len(bb.readlines())
                         bot.reply_to(message,f'اهلا بك ايها المطور\nعدد مستخدمين البوت {o}\nعدد المحظورين {oi}\nلحظر شخص ارسل حظر + الايدي')
                     elif str(message.from_user.id) in bo:
                         
                             bot.reply_to(message,'تم حظرك من البوت راسل المطور لفكه @huks3')
                         
                             
                     else:
                         
                             key = types.InlineKeyboardMarkup()
                             key.row_width = 1
                             btn2 = types.InlineKeyboardButton(text="- Dev",url="t.me/huks3")
                             key.add(btn2)
                             bot.send_photo(message.chat.id,'https://t.me/hdidveue/13',caption='Welcome in bot information of TikTok send your username\nاهلا بك في بوت معلومات التيك توك ارسل يوزرك',reply_markup=key)
                         
                         
                 else:
                     ooi = open("user.txt","r")
                     o =len(ooi.readlines())
                     bot.send_message(1887927704,f'- تم دخول شخص جديد الى البوت (:\nاليوزر : @{message.from_user.username}\nالاسم : {message.from_user.first_name}\nالايدي : {message.from_user.id}\nعدد اعضاء البوت : {o}')
                     open('user.txt','a').write(f'\n{message.from_user.id}')
                     key = types.InlineKeyboardMarkup()
                     key.row_width = 1
                     btn2 = types.InlineKeyboardButton(text="- Dev",url="t.me/huks3")
                     key.add(btn2)
                     
                     bot.send_photo(message.chat.id,'https://t.me/hdidveue/13',caption='Welcome in bot information of TikTok send your username\nاهلا بك في بوت معلومات التيك توك ارسل يوزرك',reply_markup=key)
             else:
                 bot.reply_to(message,'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/huks_4

    ‼️| اشترك ثم ارسل /start''')
         else:
             
                 bot.reply_to(message,'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/huks_3

    ‼️| اشترك ثم ارسل /start''')
             
@bot.message_handler(regexp='المحظورين')
def f(message):
    bot.reply_to(message,open('ban.txt').read())
@bot.message_handler(regexp='اذاعة')
def jj(message):
    
    msg = message.text.replace('اذاعة ','')
    h = open('user.txt','r').readlines()
    for id in h:
                bot.send_message(id,msg)
                pass          
@bot.message_handler(regexp='حظر')
def f(message):
    if message.from_user.id == 1887927704:
        id = message.text.replace('حظر ','')
        open('ban.txt','a').write(f'\n{id}')
        bot.reply_to(message,f'تم حظر {id} بنجاح')
    else:
        bot.reply_to(message,'انت لست المطور')
@bot.message_handler(func=lambda m:True)
def h(message):
     req = requests.get(f'https://api.telegram.org/bot5345560978:AAEkugO1LnnH0iw4e68hcU1xNgdoE_xYh8g/getchatmember?chat_id=@huks_3&user_id={message.from_user.id}')
     req1 = requests.get(f'https://api.telegram.org/bot5345560978:AAEkugO1LnnH0iw4e68hcU1xNgdoE_xYh8g/getchatmember?chat_id=@huks_4&user_id={message.from_user.id}')
     sudo_id = '1887927704'
     idd = message.from_user.id
     if idd == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text :
        if idd == sudo_id or 'member' in req1.text or 'creator' in req1.text or 'administartor' in req1.text :
            b = open('ban.txt').read()
           
            if str(message.from_user.id) in b:
                bot.reply_to(message,'تم حظرك من البوت راسل المطور لفكه @huks3')
            else:
                
                bot.reply_to(message,'انتظر...')
                user= message.text.replace('تيك ','')
                u=requests.get(f'https://api.dlyar-dev.tk/info-tiktok.json?user={user}').json()
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{user}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                bio=''
                yc=''
                insta = ''
                try:
                      yc = r["data"]["youtube_channel_id"]
                except:
                      yc='not found'
                try:
                      bio = r["data"]["signature"]
                except:
                      bio = 'not found'
    
                try:
                      insta = r["data"]["ins_id"]
                except:
                      insta = 'not found'
                if u['status']==True:
                    co = f'{u["country"]} , {u["code-country"]} - {u["flag"]}'
                    h = u['likes']
                    name = u['name']
                    fs = u['followers']
                    fg = u['following']
                    p = u['img']
                    id = u['id']
                    bot.send_photo(message.chat.id,r['data']['avatar_300x300']['url_list'][0],f'''• Name : {name}

• Followers : {fs}

• Following : {fg}

• Bio : {bio}

• Likes : {h}

• iNSTA : {insta}

• Youtube : {yc}

• iD : {id}

• Country : {co}
 = = = = = = = = = = = = = = = = = = = = 
By : @Huks3 Ch : @Huks_3''',reply_to_message_id=message.message_id)
        
                else:
                    bot.reply_to(message,u)
        else:
                 bot.reply_to(message,'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/huks_4

    ‼️| اشترك ثم ارسل /start''')
     else:
         bot.reply_to(message,'''🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- https://t.me/huks_3

‼️| اشترك ثم ارسل /start''')

bot.infinity_polling()
