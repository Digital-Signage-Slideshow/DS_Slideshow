from os import path


def get_file_extension(f_path: str) -> str:
    """
    Get the file extension.

    Args:
        f_path: str: path to the file

    Returns:
        str: file extension
    """
    from os import path
    return path.splitext(f_path)[1][1:]


def get_file_name(f_path: str) -> str:
    """
    Get the file name.

    Args:
        f_path: str: path to the file

    Returns:
        str: file name
    """
    return path.basename(f_path)


def allowed_file_extensions(f_name: str) -> bool:
    """
    Check if the file extension is allowed.

    Args:
        f_name: str: name of the file

    Returns:
        bool: True if the file is allowed, False otherwise
    """
    from flask import current_app
    return '.' in f_name and f_name.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def delete_file(f_path: str, f_name: str):
    """
    Delete a file if it exists.

    Args:
        f_path: str: path to the file
        f_name: str: name of the file

    Returns:
        None

    Raises:
        FileNotFoundError: if the file doesn't exist
    """
    try:
        from os import path, remove
        remove(path.join(f_path, f_name))
    except FileNotFoundError as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)


def create_directory(f_path: str, f_name: str, f_mode: int = 0o777):
    """
    Create a directory if it doesn't exist.

    Args:
        f_path: str: path to the directory
        f_name: str: name of the directory
        f_mode: int: permissions to set on the directory

    Returns:
        None

    Raises:
        FileExistsError: if the directory already exists
    """
    try:
        from os import path, mkdir
        mkdir(path.join(f_path, f_name), f_mode)
    except FileExistsError as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)


def create_file(f_path: str, f_name: str):
    """
    Create a file if it doesn't exist.

    Args:
        f_path: str: path to the file
        f_name: str: name of the file

    Returns:
        None

    Raises:
        FileExistsError: if the file already exists
    """
    try:
        from os import path, mknod
        mknod(path.join(f_path, f_name))
    except FileExistsError as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
