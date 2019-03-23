from random import *
from time import sleep

tries = 0
blue = 0
purple = 0
pink = 0
red = 0

caseCost = float(input("Cost Of Case: "))

def knifeOpened():
    print("Knife Opened")
    print("Tries", tries)
while True:
    skinChance = randint(1,10000)
    sleep(0.00000005)
    if skinChance >= 7879:
        print("Blue")
        tries += 1
        blue += 1
    if skinChance >= 1696 and skinChance < 7879:
        print("Purple")
        tries += 1
        purple += 1
    if skinChance >= 282 and skinChance < 1696:
        print("Pink")
        tries += 1
        pink += 1
    if skinChance >= 99 and skinChance < 282:
        print("Red")
        tries += 1
        red += 1
    if skinChance >= 44 and skinChance < 99:
        totalCost = str(caseCost * tries + tries * 2.5)
        print("KNIFE")
        print(" ")
        print("Blue Skins:", blue)
        print("Purple Skins:", purple)
        print("Pink Skins:", pink)
        print("Red Skins:", red)
        print("Tries:", tries)
        print("Total Cost: $" + totalCost)
        exit = input()
