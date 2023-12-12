
def parse_data(filename):

    with open(filename) as d:
        data = d.read()
    
    game_list = []
    
    for l in data.splitlines():
        
        game = {}
        game['id'] = int(l.split(':')[0][5:])
        sets = l.split(':')[1].split(';')
        game['sets'] = list()
        
        for s in sets:
        
            colors = [i.strip() for i in s.split(',')]
            cubes = {'red':0,'blue':0,'green':0}
            for i in colors:
                for c in ['red','blue','green']: 
                    if c in i:
                        value = int(i.strip().split(' ')[0])
                        cubes[c] = value
                        break
            
            game['sets'].append(cubes)
            
        game_list.append(game)
        
    return game_list


def part1(data):
    
    valid_games = []

    for game in data:
        valid = True
        for set in game['sets']:
            if set['red'] > 12 or set['blue'] > 14 or set['green'] > 13:
                valid = False
                break
                
        if valid:
            valid_games.append(game['id'])

    return sum(valid_games)
    
def part2(data):
    
    game_power = []
    
    for game in data:
        min_values = {'red':0,'blue':0,'green':0}
        for set in game['sets']:
            for c in ['red','blue','green']:
                if set[c] > min_values[c]:
                    min_values[c] = set[c]
        power = min_values['red'] * min_values['green'] * min_values['blue']
        game_power.append(power)
    
    return sum(game_power)
 

if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
