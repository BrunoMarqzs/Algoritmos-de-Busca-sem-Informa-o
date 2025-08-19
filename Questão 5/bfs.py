from collections import deque

def send_more_money_bfs():
    letters = 'SENDMORY'
    queue = deque([{}])
    
    while queue:
        mapping = queue.popleft()
        if len(mapping) == len(letters):
            if mapping['S'] == 0 or mapping['M'] == 0:
                continue
            send = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
            more = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
            money = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']
            if send + more == money:
                return mapping, send, more, money
        else:
            next_letter = letters[len(mapping)]
            for d in range(10):
                if d not in mapping.values():
                    new_mapping = mapping.copy()
                    new_mapping[next_letter] = d
                    queue.append(new_mapping)

solution_bfs = send_more_money_bfs()
print(solution_bfs)
