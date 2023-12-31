"""
Используемые клавиатуры
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
functions = InlineKeyboardMarkup()
(functions
 .add(InlineKeyboardButton(text='Официальный курс валют от ЦБ РФ на сегодня', callback_data='/exchangerate'))
 .add(InlineKeyboardButton(text='Конвертация валют', callback_data='/convert'))
 .add(InlineKeyboardButton(text='Рассчитать платеж по кредиту или ипотеке', callback_data='/credit'))
 .add(InlineKeyboardButton(text='Рассчитать итог вклада', callback_data='/deposit'))
 .add(InlineKeyboardButton(text='Показать экономические показатели страны', callback_data='/countryinfo'))
 .add(InlineKeyboardButton(text='FAQ', callback_data='/FAQ'))
 )

exchangerate_menu = InlineKeyboardMarkup()
(exchangerate_menu
 .add(InlineKeyboardButton('Доллар', callback_data='USD'))
 .add(InlineKeyboardButton('Евро', callback_data='EUR'))
 .add(InlineKeyboardButton('Юань', callback_data='CNY'))
 .add(InlineKeyboardButton('Британский фунт', callback_data='GBP'))
 .add(InlineKeyboardButton('Швейцарский франк', callback_data='CHF'))
 .add(InlineKeyboardButton('Японская иена', callback_data='JPY'))
 .add(InlineKeyboardButton('Турецкая лира', callback_data='TRY'))
 .add(InlineKeyboardButton('Грузинский лари', callback_data='GEL'))
 .add(InlineKeyboardButton('Армянский драм', callback_data='AMD'))
 )

payment_type = InlineKeyboardMarkup()
(payment_type
 .add(InlineKeyboardButton('Дифференцированный', callback_data='DIF'))
 .add(InlineKeyboardButton('Аннуитетный', callback_data='ANU'))
 )

convert_menu = InlineKeyboardMarkup()
(convert_menu
 .add(InlineKeyboardButton('Рубль', callback_data='RUB'))
 .add(InlineKeyboardButton('Доллар', callback_data='USD'))
 .add(InlineKeyboardButton('Евро', callback_data='EUR'))
 .add(InlineKeyboardButton('Юань', callback_data='CNY'))
 .add(InlineKeyboardButton('Британский фунт', callback_data='GBP'))
 .add(InlineKeyboardButton('Швейцарский франк', callback_data='CHF'))
 .add(InlineKeyboardButton('Японская иена', callback_data='JPY'))
 .add(InlineKeyboardButton('Турецкая лира', callback_data='TRY'))
 .add(InlineKeyboardButton('Грузинский лари', callback_data='GEL'))
 .add(InlineKeyboardButton('Армянский драм', callback_data='AMD'))
 )

payment_type = InlineKeyboardMarkup()
(payment_type
 .add(InlineKeyboardButton('Дифференцированный', callback_data='DIF'))
 .add(InlineKeyboardButton('Аннуитетный', callback_data='ANU'))
 )

countryinfo_menu = InlineKeyboardMarkup()
(countryinfo_menu
 .add(InlineKeyboardButton('Россия', callback_data='russia'))
 .add(InlineKeyboardButton('США', callback_data='united-states'))
 .add(InlineKeyboardButton('Китай', callback_data='china'))
 .add(InlineKeyboardButton('Япония', callback_data='japan'))
 .add(InlineKeyboardButton('Германия', callback_data='germany'))
 .add(InlineKeyboardButton('Индия', callback_data='india'))
 .add(InlineKeyboardButton('Великобритания', callback_data='united-kingdom'))
 .add(InlineKeyboardButton('Франция', callback_data='france'))
 .add(InlineKeyboardButton('Канада', callback_data='canada'))
 .add(InlineKeyboardButton('Италия', callback_data='italy'))
 .add(InlineKeyboardButton('Бразилия', callback_data='brazil'))
 .add(InlineKeyboardButton('Австралия', callback_data='australia'))
 )