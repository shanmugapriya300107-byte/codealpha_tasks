# Smart File Organizer
# Created by R. Shanmugapriya
# CodeAlpha Python Internship

import os
import shutil
from datetime import datetime

print("=" * 50)
print("SMART FILE ORGANIZER")
print("=" * 50)

folder_path = input("Enter the folder path: ")

if not os.path.exists(folder_path):
    print("Invalid folder path!")

else:

    image_ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    document_ext = [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"]
    video_ext = [".mp4", ".avi", ".mkv", ".mov"]
    audio_ext = [".mp3", ".wav", ".aac"]

    moved_count = 0

    images = 0
    documents = 0
    videos = 0
    audio = 0
    others = 0

    folders = ["Images", "Documents", "Videos", "Audio", "Others"]

    for folder in folders:
        folder_location = os.path.join(folder_path, folder)

        if not os.path.exists(folder_location):
            os.mkdir(folder_location)

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            if extension in image_ext:
                destination = "Images"
                images += 1

            elif extension in document_ext:
                destination = "Documents"
                documents += 1

            elif extension in video_ext:
                destination = "Videos"
                videos += 1

            elif extension in audio_ext:
                destination = "Audio"
                audio += 1

            else:
                destination = "Others"
                others += 1

            destination_path = os.path.join(folder_path, destination)

            shutil.move(
                file_path,
                os.path.join(destination_path, file)
            )

            moved_count += 1

            print(f"Moved: {file} -> {destination}")

    report_file = os.path.join(folder_path, "report.txt")

    with open(report_file, "w") as report:

        report.write("SMART FILE ORGANIZER REPORT\n")
        report.write("=" * 35 + "\n\n")

        report.write(
            "Date and Time: "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            + "\n\n"
        )

        report.write(f"Total Files Moved: {moved_count}\n\n")

        report.write("Category Summary\n")
        report.write("-----------------\n")
        report.write(f"Images: {images}\n")
        report.write(f"Documents: {documents}\n")
        report.write(f"Videos: {videos}\n")
        report.write(f"Audio: {audio}\n")
        report.write(f"Others: {others}\n")

    print("\nFiles Organized Successfully!")
    print(f"Total Files Moved: {moved_count}")

    print("\nSummary")
    print("-------")
    print("Images:", images)
    print("Documents:", documents)
    print("Videos:", videos)
    print("Audio:", audio)
    print("Others:", others)

    print("\nReport generated successfully!")