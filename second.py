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

def preprocess_in2(in2_filename):
    with open(in2_filename, 'r') as in2_file:
        in2_data = in2_file.read()

    # Extract IP addresses from space-separated data
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    in2_ip_addresses = re.findall(ip_pattern, in2_data)

    return in2_ip_addresses

def compare_ips(output_filename, in2_ip_addresses, out2_filename):
    with open(output_filename, 'r') as output_file:
        output_lines = output_file.readlines()

    # Compare each IP address from output.txt with in2_ip_addresses
    match_results = [ip.strip() in in2_ip_addresses for ip in output_lines]

    with open(out2_filename, 'w') as out2_file:
        for match in match_results:
            out2_file.write("Match\n" if match else "No Match\n")

if __name__ == '__main__':
    input_filename = 'input.txt'         # Replace with your input file
    output_filename = 'output.txt'       # Replace with desired output file
    in2_filename = 'in2.txt'             # Replace with in2 file
    out2_filename = 'out2.txt'           # Desired file for comparison results
    
    extract_ips(input_filename, output_filename)
    in2_ip_addresses = preprocess_in2(in2_filename)
    compare_ips(output_filename, in2_ip_addresses, out2_filename)
