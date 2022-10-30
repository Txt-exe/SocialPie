from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
from progress.bar import ShadyBar
import string
import sys
import os
import time
import spoticry

loacation_used = []

print('Welcome to Spoticry 2.0\n')

print("-h for commands")


def print_commands():
    print("\n -s : Start Spotify module to listen to artist and get plays")
    print("\n -f : Start Spotify module to follow artist of your choice")
    print("\n -p : Print The Combo List")
    print("\n -c : Set combolist")
    print("\n -q : quit program")


# gets combo list and stores
def get_combo():
    list_num = input("How many combo list would you like to store?: ")
    try:
        int(list_num)

    except:
        print("That's not an integer number.")
        main()
    else:
        for x in range(int(list_num)):
            list_input = input(
                "Please enter the full path of the location of your combo list: ")
            loacation_used.append(list_input)

            # If file not found terminate program for safety reasons
            if not (os.path.exists(list_input)):
                print("FILE NOT FOUND ")
                main()
            f = open(list_input, )
    print("\nStored Location")
    print("checking for duplicates and removing them...")
    time.sleep(2)
    print("Done\n")

    f.close()


def main():
    waitforin = " "
    waitforin.strip()

    while waitforin != '-q':
        waitforin = input(">: ")

        if waitforin == '-h':

            print_commands()

        elif waitforin == '-q':
            print("Exiting program...")
            time.sleep(2)

            def clearConsole():
                return os.system(
                    'cls' if os.name in ('nt', 'dos') else 'clear')

            clearConsole()
            sys.exit()

        elif waitforin == '-c':
            get_combo()

        elif waitforin == '-p':

            if (len(set(loacation_used)) == 0):
                print("I cant find any accounts right now...")
            else:

                print(set(loacation_used))

        elif waitforin == '-s':

            if len(set(loacation_used)) == 0:
                print("There hasn't been any accounts added to the program")
            if len(set(loacation_used)) >= 1:

                min_time_to_play = input("what is the minimum (in minutes) would you like to play your song?: "
                                         "(Before switching accounts): ")
                try:
                    int(min_time_to_play)

                except:
                    print("That's not an integer number.")
                    main()
                max_time_to_play = input("what is the maximum (in minutes) would you like to play your song?"
                                         "(Before switching accounts): ")
                try:
                    int(max_time_to_play)

                except:
                    print("That's not an integer number.")
                    main()
                else:
                    min_con = min_time_to_play * 60
                    max_con = max_time_to_play * 60

                    for x in range(len(set(loacation_used))):
                        chrome_options = Options()
                        chrome_options.add_extension(
                            r'C:\Users\Chiave\PycharmProjects\Spoticry\VPNcrx.crx')
                        chrome_options.add_extension(
                            r'C:\Users\Chiave\PycharmProjects\Spoticry\Speed.crx')
                        chrome_options.add_experimental_option(
                            "excludeSwitches", ["enable-logging"])

                        driver = webdriver.Chrome(options=chrome_options)
                        spoticry.Spoticry.load_spot(driver, set(loacation_used),
                                                    "https://open.spotify.com/track/6emaRY97qI4JlEBQK7LUjU?si=86669d2d41c14e7f", min_con, max_con)
        else:
            print("Value not recognized...")
            print_commands()


main()
