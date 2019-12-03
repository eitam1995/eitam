import math
import wave_helper
import os.path


def get_file():
    file_name = input("insert a file name you want to turn to music")
    is_file_exc = os.path.isfile(file_name)
    while not is_file_exc:
        print("wrong file name")
        file_name = input("insert a file name you want to turn to music")
        is_file_exc = os.path.isfile(file_name)
    return file_name
def reverseaudio(lst_music):
    return lst_music[::-1]
def accelerate(music_list):
    newlst=[]
    for i in range(0,len(music_list),2):
        newlst.append(music_list[i])
    return newlst
def decelerate(music_list):
    newlst=[]
    for i in range(len(music_list)):
        newlst.append(music_list[i])
        if i+1<len(music_list):
            x = int((music_list[i][0]+music_list[i+1][0])/2)
            y = int((music_list[i][1]+music_list[i+1][1])/2)
            newlst.append([x,y])
    return newlst
def volume_up(music_list):
    newlst=[]
    for i in range(len(music_list)):
        x = int(music_list[i][0] * 1.2)
        y = int(music_list[i][1] * 1.2)
        if x > 32767:
            x = 32767
        if y > 32767:
            y = 32767
        if x < (-32768):
            x = (-32768)
        if y < (-32768):
            y = (-32768)
        newlst.append([x,y])
    return newlst
def volume_down(music_list):
    newlst = []
    for i in range(len(music_list)):
        x = int(music_list[i][0] / 1.2)
        y = int(music_list[i][1] / 1.2)
        newlst.append([x, y])
    return newlst
def dimming(music_list):
    newlst=[]
    for i in range(len(music_list)):
        if i>0 and i+1<len(music_list):
            x = int((music_list[i-1][0]+music_list[i][0]+music_list[i+1][0])/3)
            y = int((music_list[i-1][1]+music_list[i][1]+music_list[i+1][1])/3)
        elif i==0:
            x = int((music_list[i][0] +
                     music_list[i + 1][0]) / 2)
            y = int((music_list[i][1] +
                     music_list[i + 1][1]) / 2)
        elif i+1==len(music_list):
            x = int((music_list[i][0] +
                     music_list[i - 1][0]) / 2)
            y = int((music_list[i][1] +
                     music_list[i - 1][1]) / 2)
        newlst.append([x,y])
    return newlst
def menu():
    file_name = get_file()
    music_list=wave_helper.load_wave(file_name)
    music_menu(music_list)
def music_menu(music_list):
    valid=True
    while valid:
        x = int(input("choose one of the options for editing \n 1. reverse audio \n"
             " 2.accelerate audio \n 3.decelerate audio \n"
             " 4. raise volume\n 5. decrease volume \n 6.dimming \n"
              " 7.exit and save file"))
        if x==1:
           music_list=reverseaudio(music_list)
           print("the audio has been reversed")
        elif x==2:
            music_list=accelerate(music_list)
            print("the audio has been accelerated")
        elif x==3:
            music_list=decelerate(music_list)
            print("the audio has been decelerated")
        elif x==4:
            music_list=volume_up(music_list)
            print("the volume in the audio has been increased")
        elif x==5:
            music_list=volume_down(music_list)
            print("the volume in the audio has been decreased")
        elif x==6:
            music_list=dimming(music_list)
            print("the audio has been dimmed")
        elif x==7:
            file_name=input("insert a file name for the new file")
            wave_helper.save_wave(2000, music_list, file_name)
            break
        else:
            print("invalid input")
        print(music_list)


print(reverseaudio([[1,2],[3,4],[5,6],[7,8]]))
print(accelerate([[1,2],[3,4],[5,6]]))
print(decelerate([[1,2],[3,4],[5,6],[7,8]]))
print(volume_up([[31666,2],[24,4],[50,6],[7,8]]))
print(volume_down([[31666,2],[24,4],[50,6],[7,8]]))
print(dimming([[1, 1], [7, 7], [20, 20], [9, 9], [-12, -12]]))
music_menu([[1, 1], [7, 7], [20, 20], [9, 9], [-12, -12],[31666,2],[24,4],[50,6],[7,8]])

