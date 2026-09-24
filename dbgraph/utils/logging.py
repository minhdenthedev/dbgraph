import logging

log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("dbgraph.log")
console_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)
