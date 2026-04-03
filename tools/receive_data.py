"""Tiny HTTP server to receive JSON data from the browser."""
import http.server
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_FILE = os.path.join(BASE_DIR, "tools", "kjv_apocrypha_data.json")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        with open(OUT_FILE, 'wb') as f:
            f.write(body)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b'OK')
        print(f"Received {length} bytes, saved to {OUT_FILE}")
        # Shutdown after receiving
        import threading
        threading.Thread(target=self.server.shutdown).start()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        pass

print("Listening on http://localhost:9876 ...")
server = http.server.HTTPServer(('127.0.0.1', 9876), Handler)
server.serve_forever()
print("Done.")
