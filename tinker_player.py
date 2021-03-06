import sounddevice                   # for recording audio
import wavio                         # for generating audio file
import vlc                           # for playing audio
import time                          # for code funcionality


print("\n\n! ! !   Welcome to Tinker Player   ! ! !\n\n")
print("1. Audio Recorder \n2. Audio Player")
choice = int(input("\nEnter your choice: "))



if choice == 1:  # Recording an audio

    frequency = 48000   # defualt frequency for recording

    name = input("Enter a name for your file (without any extension): ")   # Naming the audio file
    time_limit = int(input("Enter the duration of audio (in seconds): "))  # duartion of the audio


    # Initiating recording for the given time
    recording = sounddevice.rec(int(time_limit * frequency), samplerate = frequency, channels=2)
    sounddevice.wait()


    #Generating the record into an audio file
    wavio.write(name + ".wav", recording, frequency, sampwidth = 2)



elif choice == 2:  # Playing Audio

    name = input("Enter the file name (with path & extension): ")  

    player = vlc.MediaPlayer(name)          # Initiating Audio Player
    player.play()
    time.sleep(60)
    player.stop()
    

else:
    print("Invalid input")
    

