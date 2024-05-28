def tesk12():
    import os
    from PIL import Image, ImageFilter
    
    os.mkdirs(usefoto)
    os.mkdirs(foto)
    
    smooth_img = img.filter(ImageFilter.SMOOTH)
    
    for img1 in os.listdir(foto):
        if img1.endswith((".jpg", ".png", ".bmp")):
            image = Image.open(os.path.join(foto, img1))
            usefoto = smooth_img(image)
            usefoto.save(os.path.join(usefoto, img1))
tesk12()
