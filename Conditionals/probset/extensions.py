def main():
    file_name = input("File name: ")
    print(extension(file_name))
 
def extension(file_name):
    dict_extensions = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    file_extension = ""
    file_name = file_name.strip()
    for i in range(len(file_name)-1, -1, -1):
        if file_name[i] == '.':
            file_extension = file_name[i:].lower()
            break 
    media_type = dict_extensions.get(file_extension, "application/octet-stream")
    return media_type

if __name__ == "__main__":
    main()