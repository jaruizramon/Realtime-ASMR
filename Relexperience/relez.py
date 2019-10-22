# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:10:38 2019
@author: Pipo
"""

import os
import pyglet as sd
import time
import sys
from random import randint

from threading import Thread

def load_files(dict_, dir_, files):
    
    global sd
    
    right_side = [] # definition
    left_side = [] # left side of assignment
    
    
    for j in range(len(files)) :
    
        def_app = "sd.media.StaticSource(sd.media.load("+"\'"+ dir_ + files[j] + "\'))"
        key_app = files[j].replace('.ogg','').replace('.wav','')
        
        dict_.update({key_app:def_app})
        right_side.append(def_app)
        left_side.append(key_app) # add the variables
        
        call_this_var = left_side[j] + ' = ' + dict_.get(left_side[j])
        global_this_var = 'global ' + left_side[j] + '; ' + call_this_var
        exec(global_this_var)

        
        
#    exec(left_side[2] + '.play()')
    return left_side

def load_track(track, commander, vol, isLooped = False, randomSample = False, command_arr = []):
    
    global sd
    
    p = sd.media.Player()
    p.volume = vol

    if (isLooped == True):
        global looper
        looper = sd.media.SourceGroup(eval(commander).audio_format, None)
        looper.loop = True
        looper.queue(eval(commander))
        p.queue(looper)
        p.play()
        
    elif(isLooped == False):   
        
        while(True):
            for char in range(len(track)):
                if track[char] == '1':
#                    print(track[char])
                    p.queue(eval(commander))
                    p.play()
                    
                elif track[char] == '0':
#                    print(track[char])
                    pass
                
                randy = randint(0,18) # also randomize the index to play the sound randomly
                time.sleep(2 + randy)
                
    elif(isLooped == False and randomSample == True):
        
        random_index = randint(len(command_arr))
        
        while(True):
            for char in range(len(track)):
                if track[char] == '1':
#                    print(track[char])
                    p.queue(eval(command_arr[random_index]))
                    p.play()
                    
                elif track[char] == '0':
#                    print(track[char])
                    pass
                
                randy = randint(0,18) # also randomize the index to play the sound randomly
                time.sleep(2 + randy)
                
def main():
    global sd
    
    sd.lib.load_library('avbin64')
    sd.have_avbin = True
    
    a_sounds_dict = dict()
    o_sounds_dict = dict()
    r_sounds_dict = dict()
    
    ambient_dir = 'ambient/'
    occasio_dir = 'occasio/'
    randomp_dir = 'randomplay/'
    
    a_files = os.listdir(ambient_dir)
    r_files = os.listdir(randomp_dir)
    o_files = os.listdir(occasio_dir)
    
    print("Loading all files...")
    
    start_fileload = time.process_time()
    
    o_var = load_files(o_sounds_dict, occasio_dir, o_files)
    a_var = load_files(a_sounds_dict, ambient_dir, a_files)
    r_var = load_files(r_sounds_dict, randomp_dir, r_files)
    
    
    print("Files are loaded!!! \nTIME ELAPSED: " + str(time.process_time() - start_fileload))
    
    print(o_var)
    print(a_var)
    print(r_var)
    
    #load_track('0001000001001001010', o_var[1], False)

    #exec(o_var[0]+'.play()')
    #time.sleep(1)
    #exec(o_var[1]+'.play()')
    #time.sleep(1)
    #exec(o_var[2]+'.play()')
        
    trak1 = '010000001000100000000000100000010000100100000100000010000'
    trak2 = '000001000001001001010000010010010100000101001001010000000'
    trak4 = '100000001000000100000000000001000000000001000100000010000'
    trak3 = ''
#    trak5 = '000000010010001000000100000000000000000100000001000010000'
    trak6 = '000001000000000000000000000000000000000000000010000000000'
    trak7 = '001000000000000000000001000000000000000000000000000100000'
    
    #def load_track(track, commander, isLooped = False):
    
    t1_args = (trak1, o_var[1], .00003/10, False)
    t2_args = (trak2, o_var[4], .00003/10, False, True, o_var)
    t3_args = (trak3, a_var[3], .0009, True) 
    t4_args = (trak4, o_var[6], .00003, False)
#    t5_args = (trak5, o_var[5], .002, False)
    t6_args = (trak6, r_var[2], .050, False)
    t7_args = (trak7, r_var[1], .00002, False)
    
    #this whole block will be dynamically assigned by using n amount of tracks
    
    t1 = Thread(target=load_track, args=t1_args) # first track
    t2 = Thread(target=load_track, args=t2_args) # second track
    t3 = Thread(target=load_track, args=t3_args) # third track
    t4 = Thread(target=load_track, args=t4_args) # fourth track
#    t5 = Thread(target=load_track, args=t5_args) # fifth track
    t6 = Thread(target=load_track, args=t6_args) # sixth track
    t7 = Thread(target=load_track, args=t7_args) 
    
    # start all the processes first 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
#    t5.start()
    t6.start()
    t7.start()
    
    
    # join them in order to run them at the same time (supposedly)
    t1.join()
    t2.join()
    t3.join()
    t4.join() 
#    t5.join()
    t6.join()
    t7.join()
    
    check_exit = input("type and enter 'q' to stop sounds: ")
    
    if check_exit == 'q':
        looper.loop = False
        sys.exit()
        
'''

S T A R T

'''
if __name__ == '__main__':
    main()
    
