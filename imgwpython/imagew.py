from PIL import Image
mac = Image.open("C:\\Users\\Tanujg\\OneDrive\\Desktop\\pasport size.jpg")
#print(type(mac))
#mac.show()
#print(mac.size)
#print(mac.filename)
#print(mac.format_description)

# Cropping Images
#mac1 = mac.crop((0,0,100,100))
#mac1.show() # here our cropped images shown

#my = Image.open("C:\\Users\\Tanujg\\OneDrive\\Desktop\\Colour pencil.jpg")
#my.show()
#print(my.size)
#x = 0
#y = 374

#w=474/1
#h=474/7
#my1= my.crop((x,y,w,h))
#my1.show() # here we got only top three pencil in the output

# Now for bottom
#w = 474/1
#h = 474
#my1= my.crop((x,y,w,h))
#my1.show()# here we got bottom pencil in output.


# Rotate
#my1=my.rotate(90)
#my1.show()

# Color Transparency
red = Image.open("C:\\Users\\Tanujg\\OneDrive\\Desktop\\red.jpg")
#red.show()

blue = Image.open("C:\\Users\\Tanujg\\OneDrive\\Desktop\\blue.jpg")
#blue.show()
#blue.putalpha(0)
#blue.putalpha(255)
#blue.putalpha(128)
#blue.show() # here we get almost blank output

#red.putalpha(128)
#red.putalpha(0)
#red.show()
