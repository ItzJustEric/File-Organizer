import os
import shutil

def find_folder(folder_name):
    for root, dirs, files in os.walk("C:\\"):  # Start searching from the root directory
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None

folder_path = input("Enter the folder path: ")
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
            target_folder = find_folder("Images") or os.path.join(folder_path, "Images")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
        elif file.endswith(tuple(Docs)):
            target_folder = find_folder("Docs") or os.path.join(folder_path, "Docs")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
        elif file.endswith(tuple(Media)):
            target_folder = find_folder("Media") or os.path.join(folder_path, "Media")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
        elif file.endswith(tuple(Other)):
            target_folder = find_folder("Other") or os.path.join(folder_path, "Other")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)

organize_files()