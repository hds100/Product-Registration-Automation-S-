import pyautogui
from time import sleep

with open('produtos.txt','r') as file:
    for line in file:
        product = line.split(',')[0]
        quantity = line.split(',')[1]
        price = line.split(',')[2]

        pyautogui.click(121,259, duration=0.1)
        pyautogui.write(product)

        pyautogui.click(118,284, duration=0.1)
        pyautogui.write(quantity)

        pyautogui.click(119,312, duration=0.1)
        pyautogui.write(price)

        pyautogui.click(47,468, duration=0.1)
