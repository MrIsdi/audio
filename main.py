import pyttsx3
import numpy as np
import os
import random

base_dir = "dataset"
if not os.path.exists(base_dir):
    os.mkdir("dataset")
    
buka_dir = os.path.join(base_dir, "buka")
tutup_dir = os.path.join(base_dir, "tutup")

if not os.path.exists(buka_dir):
    os.mkdir(buka_dir)
if not os.path.exists(tutup_dir):
    os.mkdir(tutup_dir)
    
buka_train_dir = os.path.join(buka_dir, "train")
buka_val_dir = os.path.join(buka_dir, "val")

if not os.path.exists(buka_train_dir):
    os.mkdir(buka_train_dir)
if not os.path.exists(buka_val_dir):
    os.mkdir(buka_val_dir)

tutup_train_dir = os.path.join(tutup_dir, "train")
tutup_val_dir = os.path.join(tutup_dir, "val")

if not os.path.exists(tutup_train_dir):
    os.mkdir(tutup_train_dir)
if not os.path.exists(tutup_val_dir):
    os.mkdir(tutup_val_dir)
    
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def make_dataset_sound(voices, text, dir, total_data):
    rate = np.linspace(0, 150, total_data)
    for i in range(len(rate)):
        if i < int(len(rate)*0.75):
            engine.setProperty('rate', rate[i])
            engine.setProperty('volume', random.uniform(0,1))
            engine.setProperty('voice', voices[int(np.round(random.uniform(0,1)))].id)
            engine.save_to_file(f"{text}", f"{dir}/train/{text}_{i}.wav")
        else:
            engine.setProperty('rate', rate[i])
            engine.setProperty('volume', random.uniform(0,1))
            engine.setProperty('voice', voices[int(np.round(random.uniform(0,1)))].id)
            engine.save_to_file(f"{text}", f"{dir}/val/{text}_{i}.wav")
        engine.runAndWait()

if __name__ == "__main__":
    print("Dataset mulai dibuat")
    make_dataset_sound(voices, "buka", buka_dir, 200)
    make_dataset_sound(voices, "tutup", tutup_dir, 200)
    print("Dataset selesai dibuat")