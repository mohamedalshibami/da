#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
try:
    from telethon.sessions import StringSession
    import asyncio, re, json, shutil
    from kvsqlite.sync import Client as uu
    from telethon.tl.types import KeyboardButtonUrl
    from telethon.tl.types import KeyboardButton, ReplyInlineMarkup
    from telethon import TelegramClient, events, functions, types, Button
    from telethon.tl.types import DocumentAttributeFilename
    import time, datetime, random 
    from datetime import timedelta
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
    from plugins.messages import *
    from plugins.get_code import *
    from plugins.SessionConverter import *
    from telethon.errors.rpcerrorlist import UserDeactivatedBanError
    from telethon.sessions import StringSession
    from telethon.tl.types import InputPeerUser, InputPeerChannel
    from telethon.tl.functions.account import GetAuthorizationsRequest
    from telethon.tl.functions.messages import GetHistoryRequest
except:
    os.system("python3 set_module.py")
    try:
        from telethon.sessions import StringSession
        import asyncio, re, json, shutil
        from kvsqlite.sync import Client as uu
        from telethon.tl.types import KeyboardButtonUrl
        from telethon.tl.types import KeyboardButton
        from telethon import TelegramClient, events, functions, types, Button
        from telethon.tl.types import DocumentAttributeFilename
        import time, datetime, random 
        from datetime import timedelta
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
        from plugins.messages import *
        from plugins.get_code import *
        from plugins.SessionConverter import *
        from telethon.errors.rpcerrorlist import UserDeactivatedBanError
        from telethon.sessions import StringSession
        from telethon.tl.types import InputPeerUser, InputPeerChannel
        from telethon.tl.functions.account import GetAuthorizationsRequest
        from telethon.tl.functions.messages import GetHistoryRequest
    except Exception as errors:
        print('An Erorr with: ' + str(errors))
        exit(0)


def check_vip(user):
    user_id = int(user)
    users = db.get(f"vip_{user_id}")
    noww = time.time()
    if db.exists(f"vip_{user_id}"):
        last_time = users['vip']
        timeee = int(db.get(f"vip_{user_id}_time"))
        WAIT_TIMEE = int(timeee) * 24 * 60 * 60
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None
        
        
if not os.path.isdir('database'):
    os.mkdir('database')

API_ID = "1724716"
API_HASH = "00b2d8f59c12c1b9a4bc63b70b461b2f"
admin = 5639458117
new_password = "jimibot" #التحقق بخطوتين للحسابات التي سيتم بيعها
# Replace with your bot token
token = "7057662293:AAHiWLGZOogFspM-rEym5A29rh9cT4TIGTo"
client = TelegramClient('BotSession', api_id=API_ID, api_hash=API_HASH).start(bot_token=token)
bot = client

#Create DataBase
db = uu('database/KingA.ss', 'bot')

if not db.exists("accounts"):
    db.set("accounts", [])

if not db.exists("countries"):
    db.set("countries", [])

if not db.exists("bad_guys"):
    db.set("bad_guys", [])

if not db.exists("force"):
   db.set("force", [])

if not db.exists("admins"):
   db.set("admins", [admin])

@client.on(events.NewMessage(pattern="/sell_price", func = lambda x: x.is_private))
async def start(event):
    user_id = event.chat_id
    bans = db.get('bad_guys') if db.exists('bad_guys') else []
    async with bot.conversation(event.chat_id) as x:
        countries = db.get("countries")
        text = ""
        for i in countries:
            text += f'{i["name"]} ({i["calling_code"]}): {i["sell_price"]}$'
        await x.send_message(text)
@client.on(events.NewMessage(pattern="/start", func = lambda x: x.is_private))
async def start(event):
    user_id = event.chat_id
    bans = db.get('bad_guys') if db.exists('bad_guys') else []
    async with bot.conversation(event.chat_id) as x:
        try:
            force = db.get("force")
            for channel in force:
                result = await client(functions.channels.GetParticipantRequest(
                    channel=channel,
                    participant=user_id
                ))
        except Exception as a:
            await x.send_message(f"**⚠️︙عذراً عزيزي يجب عليك الاشتراك بقناة البوت**\n🚀︙القناه يتم بها عمليات تحديث البوت \n ✨︙رابط القناه : @{channel} \n\n• اشترك في القناه ثم أرسل : /start")
            return
        keyboard = [
            [
                Button.inline("- اعدادات الارقام 🚀 .", data="ajxjao"),
            ],
            [
                Button.inline("- الاشتراك الاجباري 〽️.", data="ajxkho"), 
                Button.inline("- قسم الادمنيه 👨‍✈️.", data="aksgl"), 
            ],
            [
                Button.inline("- قسم البيع و الشراء 💰 .", data="ajkofgl"),
            ],
            [
                Button.inline("- قسم الرصيد 🤍.", data="ajkcoingl"), 
                Button.inline("- قسم الحظر 🚫.", data="bbvjls"), 
            ],
            [
                Button.inline("- قناة اثباتات التسليم 🖤 .", data="set_trust_channel"),
            ],
            [
                Button.inline("- تعديل رسالة القوانين 🔐 .", data="edit_rules"),
            ],
        ]
        
        buttons = [
            [
                Button.inline("-☎️︙شراء رقم تيليجرام جاهز 🔹️.", data="buy"),
            ],
            [
                Button.inline("- 🤖︙بــوت الــرشــق 👤➕️.", url="https://t.me/QY8Bot"),
            ],
            [
                Button.inline("🛒︙بيع رقم تيليجرام جاهز 🚏.", data="buy"),
            ],
            [
                Button.inline("🪝︙ سحب رصيد💲.", data="ssart"),
                Button.inline("♻️︙ تحويل رصيد💲.", data="transfer"),
            ],
            [
                Button.inline("👩‍✈️︙ التواصل مع الإدارة 🎶.", data="supper"),
                Button.inline("-⚠️︙ شروط الإستخدام 📚.", data="liscgh"),
            ]
        ]
        
    if user_id in bans: return
    if not db.exists(f"user_{user_id}"):
        members = 0
        db.set(f"user_{user_id}", {"coins": 0, "id": user_id})
        if user_id == admin:
            await event.reply(msgs['ADMIN_MESSAGE'], buttons=keyboard)
            await event.reply(msgs['START_MESSAGE'].format(event.chat_id, 0), buttons=buttons)
        else:
            await event.reply(msgs['START_MESSAGE'].format(event.chat_id, 0), buttons=buttons)
        user_info = await client.get_entity(user_id)
        users = db.keys('user_%')
        for _ in users:
            members+=1
        if user_info.username == None: username = "None"
        else: username = "@"+str(user_info.username)
        await bot.send_message(admin, f'• دخل شخص جديد الي البوت الخاص بك 👾\n\n- معلومات المستخدم الجديد .\n\n- اسمه : <a href="tg://user?id={user_id}">{user_info.first_name}</a>\n- معرفه : {username}\n- ايديه : {user_id}\n\n• اجمالي الاعضاء : {members}', parse_mode="html")
    else:
        coins = db.get(f"user_{user_id}")["coins"]
        if user_id == admin or user_id in db.get("admins"):
            await event.reply(msgs['ADMIN_MESSAGE'], buttons=keyboard)
            await event.reply(msgs['START_MESSAGE'].format(event.chat_id, coins), buttons=buttons)
        else:
            await event.reply(msgs['START_MESSAGE'].format(event.chat_id, coins), buttons=buttons)
        
