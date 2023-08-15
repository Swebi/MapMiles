import tkinter as tk
import customtkinter

import tkintermapview
from PIL import Image


from geopy.distance import geodesic
from geopy.geocoders import Nominatim


def search():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()

    g = Nominatim(user_agent="MyApp")
    fromcord = (g.geocode(fromvar.get()).latitude, g.geocode(fromvar.get()).longitude)
    tocord = (g.geocode(tovar.get()).latitude, g.geocode(tovar.get()).longitude)


    marker_1 = map_widget.set_marker(fromcord[0],fromcord[1], text=str(fromvar.get()))
    marker_2 = map_widget.set_marker(tocord[0],tocord[1], text=str(tovar.get()))

    distance = round(geodesic(fromcord, tocord).km)


    map_widget.set_path([marker_1.position, marker_2.position])
    map_widget.set_position(tocord[0],tocord[1])

    if 0<distance<200:
        map_widget.set_zoom(10)
    elif 200 < distance < 400:
        map_widget.set_zoom(9)
    elif 400<distance<1000:
        map_widget.set_zoom(8)
    elif 1000<distance<4000:
        map_widget.set_zoom(6)
    elif 4000<distance<8000:
        map_widget.set_zoom(4)
    else:
        map_widget.set_zoom(2)



    Value_lbl.configure(text=str(distance)+' KM')



def from_click(coords):
    length=len(fromvar.get())
    From_ent.delete(0,length)
    From_ent.insert(0, coords)

def to_click(coords):
    length=len(tovar.get())
    To_ent.delete(0,length)
    To_ent.insert(0, coords)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("Distance Finder")
app.configure(fg_color="#1c2224")


bg = customtkinter.CTkImage(dark_image=Image.open("back.jpg"),size=(1920,1080))
bglabel = customtkinter.CTkLabel(master=app,text = "",image=bg)
bglabel.place(relx=0,rely=0)

fromvar = tk.StringVar()
tovar = tk.StringVar()


data_frame = customtkinter.CTkFrame(master=app, width=1000, height=700,fg_color="#1c2224",border_width=10,border_color="black") #,border_width=2,border_color="black"
data_frame.pack(padx=20,pady=50)
data_frame.pack_propagate(False)

map_widget = tkintermapview.TkinterMapView(data_frame, width=900, height=500, corner_radius= 20)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                    max_zoom=22)  # google normal


map_widget.set_address("India")
map_widget.set_zoom(3)

map_widget.pack(padx=50,pady=50)

map_widget.add_right_click_menu_command(label="From",
                                        command=from_click,
                                        pass_coords=True)

map_widget.add_right_click_menu_command(label="To",
                                        command=to_click,
                                        pass_coords=True)



Searchbutton = customtkinter.CTkButton(master=data_frame, text="Search", text_color="black", width=250, height=60,
                                    border_width=0, corner_radius=12,
                                    fg_color="#8bbad0", hover_color="#3d525c", font=("Comfortaa", 30, "bold"),
                                    command=search)  # add_function

Searchbutton.pack(padx=0, pady=0)


detail_frame = customtkinter.CTkFrame(master=app, width=1000, height=200,fg_color="#1c2224",border_width=10,border_color="black") #,border_width=2,border_color="black"
detail_frame.pack(padx=20,pady=0)
detail_frame.pack_propagate(False)

From_lbl = customtkinter.CTkLabel(master=detail_frame, text="From", fg_color='transparent',font=("Impact",30 ))
From_lbl.place(x=50,y=40)

From_ent = customtkinter.CTkEntry(master=detail_frame, font=("Comfortaa", 25),width=300, height=40,
                                  border_width=2, corner_radius=10,textvariable = fromvar)
From_ent.place(x=125,y=40)

To_lbl = customtkinter.CTkLabel(master=detail_frame, text="To", fg_color='transparent',font=("Impact",30 ),)
To_lbl.place(x=450,y=40)

To_ent = customtkinter.CTkEntry(master=detail_frame, font=("Comfortaa", 25),width=300, height=40, border_width=2, corner_radius=10,
                                textvariable = tovar)
To_ent.place(x=505,y=40)

Distance_lbl = customtkinter.CTkLabel(master=detail_frame, text="Distance", fg_color='transparent',font=("Impact",40 ))
Distance_lbl.place(x=50,y=110)

Value_lbl = customtkinter.CTkLabel(master=detail_frame, text="", fg_color='transparent',font=("Impact",40 ))
Value_lbl.place(x=250,y=110)


app.mainloop()

