from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
import math

pro_path = "/home/sun/code/WeChatOA"
im_path = "/home/sun/code/WeChatOA/timg.jpeg"
font = ImageFont.load_default()

def add_text2img(img, text, font= font):
    img_draw = ImageDraw.Draw(img)

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if not in_center(im.size[0] / 2, im.size[1] / 2, min(im.size) / 2, x, y):
                img_draw.point((x, y), fill=(255, 255, 255, 0))

    # if img.size[0] < img.size[1]:
    #     x0 = 0
    #     x1 = img.size[0]
    #     y0 = (img.size[1] - x1) / 2
    #     y1 = (img.size[1] + x1) / 2
    # else:
    #     y0 = 0
    #     y1 = img.size[1]
    #     x0 = img.size[0] - y1 / 2
    #     x1 = img.size[0] + y1 / 2
    # img_draw.arc([x0, y0, x1, y1], 0, 360, fill= (0, 0, 0, 0))

    text_size_x, text_size_y = img_draw.textsize(text, font)
    print(text_size_x, text_size_y)
    text_xy = ((img.size[0] - font.getsize(text)[0]) / 2, (img.size[1] - font.getsize(text)[1]) / 2)
    print(text_xy)
    img_draw.text(text_xy, text, font= font, fill="red")


def create_img(img):
    size = (min(img.size), min(img.size))
    mask = Image.new("L", size, 255)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill = 0)
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.paste(0, mask = mask)
    output.convert("P", palette=Image.ADAPTIVE)
    output.save("output.jpg")




def in_center(center_x, center_y, r, x, y):
    return math.pow(math.pow(math.fabs(center_x - x), 2) + math.pow(math.fabs(center_y - y), 2), 0.5) < r


if __name__ == '__main__':
    im = Image.open(im_path)
    # im.show()
    # im = im.rotate(45)#.show()
    print(im.size)

    create_img(im)


    font_path = os.path.join(pro_path, "/fonts/Ubuntu-C.ttf")
    font = ImageFont.truetype(font_path, 80)
    # add_text2img(im, "sunhaihong", font)
    # im.show()
    # im.rotate(-45).show()
    # im.save("circle7.jpg")
    # im.rotate(135).show()
