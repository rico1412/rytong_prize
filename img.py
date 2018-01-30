from PIL import ImageTk, Image


def get_img(name):
    return ImageTk.PhotoImage(Image.open(name))
