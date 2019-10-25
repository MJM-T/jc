"""jc - JSON CLI output utility history Parser

Usage:
    specify --history as the first argument if the piped input is coming from history

Example:

$ history | jc --history -p
{
  "n118": "sleep 100",
  "n119": "ls /bin",
  "n120": "echo \"hello\"",
  "n121": "docker images",
  ...
}
"""


def parse(data):
    output = {}

    linedata = data.splitlines()

    # Clear any blank lines
    cleandata = list(filter(None, linedata))

    if cleandata:
        for entry in cleandata:
            try:
                parsed_line = entry.split(maxsplit=1)
                # prepend a alpha character n to be more json compliant
                output['n' + parsed_line[0]] = parsed_line[1]
            except IndexError:
                # need to catch indexerror in case there is weird input from prior commands
                pass

    return output
