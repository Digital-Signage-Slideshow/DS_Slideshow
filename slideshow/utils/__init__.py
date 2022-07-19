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
