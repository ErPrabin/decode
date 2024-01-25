
def decode(filepath):
    dist={}
    with open(filepath,'r') as f:
        for x in f:
            splitted_words=x.split()
            dist[x[0]]=splitted_words[1]
    
    sorted_dict = {k: dist[k] for k in sorted(dist)}
    new_list=[]
    keys = list(sorted_dict.keys())

    num_levels = len(keys)
    start_number = 1
    # Print the pyramid pattern
    for i in range(num_levels):
        new_list.append(keys[start_number-1:start_number+i])
        print("".join(keys[start_number-1:start_number+i]))
        start_number += i+1

    message=[]
    for item in new_list:
        message.append(sorted_dict[item[-1]]) if len(item) else ''

    print(' '.join(message))  

        

decode('sample2.txt')

