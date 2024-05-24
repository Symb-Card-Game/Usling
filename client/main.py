import socket
import logging


HOST = "127.0.0.1"
PORT = 35677

logger = logging.getLogger(__name__)


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, World!")
        data = s.recv(1024)
    logger.info(f"Client got back: {data}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_client()
