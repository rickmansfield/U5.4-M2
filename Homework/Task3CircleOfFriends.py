def dfs(r, f, v): # row, friends, visited
    v.add(r)
    
    for neighbor in range(len(f[r])):
        if f[r][neighbor] == 1 and neighbor not in v:
            dfs(neighbor, f, v)
    return v

def solution(friendships):
    count = 0
    checked = set()
    
    if friendships is None or len(friendships) == 0:
        return 0
        
    for eachRow in range(len(friendships)):
        if friendships[eachRow][eachRow] == 1 and eachRow not in checked:
            count += 1
            checked= dfs(eachRow, friendships, checked)
            
    return count