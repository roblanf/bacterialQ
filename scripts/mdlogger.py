import logging
import os

# Define custom log levels
COMMAND_LOG_LEVEL = 15
RESULT_LOG_LEVEL = 20
PROCESS_LOG_LEVEL = 30
ERROR_LOG_LEVEL = 40

# Add custom log levels to the logging module
logging.addLevelName(COMMAND_LOG_LEVEL, "COMMAND")
logging.addLevelName(RESULT_LOG_LEVEL, "RESULT")
logging.addLevelName(PROCESS_LOG_LEVEL, "PROCESS")
logging.addLevelName(ERROR_LOG_LEVEL, "ERROR")

# Disable logging for matplotlib font manager to reduce log noise
logging.getLogger('matplotlib.font_manager').disabled = True

# Dictionary to map log level names to their corresponding log level values
LOG_LEVEL = {
    'command': COMMAND_LOG_LEVEL,
    'result': RESULT_LOG_LEVEL,
    'process': PROCESS_LOG_LEVEL,
    'error': ERROR_LOG_LEVEL
}

# Custom formatter to handle custom log levels
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Map custom log levels to their names
        if record.levelno == COMMAND_LOG_LEVEL:
            record.levelname = 'COMMAND'
        elif record.levelno == RESULT_LOG_LEVEL:
            record.levelname = 'RESULT'
        elif record.levelno == PROCESS_LOG_LEVEL:
            record.levelname = 'PROCESS'
        elif record.levelno == ERROR_LOG_LEVEL:
            record.levelname = 'ERROR'
        # Use the parent class's format method to format the record
        return super().format(record)

# Function to set up logging
def setup_logging(output_dir, verbose):
    """
    Set up logging to file and console.

    Args:
        output_dir (Path): Directory to save the log file.
        verbose (bool): If True, set file log level to COMMAND_LOG_LEVEL, else PROCESS_LOG_LEVEL.
    """
    log_file = output_dir / "log.md"  # Define the log file path
    console_level = PROCESS_LOG_LEVEL  # Set console log level
    file_level = COMMAND_LOG_LEVEL if verbose else PROCESS_LOG_LEVEL  # Set file log level based on verbosity

    # Configure the logging module
    logging.basicConfig(
        level=min(console_level, file_level),  # Set the minimum log level
        format='%(message)s',  # Set the log message format
        handlers=[
            logging.FileHandler(log_file),  # Log to file
            logging.StreamHandler()  # Log to console
        ]
    )

    # Set log levels for handlers
    logging.getLogger().handlers[0].setLevel(file_level)
    logging.getLogger().handlers[1].setLevel(console_level)

    # Set custom formatter for all handlers
    formatter = CustomFormatter()
    for handler in logging.getLogger().handlers:
        handler.setFormatter(formatter)

# Function to log a message
def log_message(level, msg, new_line=False):
    """
    Log a message at a specified log level.

    Args:
        level (str): Log level name (command, result, process, error).
        msg (str): Message to log.
        new_line (bool): If True, add a new line before the message.
    """
    if level in LOG_LEVEL:
        if new_line:
            logging.log(LOG_LEVEL[level], "")  # Log a new line if specified
        if not (msg.endswith("|") or msg.endswith("  ")):
            msg = msg + "  "  # Ensure message ends with two spaces for Markdown
        logging.log(LOG_LEVEL[level], msg)  # Log the message
    else:
        raise ValueError(f"Invalid log level: {level}")  # Raise error for invalid log level

# Function to log a link
def log_link(level, link_text, file_path):
    """
    Log a link to a file/figure.

    Args:
        level (str): Log level name (command, result, process, error).
        link_text (str): Text for the link.
        file_path (str): Path to the file.
    """
    log_file = logging.getLogger().handlers[0].baseFilename  # Get the log file path
    relative_path = os.path.relpath(file_path, os.path.dirname(log_file))  # Get relative path to the file
    if file_path.lower().endswith(('.png', '.jpeg', '.jpg')):
        log_message(level, f"![{link_text}]({relative_path})")  # Log image link for image files
    else:
        log_message(level, f"[{link_text}]({relative_path})")  # Log regular link for other files

# Function to log a command
def log_command(cmd):
    """
    Log a command in code block.
    """
    logging.log(COMMAND_LOG_LEVEL, f"```bash\n{cmd}\n```\n")
