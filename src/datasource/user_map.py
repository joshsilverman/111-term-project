
map = {}
mapReverse = {}

def set(users):
    
    for user in users: 
        map[user['user.name']] = user['user.userid']
        mapReverse[user['user.userid']] = user['user.name']
        