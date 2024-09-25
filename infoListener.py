import socket
import json

def start_listening(host='0.0.0.0', port=369):
    """Starts listening for incoming connections."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    
    print(f"Server listening on {host}:{port}")
    
    while True:
        conn, addr = sock.accept()
        print(f"Connected by {addr}")
        
        try:
            data = conn.recv(1024).decode('utf-8')
            if data:
                parsed_data = json.loads(data)
                process_json_data(parsed_data)
        finally:
            conn.close()

def process_json_data(data):
    """Processes and prints the received JSON data."""
    for key, value in data.items():
        print(f"{key}: {value}")
    
    # Example of how you might store or process the data
    store_system_info(data)

def store_system_info(info):
    """Stores the system information in a file."""
    with open('system_info.txt', 'w') as f:
        json.dump(info, f, indent=2)

if __name__ == "__main__":
    start_listening()
