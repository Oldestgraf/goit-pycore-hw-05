import sys

def parse_log_line(line: str) -> dict:
    """Create dictionary for each log line"""
    parts = line.split(" ", 3)
    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = parts[3]
    return {"date": date, "time": time, "level": level, "message": message}

def load_logs(file_path: str) -> list:
    """Download logs from file and divide to separate log lines"""
    log_list = []
    try:
        with open(file_path, "r", encoding='utf-8') as log_file:
            for line in log_file:
                log_list.append(parse_log_line(line))
    except FileNotFoundError:
        print("Incorrect path or file is absent.")
    except Exception as e:
        print(f"Exception: {e}")
    return log_list

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by level"""
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    """Count records by level"""
    counts = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    print(list)
    for log in logs:
        counts[log["level"]] += 1
    print(counts)
    return counts

def display_log_counts(counts: dict):
    """Format and display results"""
    print("Рівень логування | Кількість")
    print("---------------- | ---------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<9}")

def display_logs(logs: list, level: str):
    print(f"Деталі логів для рівня '{level}'")
    for log in logs:
        if log["level"] == level:
            print(f"{log["date"]} {log["time"]} - {log["message"]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage example: python3 [main.py](<http://main.py/>) /path/to/logfile.log [<log_level>]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = None
    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()

    logs = load_logs(log_file_path)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if filtered_logs:
            display_logs(logs, log_level)
        else:
            print(f"No logs found for level '{log_level}'.")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)