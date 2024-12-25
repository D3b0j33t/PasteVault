def format_output(message, style="info"):
    """
    Formats output messages for the CLI.
    """
    styles = {
        "info": "\033[94m",   # Blue
        "success": "\033[92m", # Green
        "error": "\033[91m",  # Red
        "end": "\033[0m",     # Reset
    }
    return f"{styles.get(style, '')}{message}{styles['end']}"
