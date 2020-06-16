import time
import vlc
lofi = vlc.MediaPlayer('./projeto2/book-notes/sound/lofi.mp3')

def pomodoroTimer(numVezes,minutos, descansar):
    numTocados=0
    while not(numVezes==numTocados):
        lofi.play()
        for i in range(minutos, 0, -1):
            for j in range(60,0,-1):
                print("\n"*20)
                print("Comece a ler o Livro, sem distrações!")
                if j>10:
                    print("{}:{}".format(i-1,j-1))
                else:
                    print("{}:0{}".format(i-1,j-1))
                time.sleep(1)
        for i in range(descansar, 0, -1):
            lofi.stop()
            for j in range(60,0,-1):
                print("\n"*20)
                print("Agora você pode descansar!")
                if j>10:
                    print("\r{}:{}".format(i-1,j-1))
                else:
                    print("\r{}:0{}".format(i-1,j-1))
                time.sleep(1)
        numTocados+=1
    print ("\nFim do Pomodoro")
