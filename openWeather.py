import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Verdana", 18)


class openWeather(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="ic.ico")
        tk.Tk.wm_title(self, "Your Personal Weather Forecast")
        tk.Tk.geometry(self, "400x400")

        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = "True")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames= {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0 , sticky= "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        tk.Label(self, text = "Personal Weather Forecast", font= LARGE_FONT).grid( row = 1,columnspan= 4, pady = 50)
        # label.pack(pady = 10 , padx = 10)

        location_var = tk.StringVar()
        location_var.set("Warsaw")
        option_location = {"Warsaw", "London", "Lodz", "Jakarta"}
        tk.Label(self, text = "Location:").grid(row = 2, column = 1)
        tk.OptionMenu(self, location_var, *option_location).grid(row = 2, column = 3)


        ##variables
        variables_option = tk.StringVar()
        variables_option.set("Use variables from OpenWeatherMap")
        var_opt = {"Use variables from OpenWeatherMap","Use my variables"}
        tk.Label(self, text="Variables:").grid(row = 3, column = 1)
        tk.OptionMenu(self, variables_option, *var_opt).grid(row = 3, column = 3)

        variables_option.get()
        if (True):
            windSpeed = tk.StringVar(value="")
            tk.Label(self, text="Wind Speed:").grid(row= 4, column = 1)
            tk.Entry(self, textvariable= windSpeed, width = 10).grid(row = 4, column = 2)
            tk.Label(self, text="mps").grid(row=4, column=3)

            temperature = tk.StringVar(value="")
            tk.Label(self, text="Temperature:").grid(row=5, column=1)
            tk.Entry(self, textvariable=temperature, width=10).grid(row=5, column=2)
            tk.Label(self, text="C").grid(row=5, column=3)

            pressure = tk.StringVar(value="")
            tk.Label(self, text="Pressure:").grid(row=6, column=1)
            tk.Entry(self, textvariable=pressure, width=10).grid(row=6, column=2)
            tk.Label(self, text="hPa").grid(row=6, column=3)

            humidity = tk.StringVar(value="")
            tk.Label(self, text="Humidity:").grid(row=7, column=1)
            tk.Entry(self, textvariable=humidity, width=10).grid(row=7, column=2)
            tk.Label(self, text="%").grid(row=7, column=3)

            clouds = tk.StringVar(value="")
            tk.Label(self, text="Clouds").grid(row=8, column=1)
            tk.Entry(self, textvariable=clouds, width=10).grid(row=8, column=2)
            tk.Label(self, text="%").grid(row=8, column=3)

        ttk.Button(self, text= "Calculate",
                            command = lambda : controller.show_frame(PageOne)). grid(row = 10, column = 3)
        # button1.pack()#(side = tk.BOTTOM)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Personal Weather Forecast", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

app = openWeather()
app.mainloop()

