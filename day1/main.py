
def parse_data(filename):

    with open(filename) as d:
        data = d.read()

    return data


def part1(data):
    
    lines = data.splitlines()
    
    calibration_values = list()

    for l in lines:
        
        for c in l:
            if c.isdigit():
                first_digit = c
                break
        
        for c in l[::-1]:
            if c.isdigit():
                last_digit = c
                break
        
        value = int(first_digit + last_digit)
        calibration_values.append(value)

    return sum(calibration_values)

def value_finder(line,reversed):
    
    values_dict = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    values = [str(i) for i in range(1,10)] + list(values_dict.keys())
    if reversed:
        values = [i[::-1] for i in values]
    
    digit = None
    c = True
    
    while c == True:
        
        for i in values:
            if line.startswith(i):
                if i.isdigit():
                    digit = i
                    c = False
                    break
                else:
                    if reversed:
                        digit = values_dict[i[::-1]]
                    else:
                        digit = values_dict[i]
                    c = False
                    break

        line = line[1:]
                    
    return digit       
        

def part2(data):
    
    lines = data.splitlines()
    calibration_values = list()
    
    for line in lines:
        first_digit = value_finder(line,reversed=False)
        last_digit = value_finder(line[::-1],reversed=True)
        calibration_values.append(int(first_digit + last_digit))
        
    return sum(calibration_values)


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
