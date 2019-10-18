import tkinter as tk
def get_square(x, y, radius):
    '''
    given the center=(x,y) and radius
    calculate the square for the circle to fit into
    return x1, y1, x2, y2 of square's ulc=(x1,y1) and lrc=(x2,y2)
    '''
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2

def moire_pattern(im_orig):

    ImgW,ImgH=image.size

    NoiseW=ImgW*2
    NoiseH=ImgH*2

    im = Image.new('RGB', (NoiseW, NoiseH))
    draw = ImageDraw.Draw(im)
    linecolor = 255

    for k in range(1, NoiseW/2, 2):
        draw.ellipse(get_square(k, k, k), outline=(linecolor,linecolor,linecolor))
        draw.ellipse(get_square(NoiseW-k, k, k), outline=(linecolor,linecolor,linecolor))
        draw.ellipse(get_square(k, NoiseH-k, k), outline=(linecolor,linecolor,linecolor))
        draw.ellipse(get_square(NoiseW-k, NoiseH-k, k), outline=(linecolor,linecolor,linecolor))
    del draw     

    image5 = im_orig.convert("RGBA")

    left=random.randint(1, NoiseW-ImgW)
    top=random.randint(1, NoiseH-ImgH)

    image3 = im.crop((left, top, left+ImgW, top+ImgH))
    image6 = image3.convert("RGBA")
    datas = image6.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((item[0],item[1],item[2],50))

    image6.putdata(newData)    
    image5.paste(image6, (0, 0), image6)

    #im.show()    
    #im_orig.show()    
    #image5.show()    
    
    background = Image.new("RGB", image5.size, (255, 255, 255))
    background.paste(image5, mask=image5.split()[3]) # 3 is the alpha channel
    
    return background
