from http.server import BaseHTTPRequestHandler, HTTPServer
import random

QUOTES = [
    "To Iqra: You make my world infinitely brighter every single day.",
    "To Iqra: In a world full of variables, you are my absolute constant.",
    "To Iqra: Every single line of code I write is driven by the future we are building together.",
    "To Iqra: Loving you is as natural as an infinite loop, it never ends."
]

class LoveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        selected_quote = random.choice(QUOTES)
        
        # A beautiful clean styling layout for the web page
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>For Iqra</title>
            <style>
                body {{ background: #fff5f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; max-width: 500px; border: 1px solid #ffe3e3; }}
                h1 {{ color: #ff4d6d; margin-bottom: 20px; font-size: 2.5em; }}
                p {{ color: #4a4a4a; font-size: 1.3em; line-height: 1.6; font-style: italic; }}
                .heart {{ color: #ff4d6d; font-size: 3em; animation: beat .3s infinite alternate; }}
                @keyframes beat {{ to {{ transform: scale(1.1); }} }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="heart">❤️</div>
                <h1>For Iqra</h1>
                <p>"{selected_quote}"</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), LoveHandler)
    print("Love server started on port 8080...")
    server.serve_forever()
