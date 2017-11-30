import subprocess
from flask import Flask, render_template

app = Flask(__name__);

proc = None

@app.route("/")
def hello():
    return render_template("index.html");

@app.route("/start", methods=['GET', 'POST'])
def start():
    global proc
    print("> Starting up");
    proc = subprocess.Popen(["python", "tagDetection.py"]);
    return "Started!";

@app.route("/stop", methods=['GET', 'POST'])
def stop():
    global proc
    proc.kill();
    return "Stopped!";

@app.route("/status", methods=['GET','POST'])
def status():
    global proc
    if proc is None:
        print("> Camera is stopped")
        return "Resting!"

    if proc.poll() is None:
        return "Running!"

    else:
        print("> Camera is stopped");
        return "Stopped!";

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 4040, debug=False)

