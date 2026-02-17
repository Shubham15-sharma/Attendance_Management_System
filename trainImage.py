import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image


# Train Image
def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message,text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully"  # +",".join(str(f) for f in Id)
    message.configure(text=res)
    text_to_speech(res)


def getImagesAndLables(path):
    # Get all subdirectories (student folders)
    imagePath = []
    Ids = []
    faces = []
    
    try:
        for student_dir in os.listdir(path):
            student_path = os.path.join(path, student_dir)
            # Only process directories
            if not os.path.isdir(student_path):
                continue
                
            # Extract enrollment ID from directory name
            try:
                Id = int(student_dir.split("_")[0])
            except (ValueError, IndexError):
                print(f"Skipping invalid directory name: {student_dir}")
                continue
            
            # Process all images in this student's directory
            for img_file in os.listdir(student_path):
                if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    try:
                        img_path = os.path.join(student_path, img_file)
                        pilImage = Image.open(img_path).convert("L")
                        imageNp = np.array(pilImage, "uint8")
                        faces.append(imageNp)
                        Ids.append(Id)
                    except Exception as e:
                        print(f"Error processing {img_file}: {e}")
                        continue
    except Exception as e:
        print(f"Error reading training directory: {e}")
    
    return faces, Ids
