# Whatsapp-Bulk-Messenger

WhatsApp Bulk Messenger automates sending of messages via WhatsApp Web. The tool can be used to send WhatsApp messages in bulk. The program runs through a list of numbers provided in `numbers.txt` and sends a predefined (but templated) message to each number in the list. It supports personalized messages by using name placeholders that get replaced with actual recipient names.

## Features

✅ **Bulk Messaging** - Send messages to multiple contacts automatically
✅ **Message Personalization** - Use `{name}` placeholder to personalize messages
✅ **Contact Names** - Support for format: `number - name` in numbers list
✅ **Auto Retry** - Automatically retries failed messages up to 3 times
✅ **Updated Dependencies** - Compatible with latest Selenium 4.x and Chrome
✅ **Modern WhatsApp Web Support** - Updated selectors for current WhatsApp Web interface

**Note:** The current program is limited to sending only TEXT messages

**Note:** Another version of similar project is available which supports sending media and documents along with text. As per many requests, I have added a [video here](https://youtu.be/NNkAh5sLEok) demonstrating how the app works. Please reach out to me on [email](mailto:bagrianirudh@gmail.com) for more enquiry. Join the [google group here](https://groups.google.com/g/whatsapp-bulker/) and [telegram group here](https://t.me/whatsapp_bulker).

## Requirements

*  Python >= 3.6
*  Chrome browser (ChromeDriver is installed automatically by the program)

## Setup

1. Install Python >= 3.6
2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Prepare Your Message

Edit `message.txt` with your message template. Use `{name}` as placeholder for personalization:

```
Hello {name},

This is my text to you from automated messaging system.

Thank You
```

### 2. Prepare Your Contact List

Edit `numbers.txt` with phone numbers. Format:

**With names (recommended):**
```
6285746674052 - Sultan
6285156505553 - Septyo
628123456789 - John Doe
```

**Without names:**
```
6285746674052
6285156505553
628123456789
```

**Important:**
- Use international format without `+` sign (e.g., `628xxx` for Indonesia)
- Do NOT use `08xxx` format - it will fail
- One contact per line
- If name is not provided, `{name}` will be replaced with "there"

### 3. Run the Program

```bash
python automator.py
```

### 4. Follow the Steps

1. The program will display your message and contact count
2. Chrome browser will open automatically to web.whatsapp.com
3. Scan the QR code to login to WhatsApp Web
4. Once logged in and chats are visible, press `Enter` in terminal
5. Sit back and relax! The program will send messages automatically

### 5. Monitor Progress

The program will show:
- ✅ Green: Successfully sent
- ❌ Red: Failed (with retry attempts)
- 📊 Progress: Current/Total contacts

## Number Format Guide

| ❌ Wrong | ✅ Correct |
|---------|-----------|
| `+628123456789` | `628123456789` |
| `08123456789` | `628123456789` |
| `0812-3456-789` | `628123456789` |

**Format:** `[country_code][number_without_leading_zero]`
- Indonesia: `62` + number without `0`
- Example: `0812-3456-7890` → `628123456790`

## Changelog

### Recent Updates (2025)

**🐛 Bug Fixes:**
- Fixed ChromeDriver compatibility issue with latest Chrome versions
- Updated Selenium from 3.x to 4.x for better stability
- Fixed WhatsApp Web send button selector (was failing to click)
- Updated dependencies to support modern Python versions

**✨ New Features:**
- **Personalized Messages**: Use `{name}` placeholder in messages
- **Contact Names**: Support `number - name` format in numbers.txt
- **Better Error Handling**: Improved retry mechanism with clearer error messages
- **Progress Tracking**: Shows contact name and number during sending

**📝 Example:**
```
numbers.txt:
628123456789 - John

message.txt:
Hello {name}, welcome!

Result:
"Hello John, welcome!"
```

## Troubleshooting

**Problem: "There is no such driver by url" error**
- Solution: Update dependencies with `pip install --upgrade -r requirements.txt`

**Problem: Messages not sending (staying in chat box)**
- Solution: Already fixed in latest version. Update your code.

**Problem: "Invalid phone number" error**
- Solution: Use format `628xxx` (country code + number without leading 0)

**Problem: Chrome doesn't open**
- Solution: Make sure Chrome browser is installed on your system

### Funding

If you like this app, I'd appreciate it if you could make a donation via [Buy Me a Coffee](https://www.buymeacoffee.com/anirudhbagri) or [PayPal.Me](https://paypal.me/AnirudhBagri?locale.x=en_GB).
