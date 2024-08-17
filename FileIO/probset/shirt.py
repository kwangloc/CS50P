import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    try:
        extension_1 = ""
        extension_2 = ""
        valid_extension = [".jpg", ".jpeg", ".png"]
        for i in range(len(file_1)-1, -1, -1):
            if file_1[i] == ".":
                extension_1 = file_1[i:].lower()
        for i in range(len(file_2)-1, -1, -1):
            if file_2[i] == ".":
                extension_2 = file_2[i:].lower()
        if extension_1 != extension_2:
            sys.exit("Input and output have different extensions")
        if extension_1 not in valid_extension:
            sys.exit("Invalid output")
        try:
            with Image.open(file_1) as im_1:
                with Image.open("shirt.png") as im_shirt:
                    im_tmp = ImageOps.fit(im_1, im_shirt.size)
                    im_tmp.paste(im_shirt, im_shirt)
                    im_tmp.save(file_2)
            # im_1 = Image.open(file_1)
            # im_shirt = Image.open("shirt.png")

            # im_tmp = ImageOps.fit(im_1, im_shirt.size)
            # im_tmp.paste(im_shirt, im_shirt)
            # im_tmp.save(file_2)
            
            # im_1.close()
            # im_shirt.close()
        except FileNotFoundError:
            sys.exit("File not found")
    except IndexError:
        pass

def check_extension(file_name):
    try:
        for i in range(len(file_name)-1, -1, -1):
            if file_name[i] == ".":
                extension = file_name[i:]
                return extension
        return None
    except IndexError:
        pass

if __name__ == "__main__":
    main()