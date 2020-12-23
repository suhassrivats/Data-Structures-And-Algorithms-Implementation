"""
Write a script which parses /var/log/messages and generates a CSV with two
columns: minute, number_of_messages. Note: /var/log/messages: sample content in
`2_parse_messages_and_generate_csv` file

---------- begin sample log extract ----------
Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
Jan 20 03:25:08 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
Jan 20 03:26:21 fakehost anacron[28969]: Normal exit (1 job run)
Jan 20 03:30:01 fakehost CROND[31462]: (root) CMD (/usr/lib64/sa/sa1 1 1)
Jan 20 03:30:01 fakehost CROND[31461]: (root) CMD (/var/system/bin/sys-cmd -F > /dev/null 2>&1)
Jan 20 05:03:03 fakehost ntpd[3705]: synchronized to time.faux.biz, stratum 2
Jan 20 05:20:01 fakehost rsyslogd: [origin software="rsyslogd" swVersion="5.8.10" x-pid="20438" x-info="http://www.rsyslog.com"] start
Jan 20 05:22:04 fakehost cs3[31163]:  Q: ".../bin/rsync -LD ": symlink has no referent: "/var/syscmds/fakehost/runit_scripts/etc/runit/service/superImportantService/run"#012Q: ".../bin/rsync -LD ": rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1039) [sender=3.0.6]
Jan 20 05:22:04 fakehost cs3[31163]:  I: Last 2 quoted lines were generated by "/usr/local/bin/rsync -LD --recursive --delete --password-file=/var/syscmds/modules/rsync_password /var/syscmds/fakehost syscmds@fakehost::syscmds_rsync"
Jan 20 05:22:08 fakehost cs3[31163]:  Q: ".../sbin/sv restart": ok: run: /export/service/cool-service: (pid 32323) 0s
Jan 20 05:22:08 fakehost cs3[31163]:  I: Last 1 quoted lines were generated by "/sbin/sv restart /export/service/cool-service"
Jan 20 05:22:09 fakehost cs3[31163]:  R: cs3:  The cool service on fakehost does not appear to be communicating with the cool service leader.  Automating a restart of the cool service in attempt to resolve the communication problem.
Jan 20 05:22:37 fakehost ACCT_ADD: WARNING: Manifest /var/syscmds/inputs/config-general/doit.txt has been processed already, bailing
---------- end sample log extract ----------

---------- begin sample output ----------
minute, number_of_messages
Jan 20 03:25,2
Jan 20 03:26,2
Jan 20 03:30,2
Jan 20 05:03,1
Jan 20 05:20,1
Jan 20 05:22,6
---------- end sample output ----------
"""

#!/usr/bin/python
import re
from collections import Counter


def parse_log1():  # Without Regex
    """
    Time Complexity:
        O(n), where n is the number of lines in the log file

    Space Complexity:
        Input Space: O(n)
        Auxiliary Space:
            list: O(n). Since it will store all timestamp from each line
            freq: O(n). In the worst case, all timestamps can be unique
        Total Space: O(n + n) => O(n)
    """
    timestamp_list = []
    time_message_freq = {}

    # Read contents of a file
    with open('logs/messages.txt', 'r') as file:
        lines = file.readlines()

    # Parse timestamp from each line and store it in a list. Each timestamp is
    # also a key in the time_message_freq dictionary and its value is an
    # empty list
    for line in lines[1:-1]:
        timestamp = line.strip()[:12]
        timestamp_list.append(timestamp)
        time_message_freq[timestamp] = list()

    # Iterating through the list, append 1 to dictionary for each timestamp
    for timestamp in timestamp_list:
        time_message_freq[timestamp].append(1)

    # Print output in the expected format
    for k, v in time_message_freq.items():
        print('%s,%s' % (k, len(v)))

    # Write output to a CSV file
    with open("counts.csv", "w") as output_file:
        for (dt, count) in time_message_freq.items():
            output_file.write("%s,%s\n" % (dt, len(count)))


def parse_log2():  # Using Regex
    min_msg_freq_map = {}
    pattern = re.compile(r'^(\w+ \d+ \d+:\d+)\:\d+ \w+ (.*$)')
    with open('logs/messages.txt', 'r') as file:
        lines = file.readlines()

    if len(lines) > 0:
        for line in lines:
            match = pattern.match(line)
            if match:
                if match.group(0) and match.group(1):
                    minute, error = match.groups()
                    min_msg_freq_map[minute] = min_msg_freq_map.get(minute, 0) + 1
        # Write output to a CSV file
        with open("counts2.csv", "w") as output_file:
            for (min, msg_cnt) in min_msg_freq_map.items():
                output_file.write("%s,%s\n" % (min, msg_cnt))
                print('%s,%s' % (min, msg_cnt))
    else:
        print('File is empty')


def parse_log3():
    pattern = re.compile(r'\w+ \d+ \d+:\d+')
    with open('logs/messages.txt', 'r') as file:
        total = file.read()
        times = re.findall(pattern, total)
        if len(times) > 0:
            with open("counts3.csv", "w") as output_file:
                for k, v in Counter(times).items():
                    output_file.write("%s,%s\n" % (k, v))
                    print('%s,%s' % (k, v))


def main():
    # Invoke the function
    # parse_log1()
    # parse_log2()
    parse_log3()


if __name__ == '__main__':
    main()
