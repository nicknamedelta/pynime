#!/usr/bin/env python3
import os
import json
from datetime import datetime

def theTime(tOp):
    # current date and time
    now = datetime.now()

    if tOp == 1:
        # return mm/dd/YY H:M:S format
        return now.strftime('%m/%d/%Y, %H:%M:%S')
    if tOp == 2:
        # return mm/dd/YY format
        return now.strftime('%m/%d/%Y')

def loadJson():
    try:
        with open("assets/list.json", "r") as file:
            data = json.load(file)
        return data
    except:
        print('Have any error while we are loading the file.')

def saveJson(data):
    try:
        with open("assets/list.json", "w") as file:
            json.dump(data, file, indent = 4)
    except:
        print('Have any error while we are saving new anime.')

def addAnimeJson(sName, sEp, sSea):
    # loads json data in array
    svdAn = loadJson()
    # new object with the anime's information
    sAn = {"name": sName, "episode": int(sEp), "season": int(sSea)}

    if not svdAn:
        # add new anime in the end of array
        svdAn = [sAn]
    else:
        svdAn.append(sAn)

    # save the content in json
    saveJson(svdAn)
    print('You added a new anime to the list.')

def main():
    print('Welcome, today is: {};'.format(theTime(1)))
    print('----------MENU----------')
    
    sOp = -1
    while sOp != 0:
        print('Select an option:\n1 - CREATE\n0 - EXIT')
        sOp = int(input('\nEnter selected option: '))

        if sOp == 1:
            print('\n----------START CREATE ANIMES----------\n')
            name = input('Enter the name: ')
            ep = input('Enter the episode: ')
            sea = input('Enter the season: ')

            addAnimeJson(name, ep, sea)
            print('\n----------END CREATE ANIMES----------\n')
        if ((sOp < 1 and sOp != 0) or sOp > 4):
            print('(^-^)b - "sorry, i can\'t make this."')
        if sOp == 0:
            exit()
        # wait user press 'ENTER' key
        input("Press Enter to continue...")
main()