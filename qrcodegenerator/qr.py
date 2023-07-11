import qrcode
img=qrcode.make("https://www.youtube.com/channel/UCueYcgdqos0_PzNOq81zAFg")
img.save("youtube_qr.png.png")
print("created")
