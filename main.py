import telebot
from telebot import types
import time

TOKEN = "8436874177:AAGLs7LJ1tW-IIggjKJfTyLfvvu2jqEhUGw"
bot = telebot.TeleBot(TOKEN)

# === Стартовые сообщения ===
def send_intro(chat_id):
    bot.send_message(chat_id, "👋 Здравствуйте!\nЯ бот, который поможет вам вступить в клан ALGN или LGN 🤔💪. Также дам советы для игры Harekat 2 Online 🥳")
    time.sleep(1)
    bot.send_message(chat_id, "🛠 Мы разыскиваем специалистов для создания видео!\nНужно выкладывать материалы в разделе «Монтаж» минимум раз в неделю.")
    time.sleep(1)
    bot.send_message(chat_id, """✨ Что мы предлагаем в качестве компенсации?

- 🎖 Баллы для повышения в звании
- 🤝 Доверие

Чтобы получить баллы, необходимо достичь 20-го ранга.

Если есть вопросы — пишите 👉 @Dania3003.""")
    time.sleep(1)
    bot.send_message(chat_id, """👾 Присоединяйтесь к игровому чату!

Если вы ищете компанию для игр или просто хотите пообщаться — этот чат создан для вас! ⬇️
https://t.me/LGN_Legion_1

🎮 Удачи и веселых игр! ✨""")
    time.sleep(1)


# === Главное меню ===
def main_menu(chat_id):
    # Кнопки ранга
    rank_keyboard = types.InlineKeyboardMarkup()
    rank_keyboard.add(
        types.InlineKeyboardButton("🥉 1-4 ранг", callback_data="rank1"),
        types.InlineKeyboardButton("🥈 5-19 ранг", callback_data="rank2"),
        types.InlineKeyboardButton("🥇 20+ ранг", callback_data="rank3")
    )
    bot.send_message(chat_id, "🔎 Какой у вас ранг в игре Harekat 2 Online?", reply_markup=rank_keyboard)

    # Главное меню
    menu_keyboard = types.InlineKeyboardMarkup()
    menu_keyboard.add(
        types.InlineKeyboardButton("🚁 Техника", callback_data="tech"),
        types.InlineKeyboardButton("ℹ️ Информация", callback_data="info"),
        types.InlineKeyboardButton("💡 Советы", callback_data="tips")
    )
    bot.send_message(chat_id, "📌 Главное меню: выберите категорию", reply_markup=menu_keyboard)


# === Подменю Техника (5 кнопок) ===
def tech_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = {
        "🚁 Какой транспортный вертолёт лучше взять?": "tech_heli",
        "🛡 Какой танк лучше всего брать?": "tech_tank",
        "🚙 Какой БТР лучше всего взять?": "tech_btr",
        "💥 Стоит ли покупать артиллерию?": "tech_artillery",
        "🚓 Какой БМП лучше взять?": "tech_bmp"
    }
    for text, callback in buttons.items():
        markup.add(types.InlineKeyboardButton(text, callback_data=callback))
    bot.send_message(chat_id, "⚙️ Меню: Техника", reply_markup=markup)


# === Подменю Информация (3 кнопки) ===
def info_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = {
        "🎯 ПВЕ и ПВП Harekat 2:Online": "info_pvepvp",
        "🌐 Какой VPN можно использовать для стабильной игры в Harekat 2?": "info_vpn",
        "⚔️ Чем отличается ALGN и LGN?": "info_diff"
    }
    for text, callback in buttons.items():
        markup.add(types.InlineKeyboardButton(text, callback_data=callback))
    bot.send_message(chat_id, "📖 Меню: Информация", reply_markup=markup)


# === Подменю Советы (4 кнопки) ===
def tips_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    buttons = {
        "💰 Как зароботать деньги?": "tips_money",
        "🗺 Какая лучшая карта для фарма?": "tips_map",
        "🚗 Какой самый лучший транспорт для новичка?": "tips_transport",
        "🔫 Какую пушку лучше всего взять для ПВЕ и ПВП?": "tips_gun"
    }
    for text, callback in buttons.items():
        markup.add(types.InlineKeyboardButton(text, callback_data=callback))
    bot.send_message(chat_id, "💡 Меню: Советы", reply_markup=markup)


