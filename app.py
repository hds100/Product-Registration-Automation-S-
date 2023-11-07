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
     # Time(duration): set to 100 milliseconds = 0.1 seconds interval between actions to be performed
     # Writing: the pyautogui.write(variable) function will write what it read from each comma-separated variable in the produtos.txt file
        pyautogui.click(121,259, duration=0.1)
        pyautogui.write(product)

        pyautogui.click(118,284, duration=0.1)
        pyautogui.write(quantity)

        pyautogui.click(119,312, duration=0.1)
        pyautogui.write(price)
     # This last function is to define the coordinates of the registration button and click on this button
        pyautogui.click(47,468, duration=0.1)
