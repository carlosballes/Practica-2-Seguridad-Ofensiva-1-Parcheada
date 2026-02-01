from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = "Guest"
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSTI Lab</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
            input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; }
            button { background-color: #28a745; color: white; border: none; padding: 10px; width: 100%; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, {{ name }}!</h1>
            <p>Enter your name to personalize this page.</p>
            <form method="post">
                <input type="text" name="name" placeholder="Your Name">
                <button type="submit">Say Hello</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
