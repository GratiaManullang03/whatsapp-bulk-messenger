from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Anirudh Bagri     ******")
print("*****           www.github.com/anirudhbagri         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

contacts = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		# Support format: nomor atau nomor - nama
		parts = line.strip().split('-', 1)
		number = parts[0].strip()
		name = parts[1].strip() if len(parts) > 1 else "there"
		contacts.append({"number": number, "name": name})
f.close()
total_number=len(contacts)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, contact in enumerate(contacts):
	number = contact["number"]
	name = contact["name"]
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {} ({}).'.format((idx+1), total_number, name, number) + style.RESET)
	try:
		# Replace {name} placeholder dengan nama sebenarnya
		personalized_message = message.replace(quote('{name}'), quote(name))
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + personalized_message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					# Tunggu chat box muncul
					click_btn = WebDriverWait(driver, delay).until(
						EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send' or @data-testid='compose-btn-send']"))
					)
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
driver.close()
