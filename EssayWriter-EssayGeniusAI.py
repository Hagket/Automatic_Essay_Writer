from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
import random

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Option to have the browser stay open after script is finished

# If a "AutoEssays" folder doesn't exist, create one to store the essays
if not(os.path.exists("C:/Users/hvket/Downloads/AutoEssays")):
    os.mkdir(os.path.join("C:/Users/hvket/Downloads/", "AutoEssays"))

with open("Prompts.txt", "r") as prompts: # Open Prompts.txt file
    for l in prompts: # For every line in Prompts.txt
        essay = "" # Creates a string called essay that will store the entire essay
        l = l[:-1] # Trim off the new line character at the end of each prompt line string
        sections = l.split("/") # Splits the line into its sections
        for x in range(1, len(sections)): # Traverse through every section besides section[0] (Title of essay)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # Open chrome browser

            driver.get("https://essaygenius.ai/") # Open Essay Genius website

            id_box = driver.find_element("xpath", "//html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/input") # Find the prompt text box
            id_box.send_keys(sections[x])  # Enter prompt into text box
            driver.find_element("xpath", "//html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/button").click() # Click "Start Writing" button
            sleep(30) # Wait 25s for essay to be written
            driver.find_element("xpath", "//html/body/div[8]/div[3]/div/button").click() # Close warning popup
            sleep(1) # Wait 1s for website to load

            sectionText = driver.find_element("xpath", "//html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div[1]").text # Extract essay text and set it to essay variable
            essay += sectionText + "\n\n\n\n" # Add the section to the full essay

            driver.close() # Close the browser when done

        path = "C:/Users/hvket/Downloads/AutoEssays/"  # Path to place the essays
        file_name = sections[0] + ".txt"  # The essay file name should be the prompt string
        with open(os.path.join(path, file_name), "w") as f:  # Open a new file with specified path and with specified file_name
            f.write(essay)  # Insert essay into the newly created file
