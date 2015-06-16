import pygame, sys, os
import pygame.camera
import time, random
import base64
from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"
THRESHOLD = 500
FORMAT = pyaudio.paInt16
RATE = 44100

class Audio(object):
    def __init__(self):
        pass

    def is_silent(self,snd_data):
        return max(snd_data) < THRESHOLD
    
    def normalize(self,snd_data):
        MAXIMUM = 16384
        times = float(MAXIMUM)/max(abs(i) for i in snd_data)
        
        r = array('h')
        for i in snd_data:
            r.append(int(i*times))
        return r
    def trim(self, snd_data):
        def _trim(snd_data):
            snd_started = False
            r = array('h')
    
            for i in snd_data:
                if not snd_started and abs(i)>THRESHOLD:
                    snd_started = True
                    r.append(i)
    
                elif snd_started:
                    r.append(i)
            return r

        # Trim to the left
        snd_data = _trim(snd_data)
    
        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data
    
    
    def add_silence(self,snd_data, seconds):
        r = array('h', [0 for i in xrange(int(seconds*RATE))])
        r.extend(snd_data)
        r.extend([0 for i in xrange(int(seconds*RATE))])
        return r
    
    def record(self, CHUNK_SIZE):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, 
                        channels=1, 
                        rate=RATE,
                        input=True, 
                        output=True,
                        frames_per_buffer=CHUNK_SIZE)
    
        num_silent = 0
        snd_started = False
    
        r = array('h')
    
        while 1:
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)
    
            silent = self.is_silent(snd_data)
    
            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True
    
            if snd_started and num_silent > 30:
                break
    
        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()
    
        r = self.normalize(r)
        r = self.trim(r)
        r = self.add_silence(r, 0.5)
        return sample_width, r

    
    def getAudio(self):
        pass
    
    def getAudioData(self, size = 1024 * 10):
        path = self.captureAudio(size)
        with open(path, "rb") as audio_file:
            encoded_string = base64.b64encode(audio_file.read())
        return encoded_string
        

    def captureAudio(self, size):
        filename = "%s/%s.wav" % (SAVEDIR, 'audio')
        sample_width, data = self.record(size)
        data = pack('<' + ('h'*len(data)), *data)
    
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
        return filename