from collections import defaultdict, deque
input = [l[:-1] for l in open('input.txt','r').readlines()]
modules = dict()

for line in input:
    module, dests = line.split(' -> ')
    dests = dests.split(', ')
    mod_type, name = module[0], module[1:]

    modules[name] = [mod_type, 0,     dict(),  dests]
    #                % or &    % on   & memory outputs
    for dest in dests:
        if dest not in modules:
            modules[dest] = ['output', 0, {}, []]

for name, (_, _, _, dests) in modules.items():
    for dest in dests:
        if modules[dest][0] == '&':
            modules[dest][2][name] = 0
# print(modules)

q = deque()
pulses = [0,0]

criticals = ['mp','qt','qb','ng']
cycles = {key: [] for key in criticals}

for i in range(1,50000):
    pulses[0] += 1
    q.append(('roadcaster',  0,     'button'))
    #         name, pulse, origin
    while q:
        # print(q)
        (name, pulse, orig) = q.popleft()
        module = modules[name]
        [mod_type, on, memory, dests] = module


        match mod_type:
            case 'b':
                for dest in dests:
                    q.append((dest, pulse, name))
                    pulses[pulse] += 1
            case '%':
                if not pulse:
                    modules[name][1] = 0 if on else 1
                    for dest in dests:
                        q.append((dest, modules[name][1], name))
                        pulses[modules[name][1]] += 1
            case '&':
                memory[orig] = pulse
                send = 0 if all(memory.values()) else 1
                if name in criticals and send:
                    cycles[name].append(i)
                for dest in dests:
                    q.append((dest, send, name))
                    pulses[send] += 1

# print(pulses)
# print(pulses[0]*pulses[1])
least_common_multiple_assuming_no_common_factors = 1
for k,v in cycles.items():
    print(k,v)
    least_common_multiple_assuming_no_common_factors *= v[0]
print(least_common_multiple_assuming_no_common_factors)