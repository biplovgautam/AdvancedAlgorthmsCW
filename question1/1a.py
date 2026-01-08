import math

def get_total_distance(hub, sensors):
    """Calculates the sum of Euclidean distances from the hub to all sensors."""
    total = 0
    hx, hy = hub
    for sx, sy in sensors:
        # Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
        total += math.sqrt((sx - hx)**2 + (sy - hy)**2)
    return total

def solve(sensor_locations):
    # 1. Start at the Centroid (average of all points)
    n = len(sensor_locations)
    curr_x = sum(s[0] for s in sensor_locations) / n
    curr_y = sum(s[1] for s in sensor_locations) / n
    
    curr_dist = get_total_distance((curr_x, curr_y), sensor_locations)
    
    # 2. Set initial parameters
    # Start with a large step, then shrink it for precision
    step = 100.0 
    precision = 1e-7
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Up, Down, Right, Left
    
    # 3. Iterative search
    while step > precision:
        found_better = False
        for dx, dy in directions:
            next_x = curr_x + dx * step
            next_y = curr_y + dy * step
            next_dist = get_total_distance((next_x, next_y), sensor_locations)
            
            # If moving in this direction improves the result, move there
            if next_dist < curr_dist:
                curr_dist = next_dist
                curr_x = next_x
                curr_y = next_y
                found_better = True
                break 
        
        # 4. If no direction was better, make the search area smaller
        if not found_better:
            step /= 2.0
            
    return curr_dist

# Testing with Example 1
sensors1 = [[0,1],[1,0],[1,2],[2,1]]
print(f"Example 1 Output: {solve(sensors1):.5f}") # Expected: 4.00000

# Testing with Example 2
sensors2 = [[1,1],[3,3]]
print(f"Example 2 Output: {solve(sensors2):.5f}") # Expected: 2.82843


