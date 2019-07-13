"""Code Simulation Tool

A tool to help programmers do their job :). Based
on the classic code simulation technique.
"""
import time
 

def main():
    """Runs the code simulation application"""
    while True:
        _write_simulation(_fetch_iterations())
        time.sleep(1)


def _fetch_iterations():
    with open('iterations.txt') as iter_input:
        return [line for line in iter_input.readlines()
                if not line.startswith('#')]


def _write_simulation(lines):
    variables = lines[0]
    with open('code_simulation.md', 'w') as codesim:
        _create_header(codesim, variables.split())
        for line in lines[1:]:
            _write_line(codesim, line.split())


def _create_header(stream, values):
    vals = list(zip(*[(var, "-" * len(var) + ":") for var in values]))
    _write_line(stream, vals[0])
    _write_line(stream, vals[1])


def _write_line(stream, values):
    stream.write(" | ".join(values) + "  \n")


if __name__ == '__main__':
    main()
