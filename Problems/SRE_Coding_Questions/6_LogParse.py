'''
Parse log file in the below format and a third column to output file.

sample.csv:
name,title
suhas,devops
prem,developer

output.csv:
name,title,location
suhas,devops,San Jose
prem,developer,San Jose
'''


def main():
    with open('sample.csv') as f:
        lines = f.readlines()
        if len(lines) > 0:
            # Write output
            with open('output.csv', 'w') as of:
                header = 'name,title,location\n'
                of.write(header)
                for line in lines[1:]:
                    name, title = line.strip().split(',')
                    body = '%s,%s,San Jose\n' % (name, title)
                    of.write(body)
        else:
            print('File is empty')


if __name__ == '__main__':
    main()
