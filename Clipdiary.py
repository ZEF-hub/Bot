def ------(message):
    try:

    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))
#-----------------------------------------------------------------------------------------------------------------------
msg = bot.send_message(message.chat.id, '')
#-----------------------------------------------------------------------------------------------------------------------
bot.register_next_step_handler(msg, )
#-----------------------------------------------------------------------------------------------------------------------
cursor.execute('CREATE TABLE `articles` (`id` tinyint unsigned NOT NULL auto_increment, `question` varchar(255) default NULL, `answer` text, PRIMARY KEY (`id`), FULLTEXT KEY `ft1` (`question`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;')
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



