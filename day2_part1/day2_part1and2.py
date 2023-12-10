f = open('input.txt','r')

max_color = {'red':12,'green':13,'blue':14}

somma = 0
s_power = 0 
for line in f:
    idx = int(line.split(':')[0].split()[1])
    games = line.split(':')[1].split(';')

    min_cubes = {'red':0,'green':0,'blue':0}

    valid=True
    for game in games:

        for ele in game.split(','):
            ele = ele.strip()
            n,color = ele.split() # by spaces
            n = int(n)
            if n>max_color[color]:
                valid = False
            if n>min_cubes[color]:
                min_cubes[color] = n
        
    if valid: somma+=idx
    s_power+=min_cubes['red']*min_cubes['green']*min_cubes['blue']
            
print('Somma',somma)
print('Somma dei power dei set',s_power)

