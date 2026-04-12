<div align="center">

<img src="https://img.shields.io/badge/Telegram-Userbot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Status-Active-00FF00?style=for-the-badge" alt="Status"/>

# 🚀 TELEGRAM SPAMMER USERBOT

<p align="center">
  <i>✨ Your personal assistant for advanced Telegram group management ✨</i>
</p>

<br>

</div>

## 📋 Table of Contents

- [🎯 Features](#-features)
- [⚙️ Installation](#️-installation)
- [🔧 Configuration](#-configuration)
- [📖 Available Commands](#-available-commands)
  - [👥 Group Management](#-group-management)
  - [💬 Message Management](#-message-management)
  - [📨 Spam System](#-spam-system)
  - [🔍 Utilities](#-utilities)
  - [🤖 RAT Commands](#-rat-commands-remote-admin-tools)
- [🚨 Disclaimer](#-disclaimer)
- [📜 License](#-license)

<br>

---

## 🎯 Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🔄 | **Auto Join** - Automatically join multiple groups simultaneously |
| 📝 | **Message Manager** - Save and reuse complex messages with formatting |
| 🚀 | **Mass Spam** - Send messages to all your groups with a custom delay |
| 🔍 | **Group Verification** - Verify your presence in lists of groups |
| ⚡ | **Flood Protection** - Automatic handling of Telegram cooldowns |
| 🤖 | **Remote Control** - Remote control via RAT commands |
| 🎨 | **Rich Formatting** - Full support for HTML and Telegram entities |

</div>

<br>

---

## ⚙️ Installation

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
Telegram Account
```

### 📦 Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/telegram-spammer-bot.git
cd telegram-spammer-bot

# 2. Install dependencies
pip install telethon

# 3. Configure credentials (see Configuration section)

# 4. Start the bot
python bot.py
```

<br>

---

## 🔧 Configuration

### 🔑 Getting API credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to **"API Development Tools"**
4. Create a new application
5. Copy your `api_id` and `api_hash`

### 📝 File Configuration

Open `bot.py` and enter your credentials:

```python
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
```

> ⚠️ **IMPORTANT**: Never share your API credentials!

<br>

---

## 📖 Available Commands

### 👥 Group Management

<table>
<tr>
<td width="30%"><b>Command</b></td>
<td width="70%"><b>Description</b></td>
</tr>

<tr>
<td><code>.chats</code></td>
<td>View the total number of groups you are currently in</td>
</tr>

<tr>
<td><code>.join [links]</code></td>
<td>Join one or more groups. Supports full links or usernames<br>
<i>Example:</i> <code>.join @group1 https://t.me/group2</code></td>
</tr>

<tr>
<td><code>.verify [links]</code></td>
<td>Verify your presence in a list of groups<br>
<i>Example:</i> <code>.verify @group1 @group2 @group3</code></td>
</tr>

</table>

### 💬 Message Management

<table>
<tr>
<td width="30%"><b>Command</b></td>
<td width="70%"><b>Description</b></td>
</tr>

<tr>
<td><code>.setmessage</code></td>
<td>Start saving mode. The next message you send will be saved</td>
</tr>

<tr>
<td><code>.getmessage</code></td>
<td>View the currently saved message</td>
</tr>

</table>

> 💡 **Tip**: The saved message keeps all HTML formatting, links, and entities!

### 📨 Spam System

<table>
<tr>
<td width="30%"><b>Command</b></td>
<td width="70%"><b>Description</b></td>
</tr>

<tr>
<td><code>.delay [minutes]</code></td>
<td>Set the delay between each spam cycle (in minutes)<br>
<i>Example:</i> <code>.delay 30</code></td>
</tr>

<tr>
<td><code>.getdelay</code></td>
<td>View the currently set delay</td>
</tr>

<tr>
<td><code>.startspam</code></td>
<td>Start automatic spam to all groups</td>
</tr>

<tr>
<td><code>.stopspam</code></td>
<td>Stop automatic spam</td>
</tr>

<tr>
<td><code>.status</code></td>
<td>Check if spam is active or not</td>
</tr>

</table>

### 🔍 Utilities

<table>
<tr>
<td width="30%"><b>Command</b></td>
<td width="70%"><b>Description</b></td>
</tr>

<tr>
<td><code>.help</code></td>
<td>Show the link to the full documentation</td>
</tr>

<tr>
<td><code>.rat</code></td>
<td>Show remote control commands</td>
</tr>

</table>

### 🤖 RAT Commands (Remote Admin Tools)

> ⚠️ These commands can be executed by other users to control the bot

<table>
<tr>
<td width="30%"><b>Command</b></td>
<td width="70%"><b>Description</b></td>
</tr>

<tr>
<td><code>.nb</code></td>
<td>Returns the number of groups</td>
</tr>

<tr>
<td><code>.qg [number]</code></td>
<td>Leaves a random number of groups<br>
<i>Example:</i> <code>.qg 5</code></td>
</tr>

<tr>
<td><code>.msstart</code></td>
<td>Starts silent spam (fixed 2-minute delay)</td>
</tr>

<tr>
<td><code>.msstop</code></td>
<td>Stops silent spam</td>
</tr>

<tr>
<td><code>.ss</code></td>
<td>Stops any active spam</td>
</tr>

<tr>
<td><code>.dl</code></td>
<td>Deletes the current chat history</td>
</tr>

</table>

<br>

---

## 🎮 Usage Example

```bash
# 1. Set a message
.setmessage
# Send your promotional message

# 2. Verify it has been saved
.getmessage

# 3. Set the delay
.delay 60  # Every 60 minutes

# 4. Start spam
.startspam

# 5. Check status
.status

# 6. When you're finished, stop it
.stopspam
```

<br>

---

## 🚨 Disclaimer

<div align="center">

### ⚠️ IMPORTANT - READ CAREFULLY ⚠️

</div>

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  This software is provided exclusively for educational        ║
║  and research purposes. Misuse of this tool may               ║
║  violate Telegram's Terms of Service and local laws.          ║
║                                                               ║
║  ❌ DO NOT use for:                                           ║
║    • Unauthorized spam                                        ║
║    • Harassment or nuisance                                   ║
║    • Privacy violation                                        ║
║    • Any illegal activity                                     ║
║                                                               ║
║  ✅ The author is NOT responsible for:                        ║
║    • Misuse of the software                                   ║
║    • Account bans or suspensions                              ║
║    • Legal consequences resulting from use                    ║
║                                                               ║
║  By using this software you agree to be solely                ║
║  responsible for your actions.                                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

<br>

---

## 🛡️ Security

- 🔒 **Never share** your API credentials
- 🚫 **Do not commit** session files (`.session`)
- ⚡ Respect Telegram's **rate limits**
- 🔐 Use the bot **responsibly**

<br>

---

## 📜 License

This project is released under the MIT license. See the `LICENSE` file for more details.

<div align="center">

---

### 💫 Made with ❤️ using Python and Telethon

<br>

[![Telegram](https://img.shields.io/badge/Telegram-Contact-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<br>

```
⭐ If you found this project useful, please leave a star! ⭐
```

---

<sub>Last update: 2025</sub>

</div>
