from flask import Flask ,render_template
from math import sin , cos , radians

app = Flask(__name__)

@app.route("/")
def home ():
    buttons = []
    center_x = 600
    center_y = 350
    rotate = 0
    circles = [
        (3, 140),
        (7, 340),
        (10, 540),
        (15, 750),
        (20, 1000)]
    for conut,radius in circles:
        rotate =+ 60
        for i in range(conut):
            angle = radians((i*360 / conut )+ rotate)
            x = center_x + radius *cos(angle)
            y = center_y + radius *sin(angle)
            buttons.append({"x":x , "y":y})
        


    return render_template('index.html' ,buttons=buttons)


if __name__ == "__main__":
    app.run(debug=True)