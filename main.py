import pyttsx3
import numpy as np
import os
import random

base_dir = "dataset"
if not os.path.exists(base_dir):
    os.mkdir("dataset")
    
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")

if not os.path.exists(train_dir):
    os.mkdir(train_dir)
if not os.path.exists(val_dir):
    os.mkdir(val_dir)
    
train_buka_dir = os.path.join(train_dir, "buka")
train_tutup_dir = os.path.join(train_dir, "tutup")

if not os.path.exists(train_buka_dir):
    os.mkdir(train_buka_dir)
if not os.path.exists(train_tutup_dir):
    os.mkdir(train_tutup_dir)

val_buka_dir = os.path.join(val_dir, "buka")
val_tutup_dir = os.path.join(val_dir, "tutup")

if not os.path.exists(val_buka_dir):
    os.mkdir(val_buka_dir)
if not os.path.exists(val_tutup_dir):
    os.mkdir(val_tutup_dir)
    
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def make_dataset_sound(voices, text, dir, total_data):
    rate = np.linspace(0, 150, total_data)
    for i in range(len(rate)):
        if i < int(len(rate)*0.75):
            engine.setProperty('rate', rate[i])
            engine.setProperty('volume', random.uniform(0,1))
            engine.setProperty('voice', voices[int(np.round(random.uniform(0,1)))].id)
            engine.save_to_file(f"{text}", f"{dir}/train/{text}/{text}_{i}.wav")
        else:
            engine.setProperty('rate', rate[i])
            engine.setProperty('volume', random.uniform(0,1))
            engine.setProperty('voice', voices[int(np.round(random.uniform(0,1)))].id)
            engine.save_to_file(f"{text}", f"{dir}/val/{text}/{text}_{i}.wav")
        engine.runAndWait()

if __name__ == "__main__":
    print("Dataset mulai dibuat")
    make_dataset_sound(voices, "buka", base_dir, 200)
    make_dataset_sound(voices, "tutup", base_dir, 200)
    print("Dataset selesai dibuat")