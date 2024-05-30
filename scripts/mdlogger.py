import logging
import os

# Define custom log levels
COMMAND_LOG_LEVEL = 15
RESULT_LOG_LEVEL = 20
PROCESS_LOG_LEVEL = 30
ERROR_LOG_LEVEL = 40

logging.addLevelName(COMMAND_LOG_LEVEL, "COMMAND")
logging.addLevelName(RESULT_LOG_LEVEL, "RESULT")
logging.addLevelName(PROCESS_LOG_LEVEL, "PROCESS")
logging.addLevelName(ERROR_LOG_LEVEL, "ERROR")

logging.getLogger('matplotlib.font_manager').disabled = True

LOG_LEVEL = {
    'command': COMMAND_LOG_LEVEL,
    'result': RESULT_LOG_LEVEL,
    'process': PROCESS_LOG_LEVEL,
    'error': ERROR_LOG_LEVEL
}

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == COMMAND_LOG_LEVEL:
            record.levelname = 'COMMAND'
        elif record.levelno == RESULT_LOG_LEVEL:
            record.levelname = 'RESULT'
        elif record.levelno == PROCESS_LOG_LEVEL:
            record.levelname = 'PROCESS'
        elif record.levelno == ERROR_LOG_LEVEL:
            record.levelname = 'ERROR'
        return super().format(record)

def setup_logging(output_dir, verbose):
    log_file = output_dir / "log.md"
    console_level = PROCESS_LOG_LEVEL
    file_level = COMMAND_LOG_LEVEL if verbose else PROCESS_LOG_LEVEL

    logging.basicConfig(
        level=min(console_level, file_level),
        format='%(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.getLogger().handlers[0].setLevel(file_level)
    logging.getLogger().handlers[1].setLevel(console_level)

    formatter = CustomFormatter()
    for handler in logging.getLogger().handlers:
        handler.setFormatter(formatter)

def log_message(level, msg, new_line=False):
    if level in LOG_LEVEL:
        if new_line:
            logging.log(LOG_LEVEL[level], "")
        if not (msg.endswith("|") or msg.endswith("  ")):
            msg = msg + "  "
        logging.log(LOG_LEVEL[level], msg)
    else:
        raise ValueError(f"Invalid log level: {level}")

def log_link(level, link_text, file_path):
    log_file = logging.getLogger().handlers[0].baseFilename
    relative_path = os.path.relpath(file_path, os.path.dirname(log_file))
    if file_path.lower().endswith(('.png', '.jpeg', '.jpg')):
        log_message(level, f"![{link_text}]({relative_path})")
    else:
        log_message(level, f"[{link_text}]({relative_path})")

def log_command(cmd):
    logging.log(COMMAND_LOG_LEVEL, f"```bash\n{cmd}\n```\n")