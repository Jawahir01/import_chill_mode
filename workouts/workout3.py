# Algorithms: Interval Merger
# The Challenge: Given a collection of intervals, merge all overlapping intervals.
# Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Logic: Sort the intervals based on the start time first, then iterate through to merge 
# adjacent intervals if they overlap.

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check if there is an overlap
        if current[0] <= last_merged[1]:
            # Merge the intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    
    return merged



# Example usage:
input_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(input_intervals))  # Output: [[1, 6], [8, 10], [15, 18]]

# Example usage2:
input_intervals2 = [[1,4],[4,5]]    
print(merge_intervals(input_intervals2))  # Output: [[1, 5]]

# Example usage3:
input_intervals3 = [[1, 4], [3, 5], [6, 8], [8, 9], [10, 12]]
print(merge_intervals(input_intervals3))  # Output: [[1, 5], [6, 9], [10, 12]]