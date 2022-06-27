import os


path = "D:\Down\\"
VERBOSE = True
obj = os.scandir(path)

file_extensions = {'documents': ['pptx','docx','xlsx','pdf'], 'archives': ['rar', 'zip', '7z', 'tar.gz'], 'iso': ['iso'], 
                   'images': ['img', 'png', 'jpg', 'jpeg', 'gif', 'ico', 'webp', 'ase'], 'apps': ['exe', 'msi'], 'code': ['py', 'html', 'css', 'cpp', 'sh'],
                   'torrent': ['torrent'], 'multimedia': ['mp3', 'mp4', 'webm', 'ogg', 'wav'], 'text': ['txt'], 'mods': ['jar'], 'other': '' }

end_path = "D:\Download\\"
extensions = list(file_extensions.items())


for (key, values) in extensions:
    try:
        os.mkdir(end_path + key, 0o777)
    except FileExistsError:
        if VERBOSE:
            print(key, "exists")
        else: pass


for entry in obj:
    if entry.is_file():
        file = entry.name
        file_extension = file.split('.')[-1]
        
        for (key, values) in extensions:
                for value in values:
                    if file_extension == value or file_extension == value.upper():
                        if VERBOSE:
                            print(f"{file} has been moved")
                        os.replace(path+file, end_path+key+'\\' + str(file))
 
                                        
# other

other_files = os.scandir(path)   
for entry in other_files:
    file = entry.name
    if VERBOSE:
        print(f"{file} has been moved")
    os.replace(path + file, end_path+ 'other\\' + file)                

     
obj.close()