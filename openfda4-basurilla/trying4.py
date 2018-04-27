import http.server
import socketserver
import json


# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8002


# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        def file_send(file_name):
            with open (file_name, "r") as f:
                message = f.read()
            self.wfile.write(bytes(message, "utf8"))

        #conn = http.client.HTTPSConnection("api.fda.gov")
        #conn.request("GET", "/drug/label.json?search=generic_name:%s&limit=%s", None, headers)
        #r1 = conn.getresponse()
        #print(r1.status, r1.reason)
        #repos_raw = r1.read().decode("utf-8")
        #conn.close()

        #repos = json.loads(repos_raw)




        # Send message back to client
        message = "Hello world! " + self.path
        # Write content as utf-8 data
        hola = self.wfile.write(bytes(message, "utf8"))
        path = self.path

        headers = {'User-Agent': 'http-client'}



        if path == "/":
            filename = "index.html"
        else:
            if path == "/new":
                filename = "new.html"
            else:
                filename = "error.html"
        with open(filename, "r") as f:
            content = f.read()

        header = "Content-Type: text/html\n"
        header += "Content-Length: {}\n".format(len(str.encode(content)))

        response_msg = str.encode(status_line + header + "\n" + content)
        clientsocket.send(response_msg)

        print("File served!")
        return


# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")

# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py