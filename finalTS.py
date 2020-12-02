import pyaudio 
import numpy as np
import wave
from tkinter import *

ventan = Tk()
ventan.title("Analisis")
ventan.configure(bg='beige')

ventan.geometry("350x300")

#formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100

#tamaño de chunk
CHUNK = 2048

SEGUNDOS_GRABACION = 1


frec_actual = StringVar()
sonido_cuerda = StringVar()
afinacion = StringVar()





window = np.blackman(CHUNK)
def iniciar():
    
    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        #"2048h"
        waveData = wave.struct.unpack("%dh"%(CHUNK), data)
        npData=np.array(waveData)

        dataEntrada = npData * window
        fftData = np.abs(np.fft.rfft(dataEntrada))

        indice_frec_dominante = fftData[1:].argmax() + 1
        
        #cambio de indice  Hz
        y0,y1,y2 = np.log(fftData[indice_frec_dominante-1: indice_frec_dominante+2])
        x1 =(y2 - y0) * 0.5/(2 * y1 -y2 - y0)
        frec_dominante = (indice_frec_dominante + x1)* FRECUENCIA_MUESTREO/CHUNK
        frecuencia = str(frec_dominante)
        print ("frecuencia dominante: "+ str(frec_dominante) + "Hz", end='\r')
        frec_actual.set(frecuencia)
        
        tolerancia=13
        tolerancia_afinacion = 1.3

        if frec_dominante > 82.4 - tolerancia and frec_dominante < 82.4 + tolerancia:
            cuerda= "6ta Mi con una frecuencia de 82.4 Hz"
            if frec_dominante >82.4 - tolerancia_afinacion and frec_dominante < 82.4 + tolerancia_afinacion:
                Afinacion = "la afinacion es la correcta"
            elif frec_dominante < 82.4 + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frec_dominante > 110.0 - tolerancia and frec_dominante < 110.0 + tolerancia:
            cuerda= "5ta La con una frecuencia de 110.0 Hz"
            if frec_dominante >110.0 - tolerancia_afinacion and frec_dominante < 110.0 + tolerancia_afinacion:
                Afinacion = "la afinacion es correcta"
            elif frec_dominante < 110.0 + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frec_dominante > 146.83 - tolerancia and frec_dominante < 146.83 + tolerancia:
            cuerda= "4ta Re con una frecuencia de 146.83 Hz"
            if frec_dominante >146.83 - tolerancia_afinacion and frec_dominante < 146.83 + tolerancia_afinacion:
                Afinacion = "la afinacion es la correcta"
            elif frec_dominante < 146.83 + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frec_dominante > 196.0 - tolerancia and frec_dominante < 196.0 + tolerancia:
            cuerda= "3ra Sol con una frecuencia de 196.0 Hz"
            if frec_dominante >196.0 - tolerancia_afinacion and frec_dominante < 196.0 + tolerancia_afinacion:
                Afinacion = "la afinacion es la correcta"
            elif frec_dominante < 196.0 + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"
        
        elif frec_dominante > 246.94- tolerancia and frec_dominante < 246.94 + tolerancia:
            cuerda= "2da Si con una frecuencia de 246.94 Hz"
            if frec_dominante >246.94 - tolerancia_afinacion and frec_dominante < 246.94 + tolerancia_afinacion:
                Afinacion = "la afinacion es la correcta"
            elif frec_dominante < 246.94 + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frec_dominante > 329.63 - tolerancia and frec_dominante < 329.63  + tolerancia:
            cuerda= "1ra Mi con una frecuencia de  329.63 Hz"
            if frec_dominante >329.63  - tolerancia_afinacion and frec_dominante < 329.63  + tolerancia_afinacion:
                Afinacion = "la afinacion es la correcta"
            elif frec_dominante < 329.63  + tolerancia_afinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"
        else:
            cuerda = "la cuerda no ha identificada"
            Afinacion = "presione de nuevo el boton de ingresar"
        

        sonido_cuerda.set(cuerda)
        
        afinacion.set(Afinacion)


        


    
    if __name__=="__main__":
   
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES, rate=FRECUENCIA_MUESTREO, input=True, frames_per_buffer=CHUNK)
        
        for i in range(0, int(FRECUENCIA_MUESTREO * SEGUNDOS_GRABACION / CHUNK)):
            analizar(stream)


        
        stream.stop_stream()
        stream.close()
        p.terminate()
    

boton = Button(ventan, text="Ingresar", command=iniciar, background="pink")
boton.pack(pady=21)

etiquetaCuerda = Label(ventan, textvariable=sonido_cuerda, background="beige")
etiquetaCuerda.pack()

etiqueta1=Label(ventan, textvariable=frec_actual, background="beige")
etiqueta1.pack()

etiquetaAfinacion = Label(ventan, textvariable=afinacion, background="beige")
etiquetaAfinacion.pack()


ventan.mainloop()  
   
    





boton = Button(ventan, text="Iniciar", command=iniciar)
boton.pack()

ventan.mainloop()
