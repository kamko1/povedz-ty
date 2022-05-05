import tkinter

w = 500
h = 300
canvas = tkinter.Canvas(width = w, height = h)
canvas.pack()
vaha = float(input("Zadajte vašu hmotnosť: "))
vyska = float(input("Zadajte vašu výšku (v cm): "))
canvas.create_rectangle(0, 100, 240, 200, fill = "yellow", outline="")
canvas.create_rectangle(240, 100, 330, 200, fill = "green", outline="")
canvas.create_rectangle(330, 100, 390, 200, fill = "orange", outline="")
canvas.create_rectangle(390, 100, 500, 200, fill = "red", outline="")
def vypocitaj_bmi():
    m = vyska/100
    bmi = round(vaha/(m**2))
    if 0 <= bmi < 17.5:
        canvas.create_text(250, 230, text="podvýživa", font=("Arial","15", "bold"), fill="yellow")
        canvas.create_text(250, 250, text=f"BMI = {bmi}", font=("Arial","15", "bold"), fill="yellow")
        a = (bmi*500)/40+17.5
        canvas.create_rectangle(a, 90, a+5, 210, fill="black")
    if 17.5 <= bmi <= 25:
        canvas.create_text(250, 230, text="ideálna a zdravá váha", font=("Arial","15", "bold"), fill="green")
        canvas.create_text(250, 250, text=f"BMI = {bmi}", font=("Arial","15", "bold"), fill="green")
        a = (bmi*500)/40+7.5
        canvas.create_rectangle(a, 90, a+5, 210, fill="black")
    if 25 < bmi < 30:
        canvas.create_text(250, 230, text="mierna nadváha", font=("Arial","15", "bold"), fill="orange")
        canvas.create_text(250, 250, text=f"BMI = {bmi}", font=("Arial","15", "bold"), fill="orange")
        a = (bmi*500)/40+5
        canvas.create_rectangle(a, 90, a+5, 210, fill="black")
    if 30 <= bmi < 40:
        canvas.create_text(250, 230, text="obezita", font=("Arial","15", "bold"), fill="red")
        canvas.create_text(250, 250, text=f"BMI = {bmi}", font=("Arial","15", "bold"), fill="red")
        a = (bmi*500)/40+10
        canvas.create_rectangle(a, 90, a+5, 210, fill="black")
    if bmi >= 40:
        canvas.create_text(250, 230, text="ťažká obezita", font=("Arial","15", "bold"), fill="red")
        canvas.create_text(250, 250, text=f"BMI = {bmi}", font=("Arial","15", "bold"), fill="red")
canvas.create_text(250, 50, text=f"výška {round(vyska)} cm, váha {vaha} kg", font=("Arial","15"))
vypocitaj_bmi()
canvas.mainloop()
