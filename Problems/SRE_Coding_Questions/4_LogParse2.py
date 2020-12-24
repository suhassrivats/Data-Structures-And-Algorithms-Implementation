"""
Extract the program name from the field between the hostname and the log
message and output those values in columns.

Sample Output (when run against the lines containing "Jan 20 05:2" in the log
`2_var_log_messages.txt` file):

---------- begin sample output ----------
minute,total_count,rsyslogd,cs3,ACCT_ADD
Jan 20 05:20,1,1,0,0
Jan 20 05:22,6,0,5,1
---------- end sample output ----------
====== End # QUESTION:  =====

Logic:
We will try to store the output in a dictionary data structure in this format.
Here is an example:
output = {
    'Jan 20 05:20': {
        'total_count': 1,
        'rsyslog': 2,
        'cs3': 3,}
    },
    'Jan 20 05:22': {
        'total_count': 3,
        'rsyslog': 1,
        'cs3': 0,}
    },
}
"""

import re
from collections import defaultdict


def parse_log():  # Using Regex
    output = {}
    all_progs = set()
    pattern = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ ([\w-]+).*$')
    with open('logs/messages.txt', 'r') as file:
        lines = file.readlines()
    if len(lines) > 0:
        for line in lines:
            match = pattern.match(line)
            if match:
                if match.group(1) and match.group(2):
                    minute, program_name = match.group(1), match.group(2)
                    if minute not in output:
                        output[minute] = defaultdict(int)
                        output[minute]['total_count'] = 1
                    else:
                        output[minute]['total_count'] += 1
                    output[minute][program_name] = output[minute][program_name] + 1  # defaults to 0
        # Add all program names to a set
        for x in output.values():
            for y in x.keys():
                all_progs.add(y)
        # Print in desired format
        header = 'minute,' + ','.join([x for x in all_progs])
        print(header)
        for minute in output.keys():
            op = minute + ","
            for i, prog in enumerate(all_progs):
                op += str(output[minute][prog])
                if i < len(all_progs)-1:
                    op += ","
            print(op)
    else:
        print('Log file is empty')


parse_log()
