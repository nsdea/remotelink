'''Runs a runner which can be controlled'''

import os
import time
import subprocess

def execute(script: str=open('run.bat').read(), log='log.txt'):
    '''Executes a batch script and returns output'''

    output = ''
    

    for line in script.split('\n'):
        line_output = subprocess.check_output(line, shell=True).decode('utf-8').strip()
        if log:
            open(log, 'w').write(f'{line_output}')
        output += line_output + '\n'
    return output

def run(run_file: str='run.bat', log='log.txt'):
    '''Whenever <run_file> changes, it is being ran.'''

    run_count = 0

    while True:
        old = open(run_file).read()

        if open(run_file).read() != old:
            execute(script=open(run_file).read(), log=log)
            print(open('log.txt').read())
        
            run_count += 1

if __name__ == '__main__':
    run()