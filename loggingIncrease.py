import logging

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    """Fungsi ini mencatat event ke dalam file log dengan format yang telah ditentukan.
    
    Args:
        event (str): Pesan yang akan dicatat ke dalam log.
    """
    logging.info(event)
