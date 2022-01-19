'''
Compare config.json (static) with API response and update config.json with the
new content. Once updated, send SIGHUP signal.
'''
import requests
import json
import time
import sys
import os


def get_config_output():
    with open('/home/interview/interview/webserver/config.json', 'r') as json_file:
        config_dict = json.load(json_file)
    return config_dict


def read_webserver_pid():
    with open('/home/interview/interview/webserver/webserver.pid', 'r') as f:
        pid = f.readlines()
    return pid[0]


def main():
    while True:
        try:
            response = requests.get('http://localhost:8080')
            pid = read_webserver_pid()
            cmd = 'sudo kill -SIGHUP $s' % pid
            if response.status_code == 200:
                result_dict = response.json()
                config_dict = get_config_output()
                # Write to config.json if it doesn't match
                if result_dict != config_dict:
                    f = open('/home/interview/interview/webserver/config.json', 'w')
                    json.dump(result_dict, f)
                    os.system(cmd)
                    print('OK')
                    f.close()
                else:
                    print('Dictionaries are matching. Nothing to do.')
                time.sleep(2)
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            sys.exit()


if __name__ == '__main__':
    main()
