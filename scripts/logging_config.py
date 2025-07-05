import logging
import colorlog


def setup_logging():
    log = colorlog.getLogger()  # Rename the logger variable to avoid conflict

    # Check if the logger already has handlers
    if not log.hasHandlers():
        handler = colorlog.StreamHandler()
        handler.setFormatter(
            colorlog.ColoredFormatter(
                "%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                log_colors={
                    "DEBUG": "bold_blue",
                    "INFO": "bold_green",
                    "WARNING": "bold_yellow",
                    "ERROR": "bold_red",
                    "CRITICAL": "bold_purple",
                },
                secondary_log_colors={},
                style="%",
            )
        )

        log.addHandler(handler)
        log.setLevel(logging.DEBUG)  # Set log level to DEBUG

        # Example usage


if __name__ == "__main__":
    setup_logging()
    logger = colorlog.getLogger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
