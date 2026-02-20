import serial
import time

ser = serial.Serial ("COM7", 9600, timeout = 1)
#Aspetta al massimo un secondo che arrivi una riga dalla seriale
file_dati = open("semaforo.csv", "w")
file_dati.write("timestamp, valore, led \n")

print ("Attendo eventi dal pulsante di Arduino")
cont = 1
while True:
    linea = ser.readline().decode("utf-8").strip()

    if not linea:
        continue
#se non ce nessun dato entro il timeout, fai saltare il resto del ciclo e torna subito all'inizio del while
    if linea.startswith("EVENTO"):
        timestamp = time.strftime ("%H:%M:%S")
        file_dati.write(f"{timestamp}, {linea}, {cont}\n")
        file_dati.flush()
        if cont < 3:
            cont += 1
        else :
            cont = 1