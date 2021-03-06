from PIL import Image
def medianOdd(imageList):
    listlength=len(imageList)
    sortedValues=sorted(imageList)
    middleIndex=((listlength+1)/2)-1
    return sortedValues[middleIndex]

picturesList=[]
folder=("image/")

#add all images to an array img 
img=Image.open("image/1.png")
picturesList.append(img)
img=Image.open("image/2.png")
picturesList.append(img)
img=Image.open("image/3.png")
picturesList.append(img)
img=Image.open("image/4.png")
picturesList.append(img)
img=Image.open("image/5.png")
picturesList.append(img)
img=Image.open("image/6.png")
picturesList.append(img)
img=Image.open("image/7.png")
picturesList.append(img)
img=Image.open("image/8.png")
picturesList.append(img)
img=Image.open("image/9.png")
picturesList.append(img)

#get the size of the images
picW,picH=picturesList[0].size
size=(picW,picH)
#create lists for pixel values
redList=[]
greenList=[]
blueList=[]
#create blank image
newImg=Image.new("RGB",size)

#its loop time
for i in range(0,picW):
    for j in range(0,picH):
        for k in range(0,9):
            
           temp =picturesList[k].getpixel((i,j))
           redList.append(temp[0])
           greenList.append(temp[1])
           blueList.append(temp[2])
           
        newr=medianOdd(redList)
        newg=medianOdd(greenList)
        newb=medianOdd(blueList)
        
        newImg.putpixel((i,j),(newr,newg,newb))
           
        del redList[:]
        del greenList[:]
        del blueList[:]
#make new image and save       
newImg.save('Filtered.png')            