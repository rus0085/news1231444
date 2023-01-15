import time
import sqlite3
import requests
from bs4 import BeautifulSoup as BS
import re
import telebot
from telebot import types

token = '********************'
bot = telebot.TeleBot(token)

def nft_arty(message):


    response = requests.get('https://nft-arty.com/ru/novosti/?ysclid=l3h7p8fai4')
    html = BS (response.content,"html.parser")
    y = html.find(id = "content")
    u = y.find(class_ = "w-view clear")

    o = u.find(class_="w-item col-6")
    j = str(o.find("a")).split(">")[0].split('"')[1]
    png = str(o).split('data-src="')[1].split('"')[0]
    connector = sqlite3.connect('news_link.db')
    cursor = connector.cursor()
    cursor.execute(
        "SELECT count(*) FROM news_link WHERE link= ?",
        (j,))
    yess = cursor.fetchone()

    if yess[0] == 0:
        cursor.execute(f"INSERT INTO news_link VALUES(?)", (j,))
        connector.commit()
        news = requests.get(j)
        html = BS(news.content, "html.parser")
        title = html.find(class_="title entry-title").text.upper()
        text5 = html.find(class_="entry-content").text.splitlines()
        try:
            text_itog = f"""*{title}*
        
{text5[1]}

{text5[2]}

{text5[3]}

{text5[4]}

{text5[5]}

[NFT головного мозга](https://t.me/+Jj83xA-DNyhmN2Iy) | [Всё об NFT](https://t.me/+Jj83xA-DNyhmN2Iy)

        """
        except:
            1
        bot.send_photo(chat_id = message.from_user.id , caption=text_itog, photo= png ,parse_mode="Markdown")
        bot.send_message(message.from_user.id , j)

def cryptonews(message):
    response = requests.get('https://cryptonews.net/ru/news/nft/?ysclid=l3h7p5sokw')
    html = BS(response.content, "html.parser")
    y = html.find(class_="col-xs-12 col-sm")
    u = str(y.find(class_="row news-item start-xs"))

    j = "https://cryptonews.net"+ u.split("href=")[1].split('"')[1]

    png = str(u).split('data-src="')[1].split('"')[0]

    connector = sqlite3.connect('news_link.db')
    cursor = connector.cursor()
    cursor.execute(
        "SELECT count(*) FROM news_link WHERE link= ?",
        (j,))
    yess = cursor.fetchone()

    if yess[0] ==  0:
        cursor.execute(f"INSERT INTO news_link VALUES(?)", (j,))
        connector.commit()
        news = requests.get(j)
        html = BS(news.content, "html.parser")
        title = html.find(class_="article_title").text.upper()
        text5 = html.find(class_="news-item detail content_text").text.splitlines()
        try:
            text_itog = f"""*{title}*

{text5[23]}

{text5[24]}

{text5[25]}
    
{text5[26]}
    
{text5[27]}
    

    [*************) | [Всё об NFT](*************)

            """
        except:
            1
        bot.send_photo(chat_id=message.from_user.id, caption=text_itog, photo=png, parse_mode="Markdown")
        bot.send_message(message.from_user.id , j)

@bot.message_handler(commands=["start"])

def start_def(message):
    while 1 == 1:
       nft_arty(message)
       cryptonews(message)

if 1:
    bot.infinity_polling(skip_pending=True)
