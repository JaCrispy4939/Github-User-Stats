#made by JaCrispy4939
#please dont steal the code
import bs4 as BeautifulSoup
import requests
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import time
import os
import time

username = input("Enter Username: ")


page = requests.get("https://github.com/" + username + "")
soup=BeautifulSoup(page.content,"html.parser")
soup_condition=BeautifulSoup(page.content,"html.parser")

profile_name = soup.find(class_= "p-nickname vcard-username d-block").text
profile_desc = soup.find(class_= "p-note user-profile-bio mb-3 js-user-profile-bio f4").text
profile_repos = soup.find(class_= "Counter").text
profile_followercount = soup.find(class_= "text-bold color-text-primary").text
profile_status = soup.find(class_="user-status-message-wrapper f6 color-text-primary ws-normal lh-condensed")
profile_location = soup.find(class_="p-label")



if profile_location == None:
    profile_location = "User hasnt set a location"
if profile_location == soup.find(class_="p-label"):
    profile_location = soup.find(class_="p-label").text

if profile_status == None:
    profile_status = "User hasnt set up a status"
if profile_status == soup.find(class_="user-status-message-wrapper f6 color-text-primary ws-normal lh-condensed"):
    profile_status = soup.find(class_="user-status-message-wrapper f6 color-text-primary ws-normal lh-condensed").text
if profile_desc == "":
    profile_desc = "User doesnt have a description"
if profile_followercount == "0":
    profile_followercount = "User has no followers"
if profile_repos == "0":
    profile_repos = "User doesnt have any repos"

print("Username: " + profile_name)
print("Profile Description: " + profile_desc)
print("Status: " + str(profile_status))
print("Location: " + profile_location)
print("Repo's: " + profile_repos)
print("Followers: " + str(profile_followercount))
