from PIL import Image, ImageDraw, ImageFont

achtergrond = Image.open("meme_achtegrond.jpg")

breedte = achtegrond.width
hoogte = achtegrond.height

lettertype = ImageFont.truetype("impact.ttf", 20)

tekengebied = ImageDraw.Draw(achtegrond)

tekst = "Haha bread go BRRRRR"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

achtegrond.show()

achtegrond.save("Meme_met_tekst.jpg")