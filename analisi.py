from datetime import datetime
import dearpygui.dearpygui as dpg

with open('semaforo.csv', 'r') as f:
    righe = f.readlines()[1:] 
inizio_str = righe[0].split(', ')[0]
fine_str = righe[-1].split(', ')[0]

formato = "%H:%M:%S"
inizio_t = datetime.strptime(inizio_str, formato)
fine_t = datetime.strptime(fine_str, formato)

differenza = fine_t - inizio_t

print(f"Pressioni totali: {len(righe)}")
print(f"Tempo totale di utilizzo: {differenza}")

LED1 = 0
LED2 = 0
LED3 = 0
for riga in righe:
    led = riga.split(',')[-1].strip() 
    if led == "1":
        LED1 += 1
    elif led == "2":
        LED2 += 1
    elif led == "3":
        LED3 += 1
print(f"LED 1: {LED1} volte")
print(f"LED 2: {LED2} volte")
print(f"LED 3: {LED3} volte")

#Grafico con aiuto dell'intelligenza artificiale
x_values = []
y_values = []

for i, riga in enumerate(righe):
    led = riga.split(',')[-1].strip()
    x_values.append(i)   
    y_values.append(int(led))

dpg.create_context()

with dpg.window(label="Grafico LED", width=600, height=400):

    with dpg.plot(label="Sequenza LED", height=300, width=-1):
        dpg.add_plot_axis(dpg.mvXAxis, label="Pressione")
        dpg.add_plot_axis(dpg.mvYAxis, label="LED", tag="y_axis")
        dpg.add_line_series(x_values, y_values, parent="y_axis")

dpg.create_viewport(title="Grafico LED", width=700, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()