from os import environ

def get_history():
    lines = []

    history_file_path = _get_history_file_path()

    try:
        with open(history_file_path, 'r') as f:
            lines = f.readlines()
    except:
        pass
  
    return lines

def get_last_run_command():
    last_run_command = None
  
    history = get_history()
  
    if len(history) > 1:
      return history[-2]
  
    return None

def _get_history_file_path():
    history_file_path = None
    home_path = environ['HOME']
    shell = environ['SHELL']

    if shell == '/bin/zsh':
        return home_path + '/.zhistory'
    elif shell == '/bin/bash':
        return  home_path + '/.bash_history'

    return None