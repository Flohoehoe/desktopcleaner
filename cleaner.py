import os
import shutil

dateiPfad2 = "C:/Users/Flo/Desktop/cleanup/"
dateiPfad = "C:/Users/Flo/Desktop/"
names = os.listdir(dateiPfad)
folderName = ['image', 'text', 'zips']
for x in range(0, 3):
    if not os.path.exists(dateiPfad2+folderName[x]):
        os.makedirs(dateiPfad2+folderName[x])
for files in names:
    # images
    if ".png" in files and not os.path.exists(dateiPfad2+'image/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+"image/"+files)
    if ".jpg" in files and not os.path.exists(dateiPfad2+'image/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+"image/"+files)
    if ".jpeg" in files and not os.path.exists(dateiPfad2+'image/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+"image/"+files)
    if ".skp" in files and not os.path.exists(dateiPfad2+'image/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+"image/"+files)
    # text files
    if ".txt" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".docx" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".pdf" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".tex" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".json" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".ini" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".xls" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".sh3d" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    if ".chum5" in files and not os.path.exists(dateiPfad2+'text/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'text/'+files)
    # archieve
    if ".rar" in files and not os.path.exists(dateiPfad2+'zips/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'zips/'+files)
    if ".zip" in files and not os.path.exists(dateiPfad2+'zips/'+files):
        shutil.move(dateiPfad+files, dateiPfad2+'zips/'+files)
