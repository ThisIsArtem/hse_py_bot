from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dispatcher import dp
from handlers.keyboards import functions, convert_menu, payment_type, countryinfo_menu, exchangerate_menu
from Classes.Converter import CurrencyConvertor
from Classes.StringFormat import StringFormat
from Classes.Credit import Credit
from Classes.CountryInfo import CountryInfo
from Classes.ExchangeRate import ExchangeRate


class ExchangeRateStates(StatesGroup):
    choose_currency = State()


class CountryinfoStates(StatesGroup):
    choose_country = State()


class ConvertingStates(StatesGroup):
    src = State()
    dst = State()
    amount = State()


class CreditStates(StatesGroup):
    amount = State()
    period = State()
    perc = State()
    type = State()


class DepositStates(StatesGroup):
    amount = State()
    period = State()
    perc = State()


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    start_message = "Меня зовут Финбо, и я твой персональный финансовый ассистент. \nВот что я умею:\n"
    await message.answer(start_message, reply_markup=functions)


@dp.callback_query_handler(text='/FAQ')
async def start_cmd(callback: types.CallbackQuery):
    FAQ_message = (f"Этот бот был разработан в качестве итогового проекта по дисциплине 'Программирование на Python'"
                   f"\nБот разработал студент КНАД ФКН ВШЭ [https://t.me/Itisartemka]. Буду рад любой обратной связи!"
                   f"\nФункции бота:")
    await callback.message.answer(FAQ_message, reply_markup=functions)


@dp.callback_query_handler(text='/exchangerate')
async def exchange_cmd(callback: types.CallbackQuery):
    await callback.message.answer('Курс какой валюты Вас интересует?', reply_markup=exchangerate_menu)
    await ExchangeRateStates.choose_currency.set()


