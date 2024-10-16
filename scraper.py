from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

driver = webdriver.Edge()
driver.get(START_URL)
driver.maximize_window()

planets_data = []



headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Defina o dataframe do pandas


# Converta para CSV
#para adicionar a primeira coluna com os numeros de serie o atributo index com a eitqueta id

