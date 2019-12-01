#Alright
#https://t.me/MrArtan
#https://t.me/XError
import pyrogram, re, redis, sys, os, time
from pyrogram import Client, Filters, Message
from termcolor import colored
from time import sleep
from re import match
#!#!#!#!#!#!#!#!#!#!##!#!#!#!#!#!#!#!#!#!#
print(colored("@MrArtan", "green"))
print(colored("@XError", "red"))
print(colored("Starting bot...", "blue"))
sudo = [583967841, 809993960] #Sudo Users
api_id, api_hash = 'your-Api-id', 'your-Api-Hash' #Api id - Api Hash
token = 'your-Bot-Token' #Bot Token
#!#!#!#!#!#!#!#!#!#!##!#!#!#!#!#!#!#!#!#!#
r = redis.StrictRedis(db=0, decode_responses=True) #Redis Object
bot = Client(session_name='PyRobot', bot_token=token, api_id=api_id, api_hash=api_hash) #Client Object
#!#!#!#!#!#!#!#!#!#!##!#!#!#!#!#!#!#!#!#!#
@bot.on_message(Filters.private & Filters.user(sudo) & Filters.regex(r"^[Pp][Ii][Nn][Gg]$"))
def ping(client:Client, message:Message):
    message.reply('›› Pong....')
@bot.on_message(Filters.private & Filters.user(sudo) & Filters.reply & Filters.regex(r'^([Dd][Nn])\s([\S\s]+)$'), group=1)
def downLoadMedia(client:Client, message:Message):
    try:
        if (message.reply_to_message.document):
            file=(re.match(r"^([Dd][Nn])\s([\S\s]+)$", message.text).group(2))
            if (re.match("([\S\s]+)[.](\w+)", file)):
                message.reply("Uploading File...")
                message.reply_to_message.download(file_name=file)
                time.sleep(0.2)
                s=open("downloads/{}".format(file), "r")
                g=open(file, "w")
                for i in s:
                    g.write(i)
                message.reply('done')
                s.close()
                g.close()
                os.remove("downloads/{}".format(file))
                message.reply("File Uploaded")
    except Exception as e:
        message.reply("Error:{}".format(e))
@bot.on_message(Filters.private & Filters.user(sudo) & Filters.regex(r"^([Oo][Ss])\s([\S\s]+)$"), group=2)
def osW(client:Client, message:Message):
    cmd=(re.match(r"^([Oo][Ss])\s([\S\s]+)$", message.text).group(2))
    message.reply('ok...\n{}'.format(cmd))
    os.system(cmd)
@bot.on_message(Filters.private & Filters.regex(r"^/[Ss]tart$") | Filters.regex(r"^[Hh][Ee][Ll][Pp]$"), group=3)
def osW(client:Client, message:Message):
    if (re.match(r"^[Hh][Ee][Ll][Pp]$", message.text)):
        message.reply("""- راهنمای ربات

- Ping
› تست انلاینی ربات
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
- Dn {FileName.py}
› اپلود فایل روی سرور با اسم مورد نظر
مثال › dn ARTAN.py
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
- Os {CMD}
› اجرای دستور در سرور
مثال› os killall
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
› Os python3 {FileName.py}
›ران کردن اسکریپت پایتون
مثال› os python3 ARTAN.py""")
    elif (re.match(r"^/[Ss]tart$", message.text)):
        message.reply("""این ربات جهت اپلود و اجرای سورس در سرور طراحی شده است.
سورس مورد نظر را ارسال کرده روی آن ریپلی زده و دستور dn {FileName.py} را ارسال کنید.
کلمه {FileName.py} نام سورس بعد از ذخیره شدن در سرور میباشد.
سورس در کنار سورس اصلی و با نام و پسوندی که مشخص کرده اید ذخیره خواهد شد.

برای ران کردن ربات از دستور os python3 {FileName.py} استفاده کنید.
هر کلمه ای که در جلوی دستور OS قرار دهید بصورت مستقیم در سرور اجرا خواهد شد

›› جهت دریافت راهنمای ربات دستور help را ارسال کنید
› Dev : @MrArtan""")

#!#!#!#!#!#!#!#!#!#!##!#!#!#!#!#!#!#!#!#!#
bot.start() # Logger.py
