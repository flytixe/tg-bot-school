import asyncio
import os
from aiogram import Dispatcher, types, F
from ccore.settings import bot, main, help
from aiogram.filters import CommandStart, Command
from aiogram.types.input_file import FSInputFile
from aiogram.types import CallbackQuery
import ccore.keybord as kb
import ccore.settings as st
dp = Dispatcher()


async def start():
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def main_command(message: types.Message):
    await message.reply(text="""Бот начал свою работу,выберите нужные вам действия""", reply_markup=kb.mainkb)
    await message.delete()


@dp.message(F.text.lower() == "список учеников")
async def student(message: types.Message):
    await message.reply("Выберите класс:", reply_markup=kb.class_obr)


@dp.callback_query(lambda callback: callback.data == 'five_cl')
async def five_cl(callback: types.CallbackQuery):
    await callback.message.answer('Наши пятиклашки', reply_markup=kb.clas_sk)


@dp.callback_query(lambda callback: callback.data == 'six_cl')
async def six_cl(callback: types.CallbackQuery):
    await callback.message.answer('Наши шестиклашки', reply_markup=kb.six_class_sk)


@dp.callback_query(lambda callback: callback.data == 'seven_cl')
async def seven_cl(callback: types.CallbackQuery):
    await callback.message.answer("Наши семиклашки", reply_markup=kb.seven_clas_sk)


@dp.callback_query(lambda callback: callback.data == 'eight_cl')
async def eight_cl(callback: types.CallbackQuery):
    await callback.message.answer("Наши восьмиклашки", reply_markup=kb.eight_clas_sk)


@dp.callback_query(lambda callback: callback.data == 'nine_cl')
async def nine_cl(callback: types.CallbackQuery):
    await callback.message.answer("Наши девятиклассники", reply_markup=kb.nine_clas_sk)


@dp.callback_query(lambda callback: callback.data == 'ten_cl')
async def ten_cl(callback: types.CallbackQuery):
    await callback.message.answer("Наши десятиклассники", reply_markup=kb.ten_clas_sk)


@dp.callback_query(lambda callback: callback.data == 'eleven_cl')
async def eleven_cl(callback: types.CallbackQuery):
    await callback.message.answer("Наши выпускники", reply_markup=kb.eleven_clas_sk)


@dp.callback_query(lambda callback: '11' in callback.data)
async def eleven_class(callback: types.callback_query):
    class_responses = [
        ("11a", st.eleven_A),
        ("11b", st.eleven_B),
        ("11v", st.eleven_V),
        ("11g", st.eleven_G),
        ("11d", st.eleven_D),
        ("11e", st.eleven_E)
    ]
    my_class = callback.data.lower()
    for data in class_responses:
        if my_class == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '10' in callback.data)
async def ten_class(callback: types.callback_query):
    class_responses = [
        ("10a", st.ten_A),
        ("10b", st.ten_B),
        ("10v", st.ten_V),
        ("10g", st.ten_G),
        ("10d", st.ten_D),
        ("10e", st.ten_E),
        ("10zh", st.ten_ZH)
    ]
    my_class = callback.data.lower()
    for data in class_responses:
        if my_class == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '9' in callback.data)
async def nine_class(callback: types.CallbackQuery):
    class_responses = [
        ('9a1', st.nine_A1),
        ('9a2', st.nine_A2),
        ('9a3', st.nine_A3),
        ('9b1', st.nine_B1),
        ('9b2', st.nine_B2),
        ('9b3', st.nine_B3),
        ('9v2', st.nine_V2),
        ('9v3', st.nine_V3),
        ('9v2', st.nine_G1),
        ('9v3', st.nine_G2),
        ('9v3', st.nine_G3),
        ('9m2', st.nine_M2),
        ('9f1', st.nine_F1),
        ('9f2', st.nine_F2),
        ('9h2', st.nine_H2)

    ]
    my_class = callback.data.lower()
    for data in class_responses:
        if my_class == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '8' in callback.data)
