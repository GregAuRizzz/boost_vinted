from selenium import webdriver
import time

link = input("Entrez le lien de la page web : ")

driver = webdriver.Chrome()

driver.get(link)
print("[*] Page ouverte :", link)

while True:
    driver.refresh()
    print("[*] Page actualisée")
    time.sleep(3) 

driver.quit()
