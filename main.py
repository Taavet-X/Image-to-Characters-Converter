import colorsys
from PIL import Image #pip install pillow

def convertImageToCharacters(url):
    image = Image.open(url)
    pixels = image.load()
    chars = ['@', '%', '&', '#', '0', 'C', '?', '!', ':', '.', ' '] #Ordered list, the first char is the one with the most of fill
    deepness = len(chars)-1 
    strResult =""
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
    return strResult

def readUserInput():
    try:
        print("\033[96m---------------------------------------")        
        print("Info: type 'exit' to stop this proccess.")        
        userInput = input("\033[96mImage Location (Path):\033[0m")
        if userInput != "exit":
            f = open("output.txt", "w") #The file to save the result
            f.write(convertImageToCharacters(userInput)) #I highly recommed to use small images since there is no scaling, (300 x 300 around).
            print("\033[92m---> File created!\033[0m")
    except:
        print("\033[91mThere was an error, try again.\033[0m")
        readUserInput()

readUserInput()