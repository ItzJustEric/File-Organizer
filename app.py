import os
import shutil




folder_path  = ("C:\\Users\\Eric\\Desktop\\testFolder")
os.startfile(folder_path)

def organize_files():
    Image = [".jpg", ".jpeg", ".png", ".gif"]
    Docs = [".doc", ".docx", ".txt", ".pdf"]
    Media = [".mp4", ".mp3", ".mkv", ".avi"]
    Other = [".exe", ".zip", ".tar", ".iso"]

    folder = os.listdir(folder_path)

    for file in folder:
        file_path = os.path.join(folder_path, file)

        if file.endswith(tuple(Image)):
            os.makedirs(os.path.join(folder_path, "Images"))
            shutil.move(file_path,os.path.join(folder_path, "Images"))
        elif file.endswith(tuple(Docs)):
            os.makedirs(os.path.join(folder_path,"Docs"))
            shutil.move(file_path,os.path.join(folder_path,"Docs"))
        elif file.endswith(tuple(Media)):
            # os.makedirs(os.path.join(folder_path,"Media"))
            shutil.move(file_path,os.path.join(folder_path,"Media"))
        elif file.endswith(tuple(Other)):
            os.makedirs(os.path.join(folder_path,"Other"))
            shutil.move(file_path,os.path.join(folder_path,"Other"))

organize_files()

        

        
        

# def organize_images():
#     if not os.path.exists("Images"):
#         os.makedirs("Images")
        




# def organzie_docs():
#     if not os.path.exists("Docs"):
#         os.makedirs("Docs")



# def organize_media():
#     if not os.path.exists("Media"):
#         os.makedirs("Media")


# def organize_other():
#     if not os.path.exists("Other"):
#         os.makedirs("Other")