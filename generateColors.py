from PIL import Image
input = Image.open("canvas.png")
input.resize((int(input.width ), int(input.height)))
palette = []

def averageColor(pixels):
    r = 0
    g = 0
    b = 0
    for pixel in pixels:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]
    r /= len(pixels)
    g /= len(pixels)
    b /= len(pixels)
    return((r,g,b))


from PIL import ImageEnhance
#input.quantize(20, method=1).save("imageTest1.png")
#input.quantize(20, method=2).save("imageTest2.png")

lowc = input.convert("RGB", colors=20, palette=Image.Palette.ADAPTIVE)
lowcSaturated = ImageEnhance.Color(lowc.convert("RGB")).enhance(3)

#lowcSaturated.resize((int(input.width / 5), int(input.height /5))).save("imageTest5.png")
print("jndkjgn")
colors = []
for dot in range(1, 448):
    try:
        dot = Image.open("ddc." + str(dot + 8000) + "-200x200.jpg")
        colors.append(dot.convert("RGB", colors=1, palette=Image.Palette).getpixel((2,2)))
    except:
        pass

lowcSaturated.convert("RGB", colors=20, palette=colors).save("imageDotz1.png")

from PIL import ImageDraw


grid = Image.new("RGB", (816,1056))
def createDot(color):
    dot = Image.open("Dot.png")
    print(dot)
    for x in range(dot.width):
        for y in range(dot.height):
            
            if dot.getpixel((x,y)) == (0,0,0,255):
                dot = dot.putpixel((x,y), color)
                #dot = ImageDraw.Draw(dot).text((3/4 * dot.height, 1/4 * dot.width), str(colors.index(color)))
    dot.save("dot2.png")
createDot(colors[5])