async def eight_class(callback: types.CallbackQuery):
    class_responses = [
        ('8a1', st.eight_A1),
        ('8a2', st.eight_A2),
        ('8v2', st.eight_V2),
        ('8v3', st.eight_V3),
        ('8g1', st.eight_G1),
        ('8g3', st.eight_G2),
        ('8g3', st.eight_G3),
        ('8d1', st.eight_D1),
        ('8d2', st.eight_D2),
        ('8e1', st.eight_E1),
        ('8e2', st.eight_E2),
        ('8zh1', st.eight_ZH1),
        ('8f2', st.eight_F2),
        ('8f3', st.eight_F3),
        ('8h1', st.eight_H1),
        ('8h2', st.eight_H2),

    ]
    my_class = callback.data.lower()
    for data in class_responses:
        if my_class == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '7' in callback.data)
async def seven_class(callback: types.CallbackQuery):
    class_responses = [
        ('7a1', st.seven_A1),
        ('7a2', st.seven_A2),
        ('7a3', st.seven_A3),
        ('7b1', st.seven_B1),
        ('7b2', st.seven_B2),
        ('7b3', st.seven_B3),
        ('7v1', st.seven_V1),
        ('7v2', st.seven_V2),
        ('7v3', st.seven_V3),
        ('7g1', st.seven_G1),
        ('7g2', st.seven_G2),
        ('7d1', st.seven_D1),
        ('7d2', st.seven_D2),
        ('7e1', st.seven_E1),
        ('7e2', st.seven_E1),
        ('7zh1', st.seven_ZH1),
        ('7zh2', st.seven_ZH2),
        ('7z1', st.seven_Z1),
        ('7f1', st.seven_F1),
        ('7f2', st.seven_F2),
        ('7f3', st.seven_F3),
        ('7h2', st.seven_H2),
        ('7h3', st.seven_H3),
    ]
    my_class = callback.data.lower()
    for data in class_responses:
        if my_class == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '6' in callback.data)
async def six_class(callback: types.CallbackQuery):
    class_responses = [
        ('6a1', st.six_A1),
        ('6a2', st.six_A2),
        ('6a3', st.six_A3),
        ('6b1', st.six_B1),
        ('6b2', st.six_B2),
        ('6b3', st.six_B3),
        ('6v1', st.six_V1),
        ('6v2', st.six_V2),
        ('6v3', st.six_V3),
        ('6g1', st.six_G1),
        ('6g2', st.six_G2),
        ('6g3', st.six_G3),
        ('6d1', st.six_D1),
        ('6d2', st.six_D2),
        ('6e1', st.six_E1),
        ('6e2', st.six_E2),
        ('6zh1', st.six_ZH1),
        ('6zh2', st.six_ZH2),
        ('6z1', st.six_Z1),
        ('6z2', st.six_Z2),
        ('6i1', st.six_I1),
        ('6k1', st.six_K1)
    ]
    class_name = callback.data.lower()
    for data in class_responses:
        if class_name == data[0]:
            await callback.message.answer(data[1])
            break


@dp.callback_query(lambda callback: '5' in callback.data)
async def five_class(callback: types.CallbackQuery):
    class_responses = [
        ('5a1', st.five_A1),
        ('5a2', st.five_A2),
        ('5a3', st.five_A3),
        ('5b1', st.five_B1),
        ('5b2', st.five_B2),
        ('5b3', st.five_B3),
        ('5g1', st.five_G1),
        ('5g2', st.five_G2),
        ('5g3', st.five_G3),
        ('5d1', st.five_D1),
        ('5d2', st.five_D2),
        ('5d3', st.five_D3),
        ('5e1', st.five_E1),
        ('5e2', st.five_E2),
        ('5zh1', st.five_ZH1),
        ('5zh2', st.five_ZH2),
        ('5z1', st.five_Z1),
        ('5z2', st.five_Z2),
        ('5i1', st.five_I1),
        ('5i2', st.five_I2),
        ('5k1', st.five_K1)
    ]

    class_name = callback.data.lower()

    for class_data in class_responses:
        if class_name == class_data[0]:
            await callback.message.answer(class_data[1])
            break


