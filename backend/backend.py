from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys
import subprocess
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        month = post_data['month']
        day = post_data['day']
        inquiry = post_data['inquiry']

        print(f"Received data: month={month}, day={day}, inquiry={inquiry}", file=sys.stderr)
        mkey_path = os.path.join("/mkey", "mkey.py")
        result = subprocess.run(["python", mkey_path, "-m", str(month), "-d", str(day), inquiry], capture_output=True, text=True, cwd='/mkey')
        print(f"mkey.py output: {result.stdout}", file=sys.stderr)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(result.stdout.encode())

server = HTTPServer(('', 5000), Handler)
server.serve_forever()
