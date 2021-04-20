import sys
import os
import urllib.request
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
import random
from bs4 import BeautifulSoup

def get_impfen_thueringen_content() -> str:
	'''This function gets checks the vaccination site where it says for which groups  registration 
	is open right now and returns the content as a string. <script> parts are deleted as they change
	whenever the page is loaded.'''
	# Get HTML content of url
	url = 'https://www.impfen-thueringen.de/terminvergabe.html'
	req = urllib.request.urlopen(url)
	html_string = req.read()
	# Get text
	soup = BeautifulSoup(html_string, features = 'lxml')
	site_text = str(soup.get_text())
	site_text = str(site_text.encode('utf8'))
	site_text = site_text.replace('\\n', '')
	return site_text


def popupmsg(message: str) -> None:
	'''This function creates a popup window that shows a given message'''
	popup = tk.Tk()
	popup.wm_title("!")
	label = ttk.Label(popup, text=message)
	label.pack(side="top", fill="x", pady=10)
	button = ttk.Button(popup, text="OK", command = popup.destroy)
	button.pack()
	popup.mainloop()
	return


def check_impfen_thueringen() -> bool:
	'''This function checks whether or not the html has changed since the last check. If that is the case,
	a notification will pop up and the updated version will be saved for the next check. It returns true
	if the site has changed.'''
	first_time = True
	if 'impfen_thueringen.txt' in os.listdir('.'):
		first_time = False
		with open("impfen_thueringen.txt", 'r') as saved_file:
			reference_html_content = saved_file.read()
		up_to_date_html_content = get_impfen_thueringen_content()
		if str(up_to_date_html_content) != str(reference_html_content):
			popupmsg('The site has changed since the last check!')
		else:
			print('Nothing has changed.')
	with open("impfen_thueringen.txt", 'w+') as saved_file:
		saved_file.write(str(get_impfen_thueringen_content()))
	# Return true if a change has been detected.
	if not first_time:
		if str(up_to_date_html_content) != str(reference_html_content):
			return True


def main():
	'''This script runs for approximately 10 hours (60 checks) and checks every 10 minutes if https://www.impfen-thueringen.de/terminvergabe.html has
	changed since the last check. The html string is saved in the file impfen_thueringen.html (in the same folder as the script.)'''
	for _ in range(60):
		check = check_impfen_thueringen()
		timestamp = datetime.now(tz=None)
		if check:
			print('Last checked at ' + str(timestamp) + '. Result: Something has changed! Go check if you can register.')
		else:
			print('Last checked at ' + str(timestamp) + '. Result: Nothing has changed!')
		time.sleep(random.choice(range(300,900)))
	sys.exit(1)


if __name__ == '__main__':
	main()

