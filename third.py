def count_matches_and_update_check(out2_filename, match_count_filename, match_check_filename):
    with open(out2_filename, 'r') as out2_file:
        lines = out2_file.readlines()

    match_count = sum(1 for line in lines if line.strip() == "Match")

    with open(match_count_filename, 'w') as match_count_file:
        match_count_file.write(str(match_count))

    with open(match_check_filename, 'w') as match_check_file:
        match_check_file.write("Has Matches" if match_count > 0 else "No Matches")

if __name__ == '__main__':
    out2_filename = 'out2.txt'               # File containing comparison results
    match_count_filename = 'match_count.txt' # New file to store the match count
    match_check_filename = 'match_check.txt' # New file to indicate if there are matches

    count_matches_and_update_check(out2_filename, match_count_filename, match_check_filename)
