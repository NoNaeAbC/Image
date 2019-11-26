from MyImage3 import *



def SquareFilter(img):
	Img = MyImage(img) # copy original
	w, h = Img.getSize()
	for x in range(w):
		for y in range(h):
			Img[x,y] = img[x,y]**2
	return Img


def KantenKernel(img):
	Img = MyImage(img) # copy original
	w, h = Img.getSize()
	for x in range(w-2):
		for y in range(h-2):
			Img[x+1,y+1] = (img[x+1,y+1]*8+img[x+1,y]*-1+img[x+2,y+1]*-1+img[x+1,y+2]*-1+img[x,y+1]*-1+img[x,y]*-1+img[x+2,y+2]*-1+img[x,y+2]*-1+img[x+2,y]*-1)
	return Img

def SharpKernel(img):
	Img = MyImage(img) # copy original
	w, h = Img.getSize()
	for x in range(w-2):
		for y in range(h-2):
			Img[x+1,y+1] = (img[x+1,y+1]*9+img[x+1,y]*-1+img[x+2,y+1]*-1+img[x+1,y+2]*-1+img[x,y+1]*-1+img[x,y]*-1+img[x+2,y+2]*-1+img[x,y+2]*-1+img[x+2,y]*-1)
	return Img

def BlurKernel(img):
	Img = MyImage(img) # copy original
	w, h = Img.getSize()
	for x in range(w-2):
		for y in range(h-2):
			Img[x+1,y+1] = (img[x+1,y+1]*8+img[x+1,y]*1+img[x+2,y+1]*1+img[x+1,y+2]*1+img[x,y+1]*1+img[x,y]*1+img[x+2,y+2]*1+img[x,y+2]*1+img[x+2,y]*1)/16
	return Img

def BW(img):
	Img = MyImage(img)  # copy original
	w, h = Img.getSize()
	for x in range(w):
		for y in range(h):
			if(img[x, y]>90):
				Img[x, y] = 255
			elif (img[x, y] <= 90):
				Img[x, y] = 0
	return Img

def And(img1,img2):
	Img = MyImage(img1)  # copy original
	w, h = Img.getSize()
	for x in range(w):
		for y in range(h):
			if((img1[x, y]>127)or(img2[x,y]>127)):
				Img[x, y] = 255
			else :
				Img[x, y] = 0
	return Img
def Add(img1,img2):
	Img = MyImage(img1)  # copy original
	w, h = Img.getSize()
	for x in range(w):
		for y in range(h):
			Img[x,y]=(img1[x, y]+img2[x,y])/2
	return Img

img = MyImage("brain.png")

img.show()

img4 = KantenKernel(img)
img4 = BlurKernel(img4)
#BW(img4).show()
img4.show()

img5 = SharpKernel(img)
img5 = BlurKernel(img5)
#BW(img5).show()
img5.show()
Add(BW(img4),BW(img5)).show()
