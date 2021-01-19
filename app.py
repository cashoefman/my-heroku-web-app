from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    # Load current count
    f = open("counts.txt", "r")
    counts = int(f.read())
    f.close()

    # Increment the count
    counts += 1

    # Overwrite the count
    f = open("counts.txt", "w")
    f.write(str(counts))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", counts=counts)

if __name__ == "__main__":
    app.run()