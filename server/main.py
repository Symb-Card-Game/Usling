import socket
import logging

HOST = "127.0.0.1"
PORT = 35677

logger = logging.getLogger(__name__)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()
        with conn:
            logger.info("connected")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_server()
