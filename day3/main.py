import re
# Last tries: 521242, 521318 
# Too low

def parse_data(filename):

    with open(filename) as d:
        raw_data = d.read()
        
    data = raw_data.splitlines()
    encap_data = [(len(data[0]) + 2)*'.'] + [f'.{line}.' for line in data] + [(len(data[0]) + 2)*'.']
    
    return encap_data


def part1(data):
    
    part_numbers = []
    rownum = len(data)
    
    for row in range(1,rownum - 1):
        numbers = re.findall('[0-9]+', data[row])
        
        for n in numbers:

            col = re.search(n, data[row])
            start_index = col.start()
            end_index = col.end()
            
            left = data[row][start_index - 1]
            right = data[row][end_index]
            up_string = data[row-1][start_index - 1 : end_index + 1] 
            down_string = data[row+1][start_index - 1 : end_index + 1]
            
            chars_around = [left , right] + [c for c in up_string] + [c for c in down_string]
            
            valid_part_number = False
            for element in chars_around:
                if not (element == '.' or element.isdigit()):
                    valid_part_number = True
                    break


            if valid_part_number:
                part_numbers.append(int(n))
                
            cleanup_row = [c for c in data[row]]
            for i in range(start_index,end_index):
                cleanup_row[i] = '.'
            
            data[row] = ''.join(cleanup_row)
                        
    return sum(part_numbers)


def part2(data):
    
    return False


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