@dp.callback_query(lambda callback: 'five' in callback.data)
async def raspis_five(callback: types.CallbackQuery):
    class_respons = [
        ('fivea', 'AgACAgIAAxkBAAIGO2XrddRfXvcVsm6_2vxvLM1xKOUPAAJp2DEbmLNhS2kErhmQhTHAAQADAgADeQADNAQ'),
        ('fiveb', 'AgACAgIAAxkBAAIGPWXrdoKrtyzhXvvcsTWBbXG25juvAAJq2DEbmLNhS46c-RXU5SmfAQADAgADeQADNAQ'),
        ('fivev', 'AgACAgIAAxkBAAIGP2XrdprEWbMiTjI7CPMVsevGjm2eAAJr2DEbmLNhSw9kJphaXDFUAQADAgADeQADNAQ'),
        ('fiveg', 'AgACAgIAAxkBAAIGQWXrdqFlkHU0TwRIdnfZsLmnb5lUAAJu2DEbmLNhS_Oo1b93E7mGAQADAgADeQADNAQ'),
        ('fived', 'AgACAgIAAxkBAAIGQ2XrdqUzSRZrJsIdIiNXgFdFjkrPAAJv2DEbmLNhS2POGZ0i559gAQADAgADeQADNAQ')

    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.callback_query(lambda callback: 'six' in callback.data)
async def raspis_six(callback: types.CallbackQuery):
    class_respons = [
        ('sixa', 'AgACAgIAAxkBAAIGa2Xrgh--CN5psiKfU6Vuvak1QLNHAAKK2DEbmLNhS-gosIXlDXZgAQADAgADeQADNAQ'),
        ('sixb', 'AgACAgIAAxkBAAIGbWXrgjr97Aq6n8Uwa4KC_C0Lp3hPAAKM2DEbmLNhS_HgXMoETsuTAQADAgADeQADNAQ'),
        ('sixv', 'AgACAgIAAxkBAAIGb2Xrgk2pLlxDwnCzE4NGuBri37b2AAKN2DEbmLNhSy-y0-olo_hTAQADAgADeQADNAQ'),
        ('sixg', 'AgACAgIAAxkBAAIGcWXrgmb-F14b7Ty3no_7S8OaMIK7AAKO2DEbmLNhSwE2TooOB7-MAQADAgADeQADNAQ'),
        ('sixk', 'AgACAgIAAxkBAAIGc2XrgoCqx7DbecLJdVrq0DHraer_AAKP2DEbmLNhS2oburr7UF9nAQADAgADeQADNAQ'),
        ('sixp', 'AgACAgIAAxkBAAIGdWXrgpjlxmUMoaVxlOcJ7W8w_lVbAAKQ2DEbmLNhSweFURVqtt4SAQADAgADeQADNAQ'),
        ('sixc', 'AgACAgIAAxkBAAIGd2XrgsceBVZoKmb7pofJK_kqbSx9AAKR2DEbmLNhS7F2lFyoz3M1AQADAgADeQADNAQ')

    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.callback_query(lambda callback: 'seven' in callback.data)
async def raspis_seven(callback: types.CallbackQuery):
    class_respons = [
        ('sevena', 'AgACAgIAAxkBAAIGjWXsDLUOwoZ-_ZPpJZ4ggYpuU9I2AAIK2jEbmLNhS1dZYmBKHIaJAQADAgADeQADNAQ'),
        ('sevenb', 'AgACAgIAAxkBAAIGj2XsDMYQTR17pklVlZ2CJaVaNPPNAAIL2jEbmLNhS7n-zxTjvj1QAQADAgADeQADNAQ'),
        ('sevenv', 'AgACAgIAAxkBAAIGkWXsDNEOHFNE_8yiGP6lfpvCNrjPAAIM2jEbmLNhS0WTulDl-i1GAQADAgADeQADNAQ'),
        ('sevenr', 'AgACAgIAAxkBAAIGk2XsDOgFuJj6txjrIMwKLk-8UIytAAIN2jEbmLNhS1W64Gu1U4bnAQADAgADeAADNAQ'),
        ('sevenh', 'AgACAgIAAxkBAAIGlWXsDOqDd9KAMBb3SUM3utT-kNeHAAIO2jEbmLNhS_qNhXqJCbeKAQADAgADeQADNAQ'),
        ('sevenf', 'AgACAgIAAxkBAAIGl2XsDO2QLYqYPQvA38s4Ss8AAWxyPgACD9oxG5izYUtBcq57pM1eEwEAAwIAA3kAAzQE')
    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.callback_query(lambda callback: 'eight' in callback.data)
async def raspis_eight(callback: types.CallbackQuery):
    class_respons = [
        ('eighta', 'AgACAgIAAxkBAAIGqWXsDw_6DdB4vxGUmGVRUaU8q8lkAAIY2jEbmLNhS8C4aWiuZFoMAQADAgADeQADNAQ'),
        ('eightb', 'AgACAgIAAxkBAAIGq2XsDxIPUrXR0TPqI1HededGwjiTAAIZ2jEbmLNhS4BQ1p0y2rX9AQADAgADeQADNAQ'),
        ('eightv', 'AgACAgIAAxkBAAIGrWXsDyEzjYuqtRb69I3t4I7KZo7xAAIc2jEbmLNhS5w6aPWIufhAAQADAgADeQADNAQ'),
        ('eightg', 'AgACAgIAAxkBAAIGr2XsDyT1SwPmkUMYhUbb1xZGDA1XAAId2jEbmLNhS8ti4A0u6sQkAQADAgADeQADNAQ'),
        ('eightr', 'AgACAgIAAxkBAAIGsWXsDyYod7ihnP9fe7ReKSTjzMVRAAIe2jEbmLNhSzGWFMDXHK_EAQADAgADeQADNAQ'),
        ('eightf', 'AgACAgIAAxkBAAIGs2XsDynVb-D4Mn552ZyJ5Djo12l2AAIg2jEbmLNhS9HWhptnyL4ZAQADAgADeQADNAQ'),
        ('eightm', 'AgACAgIAAxkBAAIGtWXsDys9PQTkCAHekMebrvqQqwirAAIh2jEbmLNhS_6oQrFVJvQlAQADAgADeQADNAQ')
    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break

@dp.callback_query(lambda callback: 'nine' in callback.data)
async def raspis_eight(callback: types.CallbackQuery):
    class_respons = [
        ('ninea', 'AgACAgIAAxkBAAIGw2XsERYzHFzOQSC1Ni7zkuKWOrsAA2rlMRuYs2lLjyJMp-38erIBAAMCAAN5AAM0BA'),
        ('nineb', 'AgACAgIAAxkBAAIGxWXsESqcH0Fn9VcuuhAxiCJCyRW5AAJs5TEbmLNpS8J4bTYUBxgeAQADAgADeQADNAQ'),
        ('ninev', 'AgACAgIAAxkBAAIGx2XsES2XnX2LzbNXhpmoV5uONuTqAAJt5TEbmLNpS6HRtQfcQ2I2AQADAgADeQADNAQ'),
        ('nineg', 'AgACAgIAAxkBAAIGyWXsETBJjxooJD51--0vpLq4Sw_mAAJu5TEbmLNpSysyBc2Y36zmAQADAgADeQADNAQ'),
        ('nineй', 'AgACAgIAAxkBAAIGy2XsETJaoFLv3zfFUAVSQ8tr6AKiAAJv5TEbmLNpS6G-crPTM35lAQADAgADeAADNAQ')
    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.callback_query(lambda callback: 'ten' in callback.data)
async def raspis_eight(callback: types.CallbackQuery):
    class_respons = [
        ('tena', 'AgACAgIAAxkBAAIG22XsEt76mxMcoHLanO8XfruFniSRAAJ45TEbmLNpSxjWpPb-0kkGAQADAgADeQADNAQ'),
        ('tenb', 'AgACAgIAAxkBAAIG3WXsEuFU4lx0siM7HoZ7ZPtVX4yfAAJ55TEbmLNpS16Nz247dsykAQADAgADeQADNAQ'),
        ('tenv', 'AgACAgIAAxkBAAIG32XsEuM-0Tqit5jlDX1Jp3sPfVT0AAJ65TEbmLNpS6A9X89N-PWUAQADAgADeQADNAQ'),
        ('teng', 'AgACAgIAAxkBAAIG4WXsEuZoubw4SjTwHqkLARgt3OCaAAJ75TEbmLNpS4MlGfYQv5SYAQADAgADeQADNAQ'),
          ('tend', 'AgACAgIAAxkBAAIG42XsEunHT888BAAB6cLPlpVyHPAfTwACfOUxG5izaUuyHwzhSryTdgEAAwIAA3kAAzQE'),
        ('tene', 'AgACAgIAAxkBAAIG5WXsEusFU-qfF-dlpBfy0DvDRdHIAAJ95TEbmLNpSx3vYF9pyyJ9AQADAgADeQADNAQ'),
        ('tenzh', 'AgACAgIAAxkBAAIG52XsEu0gzzVPk2o4kf2wVRhKDdtdAAJ-5TEbmLNpS5HwLvZTTdw9AQADAgADeQADNAQ'),
        ('teni', 'AgACAgIAAxkBAAIG6WXsEu9BJZRj0cDVzcX4jO6RLkaAAAJ_5TEbmLNpSx7g9Lb8AAG1kAEAAwIAA3kAAzQE')

    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.callback_query(lambda callback: 'eleven' in callback.data)
async def raspis_eight(callback: types.CallbackQuery):
    class_respons = [
        ('elevena', 'AgACAgIAAxkBAAIG9WXsFGhGdajEj9Yxu4_Urqosc4nXAAKI5TEbmLNpSyhyMZYmkD3TAQADAgADeQADNAQ'),
        ('elevenb', 'AgACAgIAAxkBAAIG92XsFGv4VrwAAaxj5kW_tVVGttWZLgACieUxG5izaUuxb09jW1SuXAEAAwIAA3kAAzQE'),
        ('elevenv', 'AgACAgIAAxkBAAIG-WXsFG41Ud127cfY2SdJ4Jhiabp_AAKK5TEbmLNpS6eW1b0T7KZGAQADAgADeQADNAQ'),
        ('eleveng', 'AgACAgIAAxkBAAIG-2XsFHD2byAizb5tNi_TeYL3w06dAAKL5TEbmLNpSy1HJqPLeshOAQADAgADeQADNAQ'),
        ('elevend', 'AgACAgIAAxkBAAIG_WXsFHIVf0SJw93lAeXw5_HqPV9HAAKM5TEbmLNpS0Rdmf34ffXhAQADAgADeQADNAQ')

    ]
    my_class = callback.data.lower()
    for data in class_respons:
        if my_class == data[0]:
            await bot.send_photo(callback.from_user.id, data[1])
            break


@dp.message(F.photo)
async def photo(message: types.Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')

@dp.callback_query(lambda callback: 'FIVE' == callback.data)
async def five_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Пятиклашки',reply_markup=kb.five_raspis_class)

@dp.callback_query(lambda callback: 'SIX' == callback.data)
async def six_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Шестиклассники',reply_markup=kb.six_raspis_class)


@dp.callback_query(lambda callback: 'SEVEN' == callback.data)
async def seven_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Семиклассники',reply_markup=kb.seven_raspis_class)


@dp.callback_query(lambda callback: 'EIGHT' == callback.data)
async def eight_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Восьмиклассники',reply_markup=kb.eight_raspis_class)

@dp.callback_query(lambda callback: 'NINE' == callback.data)
async def nine_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Девятиклассники',reply_markup=kb.nine_raspis_class)


@dp.callback_query(lambda callback: 'TEN' == callback.data)
async def nine_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Десятиклассники',reply_markup=kb.ten_raspis_class)

@dp.callback_query(lambda callback: 'ELEVEN' == callback.data)
async def nine_raspis(callback: types.CallbackQuery):
    await callback.message.answer('Одиннадцатиклассники',reply_markup=kb.eleven_raspis_class)


@dp.callback_query(lambda callback: 'quest' in callback.data)
async def questions(callback: types.CallbackQuery):
    quest_respons=[
        ('quest1',st.quest_1),
        ('quest2','AgACAgIAAxkBAAIHJ2XtgyaQCoNBTbzCm99ZwkywzwrXAAKm0jEbQs5oS0ca_TiZFP2oAQADAgADeAADNAQ'),
        ('quest3',st.quest_3),
        ('quest4', st.quest_4),
        ('questf',st.quest_5),
        ('quests',st.quest_6),
        ('questsev',st.quest_7),
        ('queste',st.quest_8)
    ]

    my_class = callback.data.lower()
    for data in quest_respons:
        if my_class == data[0]:
            if my_class == "quest2":
                await bot.send_photo(callback.from_user.id, data[1])
                break
            else:
                await callback.message.answer(data[1])
                break






@dp.message(F.text.lower() == "расписание")
async def raspis(message: types.Message):
    await message.answer("Расписание классов", reply_markup=kb.raspis_class)


@dp.message(F.text.lower() == "часто задаваемые вопросы")
async def raspis(message: types.Message):
    await message.answer("Интересующие вопросы", reply_markup=kb.questions_sk)


@dp.message(F.text.lower() == "список работников")
async def teacher(message: types.Message):
    await message.reply(text="""Выберите кафедру""", reply_markup=kb.secondkb)


@dp.message(F.text.lower() == "руководство")
async def director(message: types.Message):
    await message.answer("Руководство нашей школы", reply_markup=kb.linkskb)


@dp.message(F.text.lower() == "физ-ра")
async def sport_teacher(message: types.Message):
    await message.answer("Наши учителя физкультуры", reply_markup=kb.sportkb)


@dp.message(F.text.lower() == "история и обществознание")
async def sport_teacher(message: types.Message):
    await message.answer("Наши учителя истории и обществознании", reply_markup=kb.istobskb)


@dp.message(F.text.lower() == 'математика')
async def mat_teacher(message: types.Message):
    await message.answer("Наши учителя математики", reply_markup=kb.mathkb)


@dp.message(F.text.lower() == 'обж')
async def obj_teacher(message: types.Message):
    await message.answer("Наши учителя технологии", reply_markup=kb.objkb)


@dp.message(F.text.lower() == 'информатика')
async def inf_teacher(message: types.Message):
    await message.answer("Наши учителя информатики", reply_markup=kb.infkb)


@dp.message(F.text.lower() == 'география')
async def geo_teacher(message: types.Message):
    await message.answer("Наши учителя географии", reply_markup=kb.geokb)


@dp.message(F.text.lower() == 'русский язык и литература')
async def rus_teacher(message: types.Message):
    await message.answer("Наши учителя русского и литературы", reply_markup=kb.ruskb)


@dp.message(F.text.lower() == 'музыка')
async def myz_teacher(message: types.Message):
    await message.answer("Наши учителя музыки", reply_markup=kb.myzkb)


@dp.message(F.text.lower() == 'биология')
async def bio_teacher(message: types.Message):
    await message.answer("Наши учителя биологии", reply_markup=kb.biokb)


@dp.message(F.text.lower() == 'иностранные языки')
async def eng_teacher(message: types.Message):
    await message.answer("Наши учителя иностранных языков", reply_markup=kb.engkb)


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer(text=help)
    await message.delete()


@dp.message(Command('info'))
async def info_command(message: types.Message):
    await message.answer(text=main)
    await message.delete()


@dp.message()
async def idk(message: types.message):
    await message.answer(f'''{message.from_user.first_name}, я вас не понимаю.
Если вам нужна помощь, пропишите команду /help''')
    await message.delete()


if __name__ == '__main__':
    asyncio.run(start())
