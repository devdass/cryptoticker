#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from poloniex import Poloniex
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def stringMaker(inpair): #returns a tuple --> (text, colour)
    polo=Poloniex()
    ticker = polo.returnTicker()[inpair]
    print "~~~Running stringMaker(string_pair) function~~~"
    last_val = ticker['last']
    disp_last_val = last_val
    prefix = ""

    # For BTC pairs, this makes things more readable
    if inpair[0:3] == "BTC":
        pair1_disp = (inpair[0:3] + "/" +inpair[4:])
        #print inpair,"--> is a BTC Pair"
        if last_val < 0.001:
            disp_last_val = str(last_val/(1e-6))
            prefix = u"\u00B5\u20BF "
            #print "uB" + disp_last_val
        elif last_val < 0.01:
            disp_last_val = str(int(last_val/(1e-6)))
            prefix = u"\u00B5\u20BF "
            #print "uB " + disp_last_val
        elif last_val < 1:
            disp_last_val = str(round(last_val,5))
            prefix = u"\u20BF "
            #print "B" + disp_last_val

    # For USDT pairs, this makes thigs more readable
    if inpair[0:4] == "USDT":
        pair1_disp = (inpair[0:4] + "/" +inpair[5:])
        prefix = "$"
        #print inpair,"--> is a USDT Pair"
        count = 0
        number = last_val
        while (number > 0):
            number = number//10
            count = count + 1

        if last_val < 1:
            disp_last_val = "Less than $1"
            #print disp_last_val
        elif count > 3:
            disp_last_val = str(int(round(last_val)))
            #print "$" + disp_last_val
        elif count >= 1:
            disp_last_val = '%.2f'%last_val
            #print "$" + '%.2f'%last_val

    #print inpair

    #print"Last Value:", last_val
    percent_change = ticker['percentChange']
    percent_change = percent_change*100
    #print "Percent Change:", round(percent_change,2), "%"
    neg = 1 #change this to something orange
    if percent_change < 0:
        colour = "255,0,0"
        neg = (255,0,0) #red
    else:
        colour = "0,255,0"
        neg = (0,255,0) #green

    pc = str(round(percent_change,1))
    coin_display_string = pair1_disp + "  " + prefix + str(disp_last_val) + "  " + pc + "%   "
    print coin_display_string
    return (coin_display_string, neg)

def mergeTwoImages(imageList): #string of images in a list eg: ['LSK.ppm', 'BTC_LSK.ppm']
    images = map(Image.open, imageList)
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    saveName = "logo_" + imageList[1]
    new_im.save(saveName)
    print ("The merged mergedLogoAndTextData pic is called: ", saveName)
    return saveName

def textDataPicMaker(inTuple):
    #inTuple: A tuple containing text and a colour.
    #returns the string of the save name for the .ppm, eg: "BTC_USDT.ppm"
    #sftp://pi@192.168.1.220/home/pi/rpi-rgb-led-matrix/fonts/UphevalBTC.ttf
    #font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 32)
    font = ImageFont.truetype("/home/pi/rpi-rgb-led-matrix/fonts/UphevalBTC2.ttf", 60)
    textData = inTuple[0] #string containing the data
    textColour = inTuple[1] #(r,g,b)

    width, ignore = font.getsize(textData)
    #setting up the canvas
    im = Image.new("RGB", (width, 60), "black") #width + 30
    draw = ImageDraw.Draw(im)

    x = 0
    draw.text((x, -2), textData, textColour, font=font) #Change the number after 'x' to alter the vertical height of the text/.ppm

    #Making the filename appropriate. Eg: "BTC/USDT $2342 -4%" --> "BTC_USDT.ppm"
    slashIndex = textData.find("/")
    textData = list(textData)
    textData[slashIndex] = "_"

    textData = "".join(textData)

    spaceIndex = textData.find(" ") 

    textSaveName = textData[:spaceIndex] + "textDataPicMaker.ppm"
    im.save(textSaveName)
    if textColour == (0,255,0):
        textSaveNameWithArrow = mergeTwoImages(["test-code/arrows/Up.ppm",textSaveName])
    elif textColour == (255,0,0):
        textSaveNameWithArrow = mergeTwoImages(["test-code/arrows/Down.ppm",textSaveName])
    return textSaveNameWithArrow


#pairs = ["BTC_ZEC", "USDT_XMR", "BTC_LSK", "USDT_BTC", "BTC_ETH", "USDT_XRP"]
pairs = ["USDT_BTC"]
mergedLogoAndTextDataLIST = []

for pair in pairs:
    data = stringMaker(pair)
    textDataPic = textDataPicMaker(data) #filename for the textDataPic
    textDataString = data[0]

    pairString = textDataString[:textDataString.find(" ")] #Eg: pairString = "BTC/ETH"

    print ("pairString: " + pairString)

    index = len(pairString) - 3

    if pairString[index:] == "BTC":
        print "BTC detected"
        logoFilename = "test-code/logos/BTC.ppm"
    elif pairString[index:] == "LSK":
        print "LSK detected"
        logoFilename = "test-code/logos/LSK.ppm"
    elif pairString[index:] == "XRP":
        print "XRP detected"
        logoFilename = "test-code/logos/XRP.ppm"
    elif pairString[index:] == "ZEC":
        print "ZEC detected"
        logoFilename = "test-code/logos/ZEC.ppm"
    else:
        print "unknown detected"
        logoFilename = "test-code/logos/unknown.ppm"

    mergedLogoAndTextData = mergeTwoImages([logoFilename, textDataPic])
    mergedLogoAndTextDataLIST.append(mergedLogoAndTextData)

if len(mergedLogoAndTextDataLIST) > 1:
    finalImage = mergeTwoImages(mergedLogoAndTextDataLIST)
else:
    finalImage = mergedLogoAndTextData
print ("The final image is named: " + finalImage)


#"test-code/logos/temp/" +


################################################################################
os.system("sudo ./demo -D 1 -m 2 --led-slowdown-gpio=2 --led-cols=64 --led-chain=4  --led-pixel-mapper='U-mapper' --led-brightness=100 " + finalImage)


#--led-cols=64 --led-slowdown-gpio=2 --led-chain=4  --led-pixel-mapper="U-mapper" --led-brightness=50 --led-show-refresh
