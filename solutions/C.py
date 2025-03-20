def get_distance(from_pos, to_pos, L):
    return (to_pos - from_pos + L) % L


import sys


def main():
    input_data = sys.stdin.read().strip().splitlines()
    if not input_data:
        return
    N, L, S = map(int, input_data[0].split())

    taxi_states = {}
    output_lines = []

    for line in input_data[1:]:
        parts = line.split()
        if not parts:
            continue
        event_type = parts[0]
        if event_type == "TAXI":
            timestamp = int(parts[1])
            taxi_id = int(parts[2])
            taxi_pos = int(parts[3])
            taxi_states[taxi_id] = (timestamp, taxi_pos)
        elif event_type == "ORDER":
            order_timestamp = int(parts[1])
            order_id = int(parts[2])
            order_pos = int(parts[3])
            order_time = int(parts[4])

            available = []
            for taxi_id, (ts, pos) in taxi_states.items():
                if ts <= order_timestamp:
                    dt = order_timestamp - ts
                    next_pos = (pos + S * dt) % L
                    d1 = get_distance(pos, order_pos, L)
                    d2 = get_distance(next_pos, order_pos, L)
                    mx_d = max(d1, d2)
                    if mx_d <= order_time * S:
                        available.append(taxi_id)
            if not available:
                output_lines.append("-1")
            else:
                output_lines.append(" ".join(str(tid) for tid in available[:5]))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()