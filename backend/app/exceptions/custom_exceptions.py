class SessionNotFoundError(Exception):
    """Raised when the requested session does not exist."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        super().__init__(f"Session '{session_id}' not found.")


class UnsupportedFileTypeError(Exception):
    """Raised when an unsupported file is uploaded."""

    def __init__(self, extension: str):
        self.extension = extension
        super().__init__(f"Unsupported file type: {extension}")


class EmptyFileError(Exception):
    """Raised when an empty file is uploaded."""

    def __init__(self):
        super().__init__("Uploaded file is empty.")