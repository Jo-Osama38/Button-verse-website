from flask import Flask ,render_template , redirect , url_for
from math import sin , cos , radians

app = Flask(__name__)
buttons = []

@app.route("/")
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

    return render_template('index.html' ,buttons=buttons )


@app.route("/mode/<int:num>")
def change_mode(num):
    return render_template('index.html',buttons = buttons , num=num)



    

if __name__ == "__main__":
    app.run(debug=True)