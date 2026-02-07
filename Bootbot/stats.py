def count_words(path):
    count = 0
    with open(path) as f:
        read = f.read()
        words = read.split()
        count += len(words)
    return count

def count_char(path):
    dict = {}
    with open(path) as f:
        read = f.read()
    
    low_ch = read.lower()
    
    ch = list(low_ch)
    
    for result in ch:
        if result in dict:
            dict[result] += 1
        else:
            dict[result] = 1
    return dict

def sort_on(items):
    return items["num"]
