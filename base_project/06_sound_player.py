# پخش صدا در پایتون - جایگزین‌های playsound
# مباحث: ماژول‌ها، مدیریت خطا، فایل‌ها

import pygame
import time
import os
from pathlib import Path

def play_with_pygame(file_path):
    """پخش فایل صوتی با pygame"""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # صبر تا پایان پخش
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except pygame.error as e:
        print(f"خطا در پخش صدا: {e}")
    except FileNotFoundError:
        print(f"فایل یافت نشد: {file_path}")

def play_system_sound():
    """پخش صدای سیستم ویندوز"""
    try:
        import winsound
        winsound.MessageBeep(winsound.MB_OK)
    except ImportError:
        print("winsound فقط در ویندوز در دسترس است")

def create_simple_beep():
    """ایجاد صدای ساده با pygame"""
    try:
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # تولید صدای بوق
        duration = 0.5  # ثانیه
        sample_rate = 22050
        frames = int(duration * sample_rate)
        
        # فرکانس 440 هرتز (نت لا)
        arr = []
        for i in range(frames):
            time_val = i / sample_rate
            wave = int(32767 * 0.3 * (1 if (int(time_val * 440 * 2) % 2) else -1))
            arr.append([wave, wave])
        
        sound = pygame.sndarray.make_sound(pygame.array.array(arr))
        sound.play()
        time.sleep(duration)
        
    except Exception as e:
        print(f"خطا در ایجاد صدا: {e}")

def main():
    print("انتخاب کنید:")
    print("1. پخش فایل صوتی")
    print("2. صدای سیستم")
    print("3. صدای ساده")
    
    choice = input("شماره انتخاب: ").strip()
    
    if choice == "1":
        file_path = input("مسیر فایل صوتی: ").strip()
        if Path(file_path).exists():
            play_with_pygame(file_path)
        else:
            print("فایل یافت نشد")
            
    elif choice == "2":
        play_system_sound()
        
    elif choice == "3":
        create_simple_beep()
        
    else:
        print("انتخاب نامعتبر")

if __name__ == "__main__":
    main()
