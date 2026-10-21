import http.server
import socketserver
import os

PORT = 8082
DIRECTORY = r"D:\PHOENIX\Quản ly Thiet Bi"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Server Thiet Bi CNTT running at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
