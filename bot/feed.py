#!/usr/bin/env python
# coding=utf-8

import config
import secrets
import telebot
import feedparser
import random
import time
import os

bot = telebot.TeleBot(secrets.token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    check_base(str(message.from_user.id) + '.txt')

    news = []
    for site in config.sites:
        try:
            u = feedparser.parse(site)
            bot.send_message(message.from_user.id, site + ' ... Done')
            random.shuffle(u['entries'])
            news += u['entries']
            random.shuffle(news)
        except Exception as e:
            bot.send_message(message.from_user.id, site + '... Resource temporarily unavailable!')



    old_news = []
    with open(str(message.from_user.id) + '.txt') as base:
        for line in base:
            old_news.append(line)

    counter = 0
    answer = ''
    for feed in news:
        if check_in_base(replacer(feed['title']), old_news) == True:
            
            answer += replacer(feed['title']) + '\n'
            answer += feed['links'][0]['href'] + '\n\n' 
            add_to_base(str(message.from_user.id) + '.txt', replacer(feed['title']))
            old_news.append(replacer(feed['title']) + '\n')
            counter += 1

        if counter >= config.quant:
            bot.send_message(message.from_user.id, answer)
            answer = ''
            counter = 0
            time.sleep(2)


def replacer(string):
    string = string.replace('&nbsp;', ' ').replace('&laquo;', '"').replace('&raquo;', '"')
    string = string.replace("?utm_campaign=news-feed&utm_medium=rss&utm_source=rss-news", "")
    return(string)


def check_base(path):
    if os.path.exists(path):
        base = open(path, 'a+')
    else:
        base = open(path, 'w')
    base.close()


def add_to_base(path, string):
    base = open(path, 'a+')
    base.write(string + '\n')
    base.close()


def check_in_base(string, array):
    if string + '\n' in array:
        return(False)
    return(True)


if __name__ == '__main__':
    bot.infinity_polling()