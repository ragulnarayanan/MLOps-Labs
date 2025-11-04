import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,                      
    format="%(asctime)s - %(levelname)s - %(message)s",  
    datefmt="%Y-%m-%d %H:%M:%S",              
    filename="app.log",                       
    filemode="w"                              
)

# Log messages
logging.debug("This is a debug message — useful for development.")
logging.info("This is an info message — for general updates.")
logging.warning("This is a warning — something might be wrong.")
logging.error("This is an error message — something went wrong.")
logging.critical("This is critical — the program may not recover.")


# Exception Handling
try:
    x = 10 / 0
except Exception:
    logging.exception("An error occurred!")