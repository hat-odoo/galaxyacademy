from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json, psycopg2,time
from BaseHTTPServer import HTTPServer

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if len(self.path) < 25:
            parsed_path = urlparse.urlparse(self.path)
            
            static_file = open('index.html','rb')
            message = static_file.read()
            static_file.close()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(message) 
        elif(self.path > 25):
            check = False

            dataseq = self.path.split("?")[1]
            data = dataseq.split("&")
            dataOutput(data)
            self.messageFunc(data)
        
        return


    def messageFunc(self,data):
        message = "<html>Thank you "+ data[0].split("=")[1] +", for Submitting contact form </html>"
        #message = messageFunc(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        # self.wfile.close()
        time.sleep(5)
        self.path = "/"
        return self.do_GET()

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
       
        data = post_body.split("&")
        dataOutput(data)
        self.messageFunc(data)
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(data['foo'])
        return


def dataOutput(list_response):
    out = []
    for i in list_response:
        out.append(i.split("=")[1])
    
    conn = psycopg2.connect(database = "testweek2", user = "postgres", password = "123456", host = "127.0.0.1", port = "5432")
    print "Opened database successfully"

    cur = conn.cursor()
    print out
    cur.execute("INSERT INTO sample2 (firstname, lastname, email, phone) VALUES (%s,%s,%s,%s)",(out[0],out[1],out[2],int(out[3])));
   
    conn.commit()
    conn.close()
    return   

if __name__ == '__main__':
    
    try:
        server = HTTPServer(('localhost', 8080), GetHandler)
        print 'Starting server at http://localhost:8080'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.shutdown()
        #server.socket.close()

