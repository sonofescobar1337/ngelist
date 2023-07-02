import hashlib
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <input_file_path> <output_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

completed_lines_hash = set()
output_file = open(output_file_path, "w")
for line in open(input_file_path, "r"):
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)


output_file.close()

print("Duplicate lines have been removed successfully.")