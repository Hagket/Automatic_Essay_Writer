from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import selenium.webdriver as webdriver
import os

#user_agent = ""
edge_driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_experimental_option("detach", True)

browser = webdriver.Edge(service=edge_service, options=edge_options)
browser.get('https://google.com')