# === Команда /start ===
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    send_intro(chat_id)
    main_menu(chat_id)


# === Обработка кнопок ===
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    chat_id = call.message.chat.id
    data = call.data

    # Ранги
    if data == "rank1":
        bot.send_message(chat_id, "😅 Вам нужно поднять ранг хотя бы до 5, чтобы поступить в ALGN.")
    elif data == "rank2":
        bot.send_message(chat_id, "🙌 Отлично! Вы можете вступить в клан ALGN.\nНапишите 👉 @Dania3003 и отправьте свой ник, ранг, статистику.")
    elif data == "rank3":
        bot.send_message(chat_id, "🔥 Класс! Вы можете вступить в клан LGN.\nНапишите 👉 @Dania3003 и отправьте свой ник, ранг, статистику.")

    # Главное меню
    elif data == "tech":
        tech_menu(chat_id)
    elif data == "info":
        info_menu(chat_id)
    elif data == "tips":
        tips_menu(chat_id)

    # Подменю Техника
    elif data.startswith("tech_"):
        answers = {
            "tech_heli": "🚁 Лучший транспортный вертолёт — это LH-6 Bird.\nПреимущества:\n- Компактные размеры (можно приземлиться где угодно)\n- Отличная маневренность\n- Возможность использовать личное оружие во время полёта 😀",
            "tech_tank": "🛡 В танках ключевых отличий нет, они разные только визуально.\nРекомендую взять Т-84 — он низкий и дешёвый.",
            "tech_btr": "🚙 Лучший выбор — БТР-80. Только он способен эффективно бороться с вражеской техникой.",
            "tech_artillery": "💥 Артиллерия наносит огромный урон и имеет большой радиус поражения. Но у неё:\n- Ограниченный боекомплект\n- Низкая точность\nПоэтому в бою бывает мало полезна. Игрок на артиллерии почти ничем не поможет команде 🤙",
            "tech_bmp": "🚓 Выбирайте БМП-2 или Брэдли — они одинаковы. Это дело вкуса.\nНи в коем случае не берите W113!"
        }
        bot.send_message(chat_id, answers.get(data, "❔ Нет ответа."))

    # Подменю Информация
    elif data.startswith("info_"):
        answers = {
            "info_pvepvp": "🎯 В Harekat 2 есть 2 режима: ПВЕ и ПВП.\n\nЧтобы выбрать режим: нажмите Играть → Параметры быстрой игры → выберите режим и карту.\n\n🧩 В ПВЕ (на версии 5.1.4) доступны 3 карты: Доновск, Басиан и Маруша 🧐.\n\n⚔️ В ПВП игроки сражаются за 3 точки. Побеждает команда, которая первой обнулит тикеты противника. Тикеты тратятся за:\n- возрождение после смерти (–1 тикет),\n- вызов техники,\n- проигрыш по точкам. 💪",
            "info_vpn": "🌐 Для стабильной игры используйте VPN с минимальной задержкой (например, ProtonVPN или Windscribe).",
            "info_diff": "⚔️ ALGN — клан для игроков от 5 ранга.\n🔥 LGN — элитный клан для игроков от 20 ранга."
        }
        bot.send_message(chat_id, answers.get(data, "❔ Нет ответа."))

    # Подменю Советы
    elif data.startswith("tips_"):
        answers = {
            "tips_money": "💰 Зарабатывать деньги лучше всего через ПВЕ и фарм на картах с большим количеством техники.",
            "tips_map": "🗺 Лучшая карта для фарма — Доновск. Там легко набивать деньги и опыт.",
            "tips_transport": "🚗 Для новичков лучший транспорт — БТР-80 или LH-6 Bird (вертолёт).",
            "tips_gun": "🔫 Для ПВЕ хорош ПКМ, а для ПВП — АК-74М."
        }
        bot.send_message(chat_id, answers.get(data, "❔ Нет ответа."))


print("✅ Бот запущен...")
bot.polling()
