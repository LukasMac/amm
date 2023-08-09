import subprocess
from . import ansi
from . import history

def load(filePath):
    lines = []
    try:
        with open(filePath, 'r') as f:
            lines = [Command.deserialize(l.strip('\n').strip('\r')) for l in f.readlines() if l]
    except:
        pass
    return lines

def load_history():
    lines = [Command.deserialize(l.strip('\n').strip('\r'), True) for l in history.get_history() if l]

    return [x for x in lines if x is not None]

def save(commands, filePath):
    with open(filePath, 'w') as f:
        f.write('\n'.join([m.serialize() for m in commands]))

def add(commands, command):
    remove(commands, command)
    commands.append(command)

def remove(commands, command):
    try:
        match = next(m for m in commands if command.equals(m))
        commands.remove(match)
    except StopIteration:
        pass

class Command(object):
    '''A Command is composed of the shell command string and an optional alias'''
    def __init__(self, cmd, alias = "", is_from_history = False):
        if not cmd:
            raise "empty command argument"
        self.cmd = cmd
        self.alias = alias
        self.is_from_history = is_from_history

    def __repr__(self):
        res = self.cmd

        if self.alias and self.alias != self.cmd:
            res = res+" "+ansi.grey_text(self.alias)
        if self.is_from_history:
            res = "\U0001F551"+" "+res
        return res

    @staticmethod
    def deserialize(str, is_from_history = False):
        if not str:
            return None

        if "##" in str:
            cmd, alias = str.split("##")
        else:
            cmd = str
            alias = ""
        return Command(cmd, alias, is_from_history)

    def serialize(self):
        if self.alias:
            return self.cmd + "##" + self.alias
        else:
            return self.cmd

    def equals(self, mark):
        return self.cmd == mark.cmd and self.alias == mark.alias

