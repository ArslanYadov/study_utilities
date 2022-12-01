import logging
import pdfkit
import os
import sys


def make_path() -> str:
    """
    Make path to folder,
    where can be saved file.
    """
    path_to_folder: str = os.path.expanduser(r'~/convertResult')
    return path_to_folder


def make_dir_if_not_exist(path_to_folder: str) -> str:
    """Make dir for file, if it's doesn't exist."""
    if not os.path.isdir(path_to_folder):
        os.mkdir(path_to_folder)
        return 'Make directory [ {} ] is done.'.format(path_to_folder)
    return 'Directory [ {} ] is already exist.'.format(path_to_folder)


def get_url() -> str:
    """Get url from user input."""
    input_url: str = input('Please enter URL address: ')
    while True:
        sys.stdout.write('You entered next url: {}\n'.format(input_url))
        ans: str = input('This is right url? [y/N]: ')
        if ans.lower() in ['y', 'yes']:
            logging.info(msg='Entered url: {}'.format(input_url))
            break
        input_url = input('Please enter URL address: ')
    return input_url


def get_filename(path_to_folder: str) -> str:
    """
    Get file name from user input.
    Return path to file.
    """
    filename: str = input('Please enter file name: ')
    while True:
        sys.stdout.write('You entered next file name: {}\n'.format(filename))
        ans: str = input('This is right file name? [y/N]: ')
        if ans.lower() in ['y', 'yes']:
            logging.info(msg='Entered file name: {}.pdf'.format(filename))
            break
        filename = input('Please enter URL address: ')
    filename += '.pdf'
    filename = get_path_to_file(path_to_folder, filename)
    return filename


def get_path_to_file(path_to_folder:str, filename: str) -> str:
    """Get path to file."""
    return os.path.join(path_to_folder, filename)


def main() -> None:
    path_to_folder: str = make_path()
    log_msg: str = make_dir_if_not_exist(path_to_folder)
    logging.debug(msg=log_msg)
    url: str = get_url()
    filename: str = get_filename(path_to_folder)
    pdfkit.from_url(url=url, output_path=filename)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] : [%(levelname)s] : %(message)s',
        handlers=[logging.FileHandler('c2p_logs.log')]
    )
    main()