@bot.on(events.CallbackQuery(pattern=b'ajxjao'))
async def numgpv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم الارقام ☎️ .')
    await event.edit('** 🚀︙مرحبا بك عزيزي بقسم الارقام ** \n ✅︙يمكنك التحكم في ارقامك بكل سهوله \n 👤︙الارقام يتم تحديثها تلقائي \n **✳️︙ماذا تنتظر اذهب الان للتحكم في الارقام **',
                    buttons=[
                        [
                            Button.inline("- عدد ارقام البوت 🚀.", data="all_of_number")
                        ],
                        [
                            Button.inline("- اضافة دوله 🌎.", data="add_country"),
                            Button.inline("- حذف دوله ❌.", data="del_country")
                        ],
                        [
                            Button.inline("- اضافة رقم ✅.", data="add"),
                            Button.inline("- حذف رقم ⛔.", data="del_account")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])

                             
@bot.on(events.CallbackQuery(pattern=b'ajxkho'))
async def nuupv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم االاشتراك الاجباري 〽️️ .')
    await event.edit('** 〽️︙اختر ماذا تريده من قسم الاشتراك الاجباري **',
                    buttons=[
                        [
                            Button.inline("- اضافة قناه 🌟.", data="add_force"),
                            Button.inline("- حذف قناه ⛔.", data="del_force")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])
@bot.on(events.CallbackQuery(pattern=b'aksgl'))
async def nuupv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم الادمنيه 👨‍✈️️ .')
    await event.edit('** 👨‍✈️️︙اختر ماذا تريده من قسم الادمنيه **',
                    buttons=[
                        [
                            Button.inline("- اضافة ادمن 🤍.", data="add_admin"),
                            Button.inline("- حذف ادمن ✖️.", data="del_admin")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])
@bot.on(events.CallbackQuery(pattern=b'ajkofgl'))
async def nuupv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم الشراء و البيع♻️ .')
    await event.edit('**♻️︙اختر ماذا تريده من قسم البيع و الشراء **',
                    buttons=[
                        [
                            Button.inline("- تغيير سعر شراء 🚀.", data="change_price"),
                            Button.inline("- تغيير سعر بيع ✅.", data="del_coins")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])              
@bot.on(events.CallbackQuery(pattern=b'ajkcoingl'))
async def nuupv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم النقاط .')
    await event.edit('**💰︙اختر ماذا تريده من قسم النقاط **',
                    buttons=[
                        [
                            Button.inline("- اضافة رصيد 💰.", data="add_coins"),
                            Button.inline("- خصم رصيد ✨.", data="change_sell_price")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])            

@bot.on(events.CallbackQuery(pattern=b'bbvjls'))
async def nuupv_button(event):
    await event.answer(' - مرحباً بك عزيزي في قسم الحظر .')
    await event.edit('**🚫︙اختر ماذا تريده من قسم الحظر **',
                    buttons=[
                        [
                            Button.inline("- حظر شخص 🚫.", data="ban"),
                            Button.inline("- الغاء حظر ✅.", data="unban")
                        ],
                        [
                            Button.inline("⦉ رجوع ⬅️ ⦊", data="admin_panel")
                        ]
                    ])       

@bot.on(events.CallbackQuery(pattern=b'reply_'))
async def reply_button(event):
    data = event.data.decode('utf-8')
    user_id = int(data.split('_')[-1])
    
    async with bot.conversation(admin) as conv:
        await conv.send_message("الرجاء إرسال الرسالة التي تريد إرسالها للعضو.")
        response = await conv.get_response()
        
        await bot.send_message(
            user_id,
            f"رسالة من الدعم: {response.text}"
        )
        await conv.send_message("تم إرسال الرسالة للعضو بنجاح.")

    


@bot.on(events.CallbackQuery(pattern=b'ssart'))
async def withdraw_balance(event):
    user_id = event.chat_id
    user_data = db.get(f"user_{user_id}")
    if user_data["coins"] < 1:
        await event.answer(" - الحد الأدنى للسحب هو 1$.")
        return
    
    async with bot.conversation(user_id) as conv:
        await conv.send_message("- أرسل رقم الكاش الخاص بك أو محفظتك.")
        cash_info = await conv.get_response()
        
        await conv.send_message("- أدخل الكمية التي تريد سحبها.")
        amount_info = await conv.get_response()
        
        try:
            amount = float(amount_info.text)
            if amount > user_data["coins"]:
                await conv.send_message("- لا يمكنك سحب أكثر مما لديك من الرصيد.")
                return
            user_data["coins"] -= amount
            db.set(f"user_{user_id}", user_data)
            
            # إرسال رسالة للمالك مع معلومات العضو الذي قام بالسحب
            withdraw_message = await bot.send_message(
                admin, 
                f"• تم سحب الرصيد بنجاح من عضو:\n\n- ايديه: {user_id}\n- يوزره: @{event.sender.username}\n- الرسالة: {cash_info.text}\n- مبلغ الرصيد المسحوب: {amount}",
                buttons=[
                    [Button.inline("✅︙تاكيد عملية التحويل .", data=f"confirm_withdraw_{user_id}")]
                ]
            )
            
            await conv.send_message(f"- تم سحب {amount} من رصيدك بنجاح.")
        except ValueError:
            await conv.send_message("- يجب إدخال رقم صحيح لكمية الرصيد.")

@bot.on(events.CallbackQuery(pattern=b'confirm_withdraw_'))
async def confirm_withdraw(event):
    data = event.data.decode('utf-8')
    user_id = int(data.split('_')[-1])
    
    # إرسال رسالة للعضو
    await bot.send_message(user_id, "- تم تحويل الرصيد بنجاح.")
    
    # إرسال رسالة للمالك
    await event.edit("تم إرسال الرسالة للعضو بنجاح.")

@bot.on(events.CallbackQuery(pattern=b'supper'))
async def support_button(event):
    user_id = event.chat_id
    async with bot.conversation(user_id) as conv:
        await conv.send_message("ارسل رسالتك و سيتم الرد عليك من قبل الدعم بعد فتره من الزمن.", buttons=[Button.inline("رجوع", data="main")])
        response = await conv.get_response()
        
        user_info = await client.get_entity(user_id)
        username = f"@{user_info.username}" if user_info.username else "None"
        
        await bot.send_message(
            admin,
            f"رسالة جديدة من الدعم:\n\n"
            f"- اسم المستخدم: <a href='tg://user?id={user_id}'>{user_info.first_name}</a>\n"
            f"- معرف المستخدم: {username}\n"
            f"- ايدي المستخدم: {user_id}\n\n"
            f"الرسالة: {response.text}",
            parse_mode="html",
            buttons=[Button.inline("الرد على العضو", data=f"reply_{user_id}")]
        )
        await conv.send_message("تم إرسال رسالتك إلى الدعم، سيتم الرد عليك في أقرب وقت ممكن.")

@bot.on(events.CallbackQuery(pattern=b'reply_'))
async def reply_button(event):
    data = event.data.decode('utf-8')
    user_id = int(data.split('_')[-1])
    
    async with bot.conversation(admin) as conv:
        await conv.send_message("الرجاء إرسال الرسالة التي تريد إرسالها للعضو.")
        response = await conv.get_response()
        
        await bot.send_message(
            user_id,
            f"رسالة من الدعم: {response.text}"
        )
        await conv.send_message("تم إرسال الرسالة للعضو بنجاح.")
        
@bot.on(events.CallbackQuery(pattern=b'liscgh'))
async def rules_button(event):
    if db.exists("rules_message"):
        rules_message = db.get("rules_message")
    else:
        rules_message = "مرحباً عزيزي، يجب عليك الالتزام بالقوانين التالية:\n\n1. لا تنشر محتوى غير لائق.\n2. لا تستخدم البوت لأغراض غير قانونية.\n3. يجب عليك التحلي بالصبر والاحترام في التعامل مع الآخرين.\n4. في حالة وجود مشكلة، تواصل مع الدعم الفني."
    
    await event.edit(rules_message, buttons=[Button.inline("رجوع", data="main")])

@bot.on(events.CallbackQuery(pattern=b'edit_rules'))
async def edit_rules_button(event):
    async with bot.conversation(admin) as conv:
        await conv.send_message("الرجاء إرسال رسالة القوانين الجديدة.")
        response = await conv.get_response()
        
        db.set("rules_message", response.text)
        await conv.send_message("تم تحديث رسالة القوانين بنجاح.")

                                                                                           
@client.on(events.callbackquery.CallbackQuery())
async def start_lis(event):
    data = event.data.decode('utf-8')
    user_id = event.chat_id
    bans = db.get('bad_guys') if db.exists('bad_guys') else []
    global new_password
    if data == "change_sell_price":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['sell_price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"chs_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"chs_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="admin_panel")])
        await event.edit("- اختر الدولة التي تريد تغيير سعرها\n- سعر البيع هو السعر بجانب اسم الدولة", parse_mode='markdown', buttons=buttons)
        return 
    
    if data.startswith("chs_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان سعر البيع الجديد الذي تريد تعيينه لدولة {name}")
            ch = await x.get_response()
            try:
                price = float(ch.text)
            except:
                await x.send_message(f"- برجاء ارسل العدد ارقام او ارقام عشرية ")
                return
            countries = db.get("countries")
            for i in countries:
                if calling_code == i['calling_code']:
                    i['sell_price'] = price
                    db.set("countries", countries)
                    await x.send_message(f"- تم تغيير سعر دولة {name} الي {price}")
                    return
            await x.send_message(f"- حدث خطأ اثناء تغيير سعر الخدمة ❌")
            
    if data == "change_price":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"chg_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"chg_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="admin_panel")])
        await event.edit("- اختر الدولة التي تريد تغيير سعرها", parse_mode='markdown', buttons=buttons)
        return 
    
    if data.startswith("chg_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان السعر الجديد الذي تريد تعيينه لدولة {name}")
            ch = await x.get_response()
            try:
                price = float(ch.text)
            except:
                await x.send_message(f"- برجاء ارسل العدد ارقام او ارقام عشرية ")
                return
            countries = db.get("countries")
            for i in countries:
                if calling_code == i['calling_code']:
                    i['price'] = price
                    db.set("countries", countries)
                    await x.send_message(f"- تم تغيير سعر دولة {name} الي {price}")
                    return
            await x.send_message(f"- حدث خطأ اثناء تغيير سعر الخدمة ❌")
            
    if data == "add_force":
        async with bot.conversation(event.chat_id) as x:
            force = db.get("force")
            await x.send_message(f"- ارسل الان معرف او رابط قناة الاشتراك الاجباري.")
            ch = await x.get_response()
            channel = ch.text.replace('https://t.me/', '').replace('@', '').replace(" ", "")
            if channel in force:
                await x.send_message(f"- هذه القناة ضمن قنوات الاشتراك الاجباري بالفعل!.")
                return
            force.append(channel)
            db.set("force", force)
            await x.send_message(f"- تم حفظ قناة الاشتراك الاجباري بنجاح.")
            return
            
    if data == "del_force":
        async with bot.conversation(event.chat_id) as x:
            force = db.get("force")
            await x.send_message(f"- ارسل الان معرف او رابط قناة الاشتراك الاجباري لحذفها.")
            ch = await x.get_response()
            channel = ch.text.replace('https://t.me/', '').replace('@', '').replace(" ", "")
            if channel not in force:
                await x.send_message(f"- هذه القناة ليست ضمن قنوات الاشتراك الاجباري.")
                return
            force.remove(channel)
            db.set("force", force)
            await x.send_message(f"- تم حذف قناة الاشتراك الاجباري بنجاح.")
            return
    async with bot.conversation(event.chat_id) as x:
        try:
            force = db.get("force")
            for channel in force:
                result = await client(functions.channels.GetParticipantRequest(
                    channel=channel,
                    participant=user_id
                ))
        except Exception as a:
            await event.edit(f"- عليك الاشتراك بقناة البوت اولاً لتتمكن من استخدامه.\n\n@{channel}\n- إشترك ثم أرسل /start")
            return
    if user_id in bans:
        return
    
    if data == "sell":
        await event.edit(f"`- برجاء الانتظار ...`")
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"• ارسل الان رقم الهاتف الذي تريد بيعه مع رمز الدولة \n• مثال: \n+20466133155")
            ch = await x.get_response()
            phone_number = ch.text.replace("+", "").replace(" ", "")
            if "+" not in ch.text:
                message = "- ارسل رقم الهاتف بشكل صحيح مع +"
                await x.send_message(message)
            else:
                countries = db.get("countries")
                for code in countries:
                    if ch.text.startswith(code['calling_code']):
                        calling_code = code['calling_code']
                        name = code["name"]
                        sell_price = code["sell_price"]
                        message = f"**- معلومات مهمة قبل اتمام عملية البيع ⚠️**\n\n- الحساب : {ch.text}\n- الدولة : {name}\n- سعر البيع : {sell_price}$\n\n**- هل تريد متابعة عملية البيع ؟**"
                        buttons = [
                            [
                                Button.inline("الغاء ❌", data="back"),
                                Button.inline("متابعة ✅", data=f"next_sell:+{phone_number}"),
                            ],
                        ]
                        await event.reply(message, buttons=buttons)
                        return 
                message = "- عذراً، لا يمكنك بيع ارقام لهذه الدولة لانها غير متاحة في البوت"
                await x.send_message(message)
                
    if data.startswith("next_sell:"):
        await event.edit(f"`- برجاء الانتظار ...`")
        async with bot.conversation(event.chat_id) as x:
            phone_number = data.split(':')[1]
            countries = db.get("countries")
            for code in countries:
                if phone_number.startswith(code['calling_code']):
                    calling_code = code['calling_code']
                    name = code["name"]
                    sell_price = code["sell_price"]
                    app = TelegramClient(StringSession(), api_id=API_ID, api_hash=API_HASH)
                    await app.connect()
                    password=None
                    try:
                        code = await app.send_code_request(phone_number)
                    except (ApiIdInvalidError):
                        await x.send_message("ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ.")
                        return
                    except (PhoneNumberInvalidError):
                        await x.send_message("ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.")
                        return
                    await x.send_message("- تم ارسال كود التحقق الخاص بك علي حسابك علي تليجرام.\n\n- ارسل الكود بالتنسيق التالي : 1 2 3 4 5")
                    txt = await x.get_response()
                    code = txt.text.replace(" ", "")
                    try:
                        await app.sign_in(phone_number, code, password=None)
                        string_session = app.session.save()
                        print(string_session)
                        data = {"phone_number": phone_number, "two-step": "لا يوجد", "session": string_session}
                        accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
                        accounts.append(data)
                        db.set(f"accounts_{calling_code}", accounts)
                        buttons = [
                            [
                                Button.inline("تحقق ✅", data=f"check:{phone_number}:{calling_code}"),
                            ]
                        ]
                        try:
                            session = MangSession.TELETHON_TO_PYROGRAM(string_session)
                            await enable_password(session, new_password)
                        except Exception as a:
                            print(a)
                            pass
                        await event.reply(f"**• تم التحقق من صحة الكود ✅**\n\n- الان الخطوة التالية هي تسجيل الخروج من جميع جلسات الحساب ماعدا جلسة البوت الاساسية، ثم اضغط زر تحقق\n\n**- بعد اكتمال التحقق ستحصل على مبلغ قدره {sell_price}$** 〽️", buttons=buttons)
                        
                    except (PhoneCodeInvalidError):
                        await x.send_message("ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**")
                        return
                    except (PhoneCodeExpiredError):
                        await x.send_message("ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**")
                        return
                    except (SessionPasswordNeededError):
                        await x.send_message("- ارسل رمز التحقق بخطوتين الخاص بحسابك")
                        txt = await x.get_response()
                        password = txt.text
                        try:
                            await app.sign_in(password=password)
                        except (PasswordHashInvalidError):
                            await x.send_message("ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.")
                            return
                        string_session = app.session.save()
                        data = {"phone_number": phone_number, "two-step": password, "session": string_session}
                        accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
                        accounts.append(data)
                        db.set(f"accounts_{calling_code}", accounts)
                        try:
                            session = MangSession.TELETHON_TO_PYROGRAM(string_session)
                            await change_password(session, password, new_password)
                        except:
                            pass
                        buttons = [
                            [
                                Button.inline("تحقق ✅", data=f"check:{phone_number}:{calling_code}"),
                            ]
                        ]
                        await event.reply(f"**• تم التحقق من صحة الكود ✅**\n\n- الان الخطوة التالية هي تسجيل الخروج من جميع جلسات الحساب ماعدا جلسة البوت الاساسية، ثم اضغط زر تحقق\n\n**- بعد اكتمال التحقق ستحصل على مبلغ قدره {sell_price}$** 〽️", buttons=buttons)
                        
    if data.startswith("check:"):
        await event.edit(f"`- برجاء الانتظار ...`")
        async with bot.conversation(event.chat_id) as x:
            phone_number = data.split(':')[1]
            calling_code = data.split(':')[2]
            countries = db.get("countries")
            for code in countries:
                if phone_number.startswith(code['calling_code']):
                    calling_code = code['calling_code']
                    name = code["name"]
                    sell_price = code["sell_price"]
                    accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
                    for i in accounts:
                        if phone_number == i["phone_number"]:
                            ses = i["session"]
                            xx = await count_ses(ses)
                            mkk = isinstance(xx, list)
                            if mkk is False:
                                await x.send_message(f"• حدث خطا ما رجاء اعادة تسجيل الرقم مرة اخرى\n\n{x}")
                                return
                            xv = len(xx)
                            if xv == 1:
                                message = f"**• تم اجتياز عملية التحقق بنجاح ✅**\n\n- الحساب : {phone_number}\n- الدولة : {name}\n\n**• تم اضافة مبلغ {sell_price}$ الي رصيد حسابك.**"
                                user = db.get(f"user_{user_id}")
                                user["coins"] += float(sell_price)
                                db.set(f"user_{user_id}", user)
                                await x.send_message(message)
                                message = f"**- قام المستخدم {user_id}**👤\n\n- باضافة حساب الي البوت.\n- الرقم : {phone_number}\n- السعر : {sell_price}\n- الدولة : {name}"
                                await client.send_message(admin, message)
                            else:
                                bm = ""
                                for i in xx:
                                    bm += f"• {i}\n"
                                xxx = f"""**• فشل في اكمال عملية التحقق ❌**
            
- مازالت هناك بعض الجلسات يجب تسجيل الخروج منها.

{bm}

**- تذكر قم بحذف جميع الجلسات ماعدا جلسة البوت ثم اضغط تحقق** ⚠️"""
                                buttons = [
                                    [
                                        Button.inline("تحقق ✅", data=f"check:{phone_number}:{calling_code}"),
                                    ]
                                ]
                                await x.send_message(xxx, buttons=buttons)
    if data == "set_trust_channel":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل معرف او رابط قناة اثباتات التسليم.")
            ch = await x.get_response()
            channel = ch.text.replace('https://t.me/', '').replace('@', '').replace(" ", "")
            try:
                message = "- تم تفعيل قناة اثباتات التسليم بنجاح ✅"
                await client.send_message(channel, message)
            except:
                message = "- حدث خطأ ❌، تأكد من رفع البوت ادمن في قناتك مع صلاحية ارسال الرسائل"
                await x.send_message(message)
                return
            message = "- تم تفعيل قناة اثباتات التسليم بنجاح ✅"
            await x.send_message(message)
            db.set("trust_channel", channel)
        
    if data == "transfer":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(msgs['TRANSFER_MESSAGE'])
            iii = await x.get_response()
            try:
                id = int(iii.text)
            except:
                return await x.send_message("- ارسل ايدي المستخدم بشكل صحيح!.")
            if user_id == id:
                return await x.send_message("- لا يمكنك تحويل الرصيد لنفسك!.")
            if not db.exists(f"user_{id}"):
                return await x.send_message("- هذا المستخدم غير موجود ضمن بياناتنا!.")
            less = db.get("transfer_minimum") if db.exists("transfer_minimum") else 5
            await x.send_message(f"**• حسنا قم بإرسال الرصيد الذي تود تحويله ♻**\n\n- أدنى حد للتحويل {less} $")
            cou = await x.get_response()
            try:
                count = float(cou.text)
            except:
                return await x.send_message("- ارسل الرصيد بشكل صحيح في صورة ارقام او ارقام عشرية!.")
            info = db.get(f"user_{user_id}")
            count += 0.02 * float(cou.text)
            if info['coins'] < count:
                return await x.send_message("- رصيد غير كافٍ لتحويل هذا القدر من الرصيد!.")
            if less > count:
                return await x.send_message(f"- الحد الادني لتحويل الرصيد هو {less} $!.")
            info['coins'] -= count 
            db.set(f"user_{user_id}", info)
            acc = db.get(f"user_{id}")
            acc['coins'] += float(cou.text)
            db.set(f"user_{id}", acc)
            await client.send_message(id, f"**- تم استلام مبلغ من الرصيد 📥**\n\n- قدره : {float(cou.text)} $\n- من : `{user_id}`")
            await x.send_message(f"**- تم ارسال مبلغ من الرصيد 📤**\n\n- قدره : {float(cou.text)} $\n- الي : `{id}`")
            await client.send_message(admin, f"**• تمت عملية تحويل رصيد ♻️**\n\n- من : `{user_id}`\n- إلي : `{id}`\n- المبلغ : {cou.text}$\n\n**• عمولة التحويل : {0.02 * float(cou.text)}$**")
    if data == "add_coins":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان ايدي الشخص الذي تريد اضافة رصيد له.")
            id = await x.get_response()
            if not db.exists(f"user_{id.text}"):
                await x.send_message(f"- هذا المستخدم لم ينضم الي البوت بعد.")
                return
            info = db.get(f"user_{id.text}")
            await x.send_message(f"- المستخدم : {id.text}\n- رصيده : {info['coins']} $\n\n- ارسل الان عدد الرصيد الذي تريد اضافته المستخدم")
            count = await x.get_response()
            try:
                info['coins'] += float(count.text)
            except:
                await x.send_message(f"- ارسل عدد الرصيد ارقام او ارقام عشرية فقط.")
                return
            db.set(f"user_{id.text}", info)
            await x.send_message(f"- تم اضافة الرصيد بنجاح.✅\n\n- رصيده الان : {info['coins']} $")
            message = f"- تم اضافة {count.text}$ الي رصيدك. ✅\n\n- رصيدك الحالي : {info['coins']} $"
            await client.send_message(int(id.text), message)
            return 
    if data == "del_coins":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان ايدي الشخص الذي تريد خصم رصيد منه.")
            id = await x.get_response()
            if not db.exists(f"user_{id.text}"):
                await x.send_message(f"- هذا المستخدم لم ينضم الي البوت بعد.")
                return
            info = db.get(f"user_{id.text}")
            await x.send_message(f"- المستخدم : {id.text}\n- رصيده : {info['coins']} $\n\n- ارسل الان عدد الرصيد الذي تريد خصمه من المستخدم")
            count = await x.get_response()
            try:
                info['coins'] -= float(count.text)
            except:
                await x.send_message(f"- ارسل عدد الرصيد ارقام او ارقام عشرية فقط.")
                return
            db.set(f"user_{id.text}", info)
            await x.send_message(f"- تم خصم الرصيد بنجاح.\n- رصيده الان : {info['coins']} $")
            return
        
    if data == "ban":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان ايدي الشخص الذي تريد حظره من استخدام البوت.")
            id = await x.get_response()
            try:
                i = int(id.text)
            except:
                await x.send_message(f"- ارسل ايدي المستخدم بشكل صحيح.")
                return
            bans = db.get('bad_guys') if db.exists('bad_guys') else []
            if id.text in bans:
                await x.send_message(f"- هذا المستخدم محظور من البوت بالفعل!.")
                return
            bans.append(id.text)
            db.set("bad_guys", bans)
            await x.send_message(f"- تم حظر المستخدم من إستخدام البوت.")
            return 
    
    if data == "unban":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان ايدي الشخص الذي تريد رفع حظره من استخدام البوت.")
            id = await x.get_response()
            try:
                i = int(id.text)
            except:
                await x.send_message(f"- ارسل ايدي المستخدم بشكل صحيح.")
                return
            bans = db.get('bad_guys') if db.exists('bad_guys') else []
            if id.text not in bans:
                await x.send_message(f"- هذا المستخدم غير محظور من البوت بالفعل!.")
                return
            bans.remove(id.text)
            db.set("bad_guys", bans)
            await x.send_message(f"- تم رفع حظر المستخدم من إستخدام البوت.")
            return 
    
    if data == "all_of_number":
        countries = db.get("countries")
        count = 0
        keys = db.keys("accounts_%")
        for i in keys:
            count += len(db.get(i[0]))
                          
        return await event.answer(f"- إجمالي ارقام البوت المسجلة : {count}.", alert=True)
        
    if data == "main":
        coins = db.get(f"user_{user_id}")["coins"]
        buttons = [
            [
                Button.inline("-☎️︙شراء رقم تيليجرام جاهز 🔹️.", data="buy"),
            ],
            [
                Button.inline("- 🤖︙بــوت الــرشــق 👤➕️.", url="https://t.me/QY8Bot"),
            ],
            [
                Button.inline("🛒︙بيع رقم تيليجرام جاهز 🚏.", data="buy"),
            ],
            [
                Button.inline("🪝︙ سحب رصيد💲.", data="ssart"),
                Button.inline("♻️︙ تحويل رصيد💲.", data="transfer"),
            ],
            [
                Button.inline("👩‍✈️︙ التواصل مع الإدارة 🎶.", data="supper"),
                Button.inline("-⚠️︙ شروط الإستخدام 📚.", data="liscgh"),
            ]
        ]
        await event.edit(msgs['START_MESSAGE'].format(event.chat_id, coins), parse_mode='markdown', buttons=buttons)
        return
        
    if data == "admin_panel":
        keyboard = [
            [
                Button.inline("- اعدادات الارقام 🚀 .", data="ajxjao"),
            ],
            [
                Button.inline("- الاشتراك الاجباري 〽️.", data="ajxkho"), 
                Button.inline("- قسم الادمنيه 👨‍✈️.", data="aksgl"), 
            ],
            [
                Button.inline("- قسم البيع و الشراء 💰 .", data="ajkofgl"),
            ],
            [
                Button.inline("- قسم الرصيد 🤍.", data="ajkcoingl"), 
                Button.inline("- قسم الحظر 🚫.", data="bbvjls"), 
            ],
            [
                Button.inline("- قناة اثباتات التسليم 🖤 .", data="set_trust_channel"),
            ],
        ]
        await event.edit(msgs['ADMIN_MESSAGE'], buttons=keyboard)
        return 
        
    if data == "buy" or data == "back":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"countries_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"countries_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="main")])
        await event.edit(msgs['COUNTRY_LIST'], parse_mode='markdown', buttons=buttons)
        return
        
    if data == "del_account":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"show_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"show_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="admin_panel")])
        await event.edit("- اختر الدولة التي تريد حذف رقم منها", parse_mode='markdown', buttons=buttons)
        return
    
    if data.startswith("show_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        if accounts == []:
           return await event.answer("- لا توجد أي حسابات في هذه الدولة.", alert=True)
        text = ""
        buttons = [[Button.inline(f"{count}: +{i['phone_number']}", data=f"v:{i['phone_number']}:{calling_code}:{name}:{price}")] for count, i in enumerate(accounts, 1)]
        buttons.append([Button.inline("رجوع ↩️", data=f"del_account")])
        await event.edit(f"- اليك قائمة الحسابات المسجلة لدولة : {name}", parse_mode='markdown', buttons=buttons)
        return
        
    if data.startswith("v:"):
        phone_number = data.split(':')[1]
        calling_code = data.split(':')[2]
        name = data.split(':')[3]
        price = data.split(':')[4]
        info = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        for i in info:
            if i['phone_number'] == phone_number:
                text = f"- الحساب : `+{i['phone_number']}`\n- كلمة السر : `{i['two-step']}`\n\n**• اختر من الازرار ما تود فعله بهذه الحساب**"
        keyboard = [
            [
                Button.inline("الحصول علي الكود", data=f"get:{phone_number}:{calling_code}:{name}:{price}"),
            ],
            [
            Button.inline(f"+{phone_number} | Delete ❌", data=f"del:{phone_number}:{calling_code}:{name}"), 
            ],
            [
            Button.inline("رجوع ↩️", data=f"show_{calling_code}_{name}_{price}")
            ]
        ]
        await event.edit(text, parse_mode='markdown', buttons=keyboard)
        return
        
    if data.startswith("del:"):
        phone_number = data.split(':')[1]
        calling_code = data.split(':')[2]
        name = data.split(':')[3]
        text = f"- الرقم : `+{phone_number}`\n\n**- هل انت متاكد من حذف الرقم ؟**"
        keyboard = [
            [
            Button.inline("رجوع ↩️", data=f"v:{phone_number}:{calling_code}:{name}"),
            Button.inline("حذف ❌", data=f"del_done:{phone_number}:{calling_code}:{name}")
            ]
        ]
        await event.edit(text, parse_mode='markdown', buttons=keyboard)
        return
        
    if data.startswith("del_done:"):
        phone_number = data.split(':')[1]
        calling_code = data.split(':')[2]
        name = data.split(':')[3]
        keyboard = [
            [
            Button.inline("رجوع ↩️", data="admin_panel")
            ]
        ]
        
        info = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        for i in info:
            if i['phone_number'] == phone_number:
                info.remove(i)
                db.set(f"accounts_{calling_code}", info)
                await event.edit(f"- تم حذف الرقم `+{phone_number}` من قائمة الارقام المسجلة في دولة {name}✅", parse_mode='markdown', buttons=keyboard)
                return
        await event.edit(f"- فشل حذف الرقم `+{phone_number}` من قائمة الارقام المسجلة في دولة {name} ❌", parse_mode='markdown', buttons=keyboard)
        return 
        
    if data == "add":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"rig_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"rig_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="main")])
        await event.edit("- اختر الدولة التي تريد اضافة الرقم بها", parse_mode='markdown', buttons=buttons)
        return 
        
    if data.startswith("rig_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        async with bot.conversation(event.chat_id) as x:
            await x.send_message(f"- ارسل الان رقم حساب التليجرام مع رمز النداء لاضافته الي قائمة حسابات دولة {name}")
            txt = await x.get_response()
            phone_number = txt.text.replace("+", "").replace(" ", "")
            app = TelegramClient(StringSession(), api_id=API_ID, api_hash=API_HASH)
            await app.connect()
            password=None
            try:
                code = await app.send_code_request(phone_number)
            except (ApiIdInvalidError):
                await x.send_message("ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ.")
                return
            except (PhoneNumberInvalidError):
                await x.send_message("ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.")
                return
            await x.send_message("- تم ارسال كود التحقق الخاص بك علي حسابك علي تليجرام.\n\n- ارسل الكود بالتنسيق التالي : 1 2 3 4 5")
            txt = await x.get_response()
            code = txt.text.replace(" ", "")
            try:
                await app.sign_in(phone_number, code, password=None)
                string_session = app.session.save()
                data = {"phone_number": phone_number, "two-step": "AmmarKing", "session": string_session}
                accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
                accounts.append(data)
                db.set(f"accounts_{calling_code}", accounts)
                await x.send_message(f"- تم اضافة الحساب الي قائمة الحسابات لدولة {name}\n- عدد ارقام هذه الدولة : {len(accounts)}\n\n- الرقم جاهز الان للبيع ✅")
            except (PhoneCodeInvalidError):
                await x.send_message("ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**")
                return
            except (PhoneCodeExpiredError):
                await x.send_message("ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**")
                return
            except (SessionPasswordNeededError):
                await x.send_message("- ارسل رمز التحقق بخطوتين الخاص بحسابك")
                txt = await x.get_response()
                password = txt.text
                try:
                    await app.sign_in(password=password)
                except (PasswordHashInvalidError):
                    await x.send_message("ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.")
                    return
                string_session = app.session.save()
                data = {"phone_number": phone_number, "two-step": password, "session": string_session}
                accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
                accounts.append(data)
                db.set(f"accounts_{calling_code}", accounts)
                await x.send_message(f"- تم اضافة الحساب الي قائمة الحسابات لدولة {name}\n- عدد ارقام هذه الدولة : {len(accounts)}\n\n- الرقم جاهز الان للبيع ✅")
        return 
        
    if data == 'zip_all':
        folder_path = f"./database"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                await client.send_file(user_id, zip_file, attributes=[DocumentAttributeFilename(file_name="database.zip")])
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
    if data.startswith("get:"):
        phone_number = data.split(':')[1]
        calling_code = data.split(':')[2]
        name = data.split(':')[3]
        price = data.split(':')[4]
        info = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        keyboard = [
            [
            Button.inline("رجوع ↩️", data="main")
            ]
        ]
        for i in info:
            if i['phone_number'] == phone_number:
                code = await get_code(i['session'])
                try:
                    cd = int(code)
                    text = f"الحساب : `+{i['phone_number']}`\nتحقق بخطوتين : `{i['two-step']}`\n✅ الكود : `{code}`\n\nتم ايجاد الكود، سيتم ايقاف الاتصال بالحساب"
                    now = datetime.datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    bots = await client.get_me()
                    user_info = await client.get_entity(bots.id)
                    keyboards = [
                        [
                            KeyboardButtonUrl("شراء حساب تليجرام", url=f"https://t.me/{user_info.username}"),
                        ]
                    ]
                    if db.exists("trust_channel"):
                        await client.send_message(
                            db.get("trust_channel"),
                            msgs['TRUST_MESSAGE'].format(
                                name,
                                f"{phone_number}"[:8],
                                price,
                                f"{user_id}"[:8],
                                code,
                                current_time
                            ),
                            buttons=keyboards,
                            parse_mode="markdown"
                        )
                    info.remove(i)
                    db.set(f"accounts_{calling_code}", info)
                except Exception as a:
                    print(a)
                    text = f"الحساب : `+{i['phone_number']}`\nتحقق بخطوتين : `{i['two-step']}`\n❌ الكود : `{code}`\n\nلم يتم ايجاد الكود."
                async with bot.conversation(event.chat_id) as x:
                    await x.send_message(text, buttons=keyboard)
        return 
    if data == "add_country":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- ارسل الان الدولة مع العلم الخاص بها مثال:\n- مصر 🇪🇬")
            name = await x.get_response()
            await x.send_message(f"- ارسل الان رمز النداء الخاص بدولة {name.text} متبوع بـ + مثال\n: +20")
            calling_code = await x.get_response()
            await x.send_message(f"- ارسل الان سعر الرقم لهذه الدولة بعملة الـ $")
            price = await x.get_response()
            try:
                am = float(price.text)
            except:
                await x.send_message(f"- رجاء ارسل رقم فقط، اعد تسجيل الدولة")
                return 
            await x.send_message(f"- ارسل الان سعر بيع الارقام لدولة {name.text}")
            sell_price = await x.get_response()
            countries = db.get("countries")
            countries.append({"name": name.text, "calling_code": calling_code.text, "price": price.text, "sell_price": sell_price.text})
            db.set("countries", countries)
            await x.send_message(f"- تم حفظ الدولة بنجاح ✅\n- عدد الدول المضافة : {len(countries)}")
            return 
    
    if data == "del_country":
        countries = db.get("countries")
        buttons = []
        row = []
        for code in countries:
            calling_code = code['calling_code']
            name = code['name']
            price = code['price']
            if len(row) < 2:
                row.append(Button.inline(text=f"{name} : {price} $", data=f"delete_{calling_code}_{name}_{price}"))
            else:
                buttons.append(row)
                row = [Button.inline(text=f"{name} : {price} $", data=f"delete_{calling_code}_{name}_{price}")]
        if row:
            buttons.append(row)
        
        buttons.append([Button.inline(text="رجوع ↩️", data="main")])
        await event.edit("- اختر الدولة التي تريد حذفها", parse_mode='markdown', buttons=buttons)
    
    if data.startswith("delete_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        countries = db.get("countries")
        buttons = [
            [
            Button.inline("رجوع ↩️", data="del_country")
            ]
        ]
        for data in countries:
            if data["calling_code"] == calling_code:
                countries.remove(data)
                await event.edit("- تم حذف الدولة بنجاح ✅", parse_mode='markdown', buttons=buttons)
                db.set("countries", countries)
                return
        await event.edit("- فشل حذف الدولة ❌", parse_mode='markdown', buttons=buttons)
        
    if data.startswith("countries_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        coins = db.get(f"user_{user_id}")['coins']
        if float(coins) < float(price):
            return await event.answer("- رصيدك لا يكفي لشراء اي ارقام من هذه الدولة.", alert=True)
        accounts = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        if accounts == []:
            return await event.answer("- لا توجد أي حسابات في هذه الدولة.", alert=True)
        keyboard = [
            [
                Button.inline("الغاء ❌", data="back"),
                Button.inline("تأكيد ✅", data=f"buy_{calling_code}_{name}_{price}")
            ],
        ]
        await event.edit(msgs['BUY_MESSAGE'].format(name, price), parse_mode='markdown', buttons=keyboard)
        return
        
    if data.startswith("buy_"):
        calling_code = data.split('_')[1]
        name = data.split('_')[2]
        price = data.split('_')[3]
        acc = db.get(f"user_{user_id}")
        acc['coins'] -= float(price)
        db.set(f"user_{user_id}", acc)
        info = db.get(f"accounts_{calling_code}") if db.exists(f"accounts_{calling_code}") else []
        i = random.choice(info)
        text = f"- الحساب : `+{i['phone_number']}`\n- تحقق بخطوتين : `{i['two-step']}`\n\n**• قم بتطلب الحصول علي الكود اولا ثم اضغط علي الزر ادناه**"
        keyboard = [
            [
                Button.inline("الحصول علي الكود", data=f"get:{i['phone_number']}:{calling_code}:{name}:{price}"),
            ]
        ]
        await event.edit(text, buttons=keyboard)
    if data == "add_admin":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- ارسل الان ايدي الادمن الذي تريد رفعه")
            name = await x.get_response()
            try:
                id = int(name.text)
            except:
                return await x.send_message("- ارسل الايدي ارقام فقط")
            admins = db.get("admins")
            if id in admins:
                return await x.send_message("- العضو ادمن بالفعل ❌")
            admins.append(id)
            db.set("admins", admins)
            await x.send_message("- تم اضافة العضو ادمن بنجاح ✅")
            
    if data == "del_admin":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- ارسل الان ايدي الادمن الذي تريد حذفه")
            name = await x.get_response()
            try:
                id = int(name.text)
            except:
                return await x.send_message("- ارسل الايدي ارقام فقط")
            admins = db.get("admins")
            if id not in admins:
                return await x.send_message("- العضو ليس ادمن بالبوت ❌")
            admins.remove(id)
            db.set("admins", admins)
            await x.send_message("- تم ازالة العضو من الادمن بنجاح ✅")

async def count_ses(session):
    api_hash='d00b2a9f2c9b17ee7b25cbac6ef9f1bf'
    api_id=27140514
    try:
        app = TelegramClient(StringSession(session), api_id=API_ID, api_hash=API_HASH)
        await app.connect()
        try:
            resulkt = await app(functele.auth.ResetAuthorizationsRequest())
        except:
            pass
        unauthorized_attempts = await app(GetAuthorizationsRequest())
        listt = []
        for i in unauthorized_attempts.authorizations:
        	mod = listt.append(i.device_model)
        return listt
    except Exception as a:
        print(str(a))
        return str(a)
        
client.run_until_disconnected()
