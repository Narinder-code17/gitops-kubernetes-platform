from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = "GitOps Kubernetes Platform"
APP_VERSION = "v1.1.0"
ENVIRONMENT = "Kubernetes"


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                text-align: center;
                padding-top: 80px;
            }}

            .container {{
                background: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                margin-bottom: 25px;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}

            .info {{
                margin: 12px 0;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>{APP_NAME}</h1>

            <div class="info">
                <strong>Version:</strong> {APP_VERSION}
            </div>

            <div class="info">
                <strong>Environment:</strong> {ENVIRONMENT}
            </div>

            <div class="info">
                <strong>Status:</strong>
                <span class="status">Healthy</span>
            </div>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)