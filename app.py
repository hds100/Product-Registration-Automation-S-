import pyautogui # Importing pyautogui
from time import sleep # Importing the sleep method from the time library

# Opening the Produtos.txt text file and granting read-only permission to the registry variables
with open('produtos.txt','r') as file: 
    # Defining variables and reading order
    for line in file:
        product = line.split(',')[0]
        quantity = line.split(',')[1]
        price = line.split(',')[2]
        
    # Defining variable settings: click, time and writing
    # Click: cursor position coordinates through mouseinfo()
    # Time: set to 100 milliseconds = 0.1 seconds interval between actions to be performed
        pyautogui.click(121,259, duration=0.1)
        pyautogui.write(product)

        pyautogui.click(118,284, duration=0.1)
        pyautogui.write(quantity)

        pyautogui.click(119,312, duration=0.1)
        pyautogui.write(price)

        pyautogui.click(47,468, duration=0.1)
