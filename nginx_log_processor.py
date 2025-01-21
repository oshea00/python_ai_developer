import json
import re
import sys


def decode_escape_sequences(s):
    return bytes(s, "utf-8").decode("unicode_escape")


def process_log_line(line):
    timestamp_match = re.search(r"\[(.*?)\]", line)
    request_body_match = re.search(r'request_body="(\{.*\})"', line)

    if timestamp_match and request_body_match:
        timestamp = timestamp_match.group(1)
        request_body = request_body_match.group(1)
        decoded_body = decode_escape_sequences(request_body)
        json_content = json.loads(decoded_body)
        pretty_json = json.dumps(json_content, indent=4)

        print(f"Timestamp: {timestamp}")
        print(pretty_json)


def main():
    if len(sys.argv) != 2:
        print("Usage: python nginx_log_processor.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]

    with open(log_file, "r") as file:
        for line in file:
            if "POST" in line:
                process_log_line(line)


if __name__ == "__main__":
    main()
