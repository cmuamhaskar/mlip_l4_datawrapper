from http.server import HTTPServer, BaseHTTPRequestHandler
import csv

class CSVRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data.csv':
            # Replace the file path with the path to your own CSV file
            with open('csv_path', 'r') as csv_file:
                csv_string = csv_file.read()
                # Set the response headers
                self.send_response(200)
                self.send_header('Content-type', 'text/csv')
                self.send_header('Content-Disposition', 'attachment; filename="data.csv"')
                self.end_headers()
                # Write the CSV content to the response body
                self.wfile.write(csv_string.encode())
        else:
            # Serve the default index.html page or any other files
            super().do_GET()

if __name__ == '__main__':
    # Start the HTTP server on localhost and port 8000
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CSVRequestHandler)
    print('Server listening on port 8000...')
    httpd.serve_forever()

