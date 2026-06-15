from flask import Flask ,render_template , redirect , url_for
from math import sin , cos , radians

app = Flask(__name__)
buttons = []
effects={
    1:"IDLE CORE",
    2:"HEARTBEAT",
    3:"TIDAL WAVE",
    4:"ROLLING ORBIT",
    5:"SPECTRUM FLOW",
    6:"LIQUID MORPH",
    7:"NEON PULSE",
    8:"BLUR",
    9:"DARK WORLD",
    10:"MIRROR",
    11:"INVISIBLE",
    15:"NIGHT VISION",
    12:"BLACK & WHITE",
    13:"GLITCH",
    14:"LIGHT LINES ONLY :-)",
    16:"PORTAL WARR",


    32:"Under Development",
    33:"Under Development",
    34:"Under Development",
    35:"Under Development",
    36:"Under Development",
    37:"Under Development",
    38:"Under Development",
    40:"Under Development",
    41:"Under Development",
    42:"Under Development",
    43:"Under Development",
    44:"Under Development",
    45:"Under Development",
    46:"Under Development",
    47:"Under Development",
    48:"Under Development",
    49:"Under Development",
    50:"Under Development",
    51:"Under Development"
}

@app.route("/")
@app.route("/home")
def home ():
    global buttons
    buttons= []
    center_x = 600
    center_y = 350
    rotate = 0
    circles = [
        (5, 300),
        (10, 600),
        (15, 1000),
        (20, 1400)]
    for conut,radius in circles:
        rotate =+ 60
        for i in range(conut):
            angle = radians((i*360 / conut )+ rotate)
            x = center_x + radius *cos(angle)
            y = center_y + radius *sin(angle)
            buttons.append({"x":x , "y":y , "number": len(buttons) + 2 })

    return render_template('index.html' ,buttons=buttons,num=1,effects=effects )


@app.route("/mode/<int:num>")
def change_mode(num):
    return render_template('index.html',buttons = buttons , num=num , effects=effects)



    

if __name__ == "__main__":
    app.run(debug=True)