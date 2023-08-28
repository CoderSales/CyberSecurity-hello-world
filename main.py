import re

def extract_ips(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        data = input_file.read()
    
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, data)
    
    # Sort IP addresses in descending order
    ip_addresses.sort(reverse=True)
    
    with open(output_filename, 'w') as output_file:
        for ip in ip_addresses:
            output_file.write(ip + '\n')

if __name__ == '__main__':
    input_filename = 'input.txt'         # Replace with your input file
    output_filename = 'output.txt'       # Replace with desired output file
    
    extract_ips(input_filename, output_filename)
    
    with open(output_filename, 'r') as output_file:
        lines = output_file.readlines()

    lines.sort(key=lambda line: [int(part) if part.isdigit() else part for part in re.split(r'\.|\s+', line)], reverse=True)

    with open(output_filename, 'w') as output_file:
        for line in lines:
            output_file.write(line)
