from PIL import Image, ImageChops

pic1 = Image.open("lemur.png").convert("1")
pic2 = Image.open("code.png").convert("1")

ans = ImageChops.logical_xor(pic1, pic2)
ans.save("answer.png")

#image quality is awful. Becomes clearer the more you move away
#exclamtion point at the end of the code was just a guess as it basically invisible in picture