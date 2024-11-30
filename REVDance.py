def min_moves_to_follow_instructions(n, instructions):
    tiles = ['up', 'down', 'left', 'right']
    tile_index = {tile: i for i, tile in enumerate(tiles)}
    INF = float('inf')
    
   
    dp = [[[INF] * 4 for h in range(4)] for h in range(n + 1)]
    
    for L in range(4):
        for R in range(4):
            dp[0][L][R] = 0
    
    for i in range(1, n + 1):
        current_tile = tile_index[instructions[i - 1]]
        for L in range(4):
            for R in range(4):
                dp[i][current_tile][R] = min(dp[i][current_tile][R], dp[i - 1][L][R] + (0 if L == current_tile else 1))
                dp[i][L][current_tile] = min(dp[i][L][current_tile], dp[i - 1][L][R] + (0 if R == current_tile else 1))
    
    return min(dp[n][L][R] for L in range(4) for R in range(4))

n = int(input())
instructions = [input().strip() for _ in range(n)]

print(min_moves_to_follow_instructions(n, instructions))
