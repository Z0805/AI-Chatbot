from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


class ChatHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/chat":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))

        user_message = data.get("message", "")

        ollama_data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "stream": False
        }

        request = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(ollama_data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read())

            answer = result["message"]["content"]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(
                json.dumps({"answer": answer}).encode("utf-8")
            )

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps({"error": str(e)}).encode("utf-8")
            )


server = ThreadingHTTPServer(("localhost", 8000), ChatHandler)

print("AI Chatbot running at http://localhost:8000")

server.serve_forever()