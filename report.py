# -*- coding: utf-8 -*-
"""

Created on Thu Apr 3 18:12:12 2020 
@author: 1742242048hj@gmail.com

"""
import time
from selenium import webdriver
import selenium
from datetime import date
from datetime import datetime

#存储你帐号密码的绝对路径，支持多账号，一行
with open("/home/pi/info.txt",mode="r") as file:
    info=file.readlines()

usernames = []
passwords = []


for everyline in info:
	everyline_new = everyline.replace("\n", "")
	everyline_new = everyline_new.replace(" ", "")
	data = everyline_new.split(",")
	usernames.append(data[0].strip("\n"))
	passwords.append(data[1].strip("\n"))

if (len(usernames) != len(passwords)):
	raise Exception("Hey man, numbers of username and password are not equal")

length = len(usernames)
now = datetime.now()

def log_write(content):
	log = open("report.log", "w")
	log.write(content)
	log.write("\n")
	log.close


for i in range(length):
	username = usernames[i]
	print(username)
	password = passwords[i]
	print(password)

	# selenium part
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')

	driver = webdriver.Chrome('chromedriver', options=options)

	driver.get("http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do")
	time.sleep(10)
	log_write(driver.page_source)

	# web mock clicking
	driver.find_element_by_xpath("//input[@id='username']").send_keys(str(username))  # 填入你的一卡通号
	driver.find_element_by_xpath("//input[@id='password']").send_keys(str(password))  # 填入你的密码
	driver.find_element_by_xpath("//button[@type='submit']").click()
	time.sleep(10)

	log_write(driver.page_source)
	finally_tried = False

	while (not finally_tried):
		try:
			current_result = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]").text

		except selenium.common.exceptions.NoSuchElementException:
			phrase_to_be_recorded = str(username) + 'failed 1 time, trying 2 times at ' + str(now)
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)

		else:
			phrase_to_be_recorded = str(username) + "您上次的填写日期: " + current_result
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)
			finally_tried = True


		try:
			current_result = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]").text

		except selenium.common.exceptions.NoSuchElementException:
			phrase_to_be_recorded = str(username) + 'failed 2 time, trying 3 times at ' + str(now)
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)

		else:
			phrase_to_be_recorded = str(username) + "您上次的填写日期: " + current_result
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)
			finally_tried = True

		try:
			current_result = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]").text

		except selenium.common.exceptions.NoSuchElementException:
			phrase_to_be_recorded = str(username) + 'failed 3 times at ' + str(now) + '学校系统真的不稳定，我重新试试喔'
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)
			finally_tried = False

		else:
			phrase_to_be_recorded = str(username) + "您上次的填写日期: " + current_result
			print(phrase_to_be_recorded)
			log_write(phrase_to_be_recorded)
			finally_tried = True




	try:
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/button[1]").click()
		time.sleep(10)
		driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/button").click()
		time.sleep(10)
		driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]").click()
		print("上报成功！现在是 ", now)
		time.sleep(10)

	except selenium.common.exceptions.NoSuchElementException:
		print(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/button").text)
		today = date.today()
		now = datetime.now()
		print("你特喵的填过啦")

	except Exception:
		print("错误节点1，老bug，请联系admin")

	try:
		current_result = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]").text

	except selenium.common.exceptions.NoSuchElementException:
		phrase_to_be_recorded = 'failed again at' + str(now) + 'Please report bug!'
		print(phrase_to_be_recorded)
		log_write(phrase_to_be_recorded)

	else:
		phrase_to_be_recorded = "您上次的填写日期: " + current_result
		print(phrase_to_be_recorded)
		log_write(phrase_to_be_recorded)


	# exit
	driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/button").click()
