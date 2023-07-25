# Amm

Based off of [marker](https://github.com/pindexis/marker)

![amm](https://cloud.githubusercontent.com/assets/2557967/14209204/d99db934-f81a-11e5-910c-9d34ac155d18.gif)

"Amm" is a command palette for the terminal. the name is based on the sound usually made when trying to recall some memory or terminal command you keep forgeting :) It lets you bookmark commands (or commands templates) and easily retreive them with the help of a real-time fuzzy matcher.

## Features:
- A UI selector that lets you easily select the desired command if more than one command is matched.
- Fuzzy matching (through commands and their descriptions).
- Command template: You can bookmark commands with place-holders and place the cursor at those place-holders using a keyboard shortcut.
- Portability across supported shells: you can use bookmarked commands in both Bash and Zshell.

## Usage
- `Ctrl-space`: search for commands that match the current written string in the command-line.
- `Ctrl-k` (or `amm mark`): Bookmark a command.
- `Ctrl-t`: place the cursor at the next placeholder, identified by '{{anything}}'
- `amm remove`: remove a bookmark

You can customize key binding using environment variables, respectively with ```AMM_KEY_GET```, ```AMM_KEY_MARK``` and ```AMM_KEY_NEXT_PLACEHOLDER```.

## Requirements
- python (2.7+ or 3.0+)
- Bash-4.3+ or Zshell.
- Linux Or OSX

##### Note:
In OSX, it seems like Bash 3.x is the default shell which is not supported. you have to [update your Bash to 4.3+](http://apple.stackexchange.com/a/24635) or [change your shell to zshell](http://stackoverflow.com/a/1822126/1117720) in order to use Amm.

## Installation

`git clone --depth=1 https://github.com/LukasMac/amm.sh ~/.amm && ~/.amm/install.py`

## License
[MIT](LICENSE)
