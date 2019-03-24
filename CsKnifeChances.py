from random import *
from time import sleep

tries = 0
blue = 0
purple = 0
pink = 0
red = 0
statTrackBlue = 0
statTrackPurple = 0
statTrackPink = 0
statTrackRed = 0

caseCost = float(input("Cost Of Case: "))

statTrack = 0
while True:
    skinChance = randint(1,10000)
    statTrackChance = randint(1,100)
    sleep(0.00000005)
    if skinChance <= 7879:
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack Blue!")
            tries += 1
            blue += 1
            statTrackBlue += 1
        else:
            print("Blue")
            tries += 1
            blue += 1
    if skinChance <= 9575 and skinChance > 7879:
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack Purple!")
            tries += 1
            purple += 1
            statTrackPurple += 1
        else:
            print("Pink")
            tries += 1
            purple += 1
    if skinChance <= 9857 and skinChance > 9575:
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack Pink!")
            tries += 1
            pink += 1
            statTrackPink += 1
        else:
            print("Pink")
            tries += 1
            pink += 1
    if skinChance <= 9956 and skinChance > 9857:
        print("Red")
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack Red!")
            tries += 1
            red += 1
            statTrackRed += 1
        else:
            print("Red")
            tries += 1
            red += 1
    if skinChance <= 10000 and skinChance > 9956:
        totalCost = str(caseCost * tries + tries * 2.5)
        tries += 1
        if statTrackChance <= 8:
            statTrack += 1
            print("StatTrack Knife!")
        else:
            print("Knife!")
        print(" ")
        print("Blue Skins:", blue, "StatTrack:", statTrackBlue)
        print("Purple Skins:", purple, "StatTrack:", statTrackPurple)
        print("Pink Skins:", pink, "StatTrack:", statTrackPink)
        print("Red Skins:", red, "StatTrack:", statTrackRed)
        print("StatTrack Skins:", statTrack)
        print("Tries:", tries + 1)
        print("Total Cost: $" + totalCost)
        exit = input("Press Enter To Exit: ")
        if exit == '':
            quit()
