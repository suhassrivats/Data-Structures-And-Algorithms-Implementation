# Given an input like this [(2,5), (3, 6), (7,8)], determine how many CPUs are needed. A CPU can be reused only if a previous process is done using it. 
# For example, (7,8) can either use CPU1 or CPU2 because its start time is greater than CPU1/2s end time.
# CPU1 - (2,5)
#CPU2 - (3,6)
# CPU1 - (7,8)
# Output : 2

def cpu_count(input):
    cpu_counter = 0
    end_times = []
    
    # Sort input intervals by end_times
    sorted_times = input.sort(key=lambda x: x[1])  
    
    for time in sorted_times:
        start, end = time[0], time[1]
        
        # This is for the first element
        if len(end_times) == 0:
            cpu_counter += 1            
        else:
            for et in end_times:
                if start < et:
                    cpu_counter += 1
        end_times.append(end)
            
    return cpu_counter
