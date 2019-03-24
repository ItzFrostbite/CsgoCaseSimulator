from random import *
from time import sleep

tries = 0
blue = 0
purple = 0
pink = 0
red = 0

caseCost = float(input("Cost Of Case: "))

statTrack = 0
while True:
    skinChance = randint(1,10000)
    statTrackChance = randint(1,100)
    sleep(0.00000005)
    if skinChance <= 7879:
        print("Blue")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack!")
        tries += 1
        blue += 1
    if skinChance <= 9575 and skinChance > 7879:
        print("Purple")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack!")
        tries += 1
        purple += 1
    if skinChance <= 9857 and skinChance > 9575:
        print("Pink")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack!")
        tries += 1
        pink += 1
    if skinChance <= 9956 and skinChance > 9857:
        print("Red")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack!")
        tries += 1
        red += 1
    if skinChance <= 10000 and skinChance > 9956:
        totalCost = str(caseCost * tries + tries * 2.5)
        print("Knife")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack!")
        print(" ")
        print("Blue Skins:", blue)
        print("Purple Skins:", purple)
        print("Pink Skins:", pink)
        print("Red Skins:", red)
        print("StatTrack Skins:", statTrack)
        print("Tries:", tries + 1)
        print("Total Cost: $" + totalCost)
        exit = input("Press Enter To Exit: ")
        if exit == '':
            quit()
