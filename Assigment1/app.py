from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]
            if op == "add":
                result = num1 + num2
            elif op == "sub":
                result = num1 - num2
            elif op == "mul":
                result = num1 * num2
            elif op == "div":
                result = "Error: Division by 0" if num2 == 0 else num1 / num2
        except:
            result = "Invalid Input"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    print("✅ Flask app is starting...")
    print("🌐 Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)