@dp.callback_query_handler(state=ExchangeRateStates.choose_currency)
async def exchange_cmd_src(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['src'] = callback.data
    exchangerate = ExchangeRate(data['src']).get_info()
    await callback.message.answer(f'Вот что у меня получилось:\n'
                                  f'1{data["src"]} = {exchangerate}RUB')
    await state.finish()
    await callback.message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.callback_query_handler(text='/convert')
async def convert_cmd(callback: types.CallbackQuery):
    await callback.message.answer('Из какой валюты будет происходить конвертация?', reply_markup=convert_menu)
    await ConvertingStates.src.set()


@dp.callback_query_handler(state=ConvertingStates.src)
async def convert_cmd_src(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['src'] = callback.data
    await callback.message.answer('В какую валюту переводим?', reply_markup=convert_menu)
    await ConvertingStates.dst.set()


@dp.callback_query_handler(state=ConvertingStates.dst)
async def convert_cmd_dst(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['dst'] = callback.data
    await callback.message.answer('Какую сумму переводим?\n')
    await ConvertingStates.amount.set()


@dp.message_handler(state=ConvertingStates.amount)
async def convert_cmd_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = StringFormat(message.text).number_format()
        data['amount'] = amount
        try:
            convert = CurrencyConvertor(data.get("src"), data.get("dst"), float(data.get("amount")))
            convert_result = convert.convertor()
            await message.answer(f'Курс на {convert_result[0]}\n\n'
                                 f'{data.get("amount")} {data.get("src")} это примерно '
                                 f'{round(convert_result[1], 4)} {data.get("dst")}\n\n'
                                 f'Внимание! Расчеты производятся не по официальному курсу, а по '
                                 f'околобиржевому курсу, который предоставляет exchangerate-api.com.'
                                 f'Все расчеты носят примерный характер. '
                                 f'Для более точной конвертации обратитесь в банк или обменный пункт')
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
    await state.finish()
    await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.callback_query_handler(text='/credit')
async def credit_cmd(callback: types.CallbackQuery):
    await callback.message.answer('Какова сумма кредита или ипотеки?')
    await CreditStates.amount.set()


@dp.message_handler(state=CreditStates.amount)
async def credit_cmd_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = StringFormat(message.text).number_format()
        try:
            data['amount'] = float(amount)
            await message.answer(f'На какой период Вы берете кредит или ипотеку? (в годах)')
            await CreditStates.period.set()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
            await state.finish()
            await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.message_handler(state=CreditStates.period)
async def credit_cmd_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        period = StringFormat(message.text).number_format()
        try:
            data['period'] = float(period)
            await message.answer(f'Под какой процент Вы берете кредит или ипотеку?')
            await CreditStates.perc.set()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
            await state.finish()
            await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.message_handler(state=CreditStates.perc)
async def credit_cmd_perc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        perc = StringFormat(message.text).number_format()
        try:
            data['perc'] = float(perc)
            await message.answer(f'Какой тип платежа планируется?', reply_markup=payment_type)
            await CreditStates.type.set()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
            await state.finish()
            await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.callback_query_handler(state=CreditStates.type)
async def credit_cmd_type(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = callback.data
        credit = Credit(data['amount'], data['period'], data['perc'])
    if data['type'] == 'ANU':
        credit_result = credit.ann_int()
        await callback.message.answer(f'Вот что у меня получилось:\n'
                                      f'Ежемесячный платеж составит {credit_result[0]} рублей\n'
                                      f'Всего Вы заплатите банку {credit_result[1]} рублей\n'
                                      f'Все расчеты носят примерный характер. '
                                      f'Для более точной конвертации обратитесь в банк')
    else:
        credit_result = credit.dif_int()
        await callback.message.answer(f'Вот что у меня получилось:\n'
                                      f'Всего Вы заплатите банку {credit_result[1]} рублей\n'
                                      f'Среднемесячный платеж составляет {credit_result[0]}'
                                      f'Все расчеты носят примерный характер. '
                                      f'Для более точной конвертации обратитесь в банк')
    await state.finish()
    await callback.message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.callback_query_handler(text='/deposit')
async def deposit_cmd(callback: types.CallbackQuery):
    await callback.message.answer('Какую сумму Вы хотите положить под проценты?')
    await DepositStates.amount.set()


@dp.message_handler(state=DepositStates.amount)
async def deposit_cmd_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = StringFormat(message.text).number_format()
        try:
            data['amount'] = float(amount)
            await message.answer(f'Каков срок вклада? (в месяцах)')
            await DepositStates.period.set()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
            await state.finish()
            await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.message_handler(state=DepositStates.period)
async def deposit_cmd_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        period = StringFormat(message.text).number_format()
        try:
            data['period'] = float(period)
            await message.answer(f'Каков процент вклада?')
            await DepositStates.perc.set()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
            await state.finish()
            await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.message_handler(state=DepositStates.perc)
async def deposit_cmd_perc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        perc = StringFormat(message.text).number_format()
        try:
            data['perc'] = float(perc)
            deposit = Credit(data['amount'], data['period'], data['perc'])
            deposit_result = deposit.deposit_total_amount()
            await message.answer(f'Вот что у меня получилось:\n'
                                 f'Итоговая сумма вклада составит {deposit_result} рублей\n'
                                 f'Все расчеты носят примерный характер. '
                                 f'Для более точной конвертации обратитесь в банк')
            await state.finish()
        except ValueError:
            await message.answer("Не обманывай Финбо, Финбо очень грустит, когда его обманывают!🥺")
        await state.finish()
        await message.answer(text='Чем еще я могу помочь?', reply_markup=functions)


@dp.callback_query_handler(text='/countryinfo')
async def countryinfo_cmd(callback: types.CallbackQuery):
    await callback.message.answer('Информацию о какой стране Вы хотите получить??', reply_markup=countryinfo_menu)
    await CountryinfoStates.choose_country.set()


@dp.callback_query_handler(state=CountryinfoStates.choose_country)
async def countryinfo_cmd_src(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = callback.data
    countryinfo = CountryInfo(data['country'])
    countryinfo_result = countryinfo.get_info()
    await callback.message.answer(f'Вот какую информацию мне удалось найти:\n'
                                  f'Годовой темп прироста ВВП: {countryinfo_result[0]}% к прошлому году\n'
                                  f'Уровень безработицы: {countryinfo_result[1]}%\n'
                                  f'Уровень инфляции: {countryinfo_result[2]}% к прошлому году\n'
                                  f'Текущая процентная ставка: {countryinfo_result[3]}%\n\n'
                                  f'Информация с сайта https://tradingeconomics.com/')
    await state.finish()
    await callback.message.answer(text='Чем еще я могу помочь?', reply_markup=functions)
