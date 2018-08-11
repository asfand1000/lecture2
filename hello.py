from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    i = 28;
    print(f"i is {i}")

    f = 2.8
    print(f"i is {f}")

    b = True
    print(f"i is {b}")

    s = None
    print(f"i is {s}")

    x = 28

    coordinates = (10.0, 20.0)

    names = ["asfand", "ahamd", "bob"]
    print(names[1])
