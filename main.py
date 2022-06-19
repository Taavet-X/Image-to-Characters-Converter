from time import sleep
from PIL import Image #pip install pillow
from PIL import ImageFont, ImageDraw 
import os

def convertImageToCharacters(urlSrc, urlTrj, booleanSaveAsImage):
    image = Image.open(urlSrc)
    image.filename
    pixels = image.load()
    chars = ['@', '%', '&', '#', '0', 'C', '?', '!', ':', '.', ' '] #Ordered list, the first char is the one with the most of fill
    deepness = len(chars)-1 
    strResult =""
    ##The following validation is in order to create an image as result instead of a txt
    if(booleanSaveAsImage):                                                           ##
        text_font = ImageFont.truetype("C:\Windows\Fonts\lucon.ttf", 12)              ##
        text_width = text_font.getmask(("t "*image.size[0])).getbbox()[2]             ##
        canvas = Image.new('RGB', (text_width + 30, 14 * image.size[1]), 'white')     ##
        image_editable = ImageDraw.Draw(canvas)                                       ##
    ####################################################################################
    for y in range(image.size[1]):
        strRow = ""
        for x in range(image.size[0]):
            r = pixels[x,y][0]
            g = pixels[x,y][1]
            b = pixels[x,y][2]
            k = (r+g+b)/3 #conversion to gray scale range=[0,255]
            factor = deepness/255 # The factor requiered to convert a value from 0 to 255 into one from 0 to the deepness value
            convertedValue = int(round(k * factor, 0)) #This value is in the range of the amount of characters in the list.
            strRow += chars[convertedValue] + " "
        strResult += strRow + "\n"
        ##Paints the text in the canvas, in case that the result is an image ###########
        if(booleanSaveAsImage):                                                       ##
            image_editable.text( (15, y*14), strRow, (0, 0, 0), font=text_font)       ##
        ################################################################################
    imageName = image.filename.split("\\")[1].split(".")[0]
    if booleanSaveAsImage:
        canvas.save(urlTrj+"\\"+imageName+".png")
    else:
        open(urlTrj+"\\"+imageName+".txt", "w").write(strResult)

def readFiles(booleanSaveAsImage):
    directory = os.listdir("input")
    if len(directory) == 0:
        print("No files were found at the input folder")
        return
    for element in directory:
        strUrlScr = "input\\" + element
        try:
            print("Converting "+element)
            convertImageToCharacters(strUrlScr, "output", booleanSaveAsImage)            
        except:
            print("Skipping " + strUrlScr)                
    print("\033[92m---> Files created!\033[0m")

def readUserInput():
    try:
        print("\033[96m--------------------------------")  
        print("Type '1' for TXT or '2' for PNG")
        print("--------------------------------")  
        userInput = input("\033[96mInput: \033[0m")
        if userInput == "1":            
            readFiles(False)
            input("\033[96mPress Enter to finish\033[0m")
        elif userInput == "2":
            readFiles(True)
            input("\033[96mPress Enter to finish\033[0m")
        else:
            print("\033[91mUnknown Option, try again.\033[0m")
            readUserInput()
        
    except:
        print("\033[91mThere was an error.\033[0m")        

readUserInput()