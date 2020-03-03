#!/usr/bin/env python3

def avgrun():
    user_jog_sessions = 0
    total_time_of_run = 0 

    while True:
        one_run = input("Enter total run time for workout, or 'q' to exit: ")

        if one_run == 'q':
            break 
        
        else: 
            user_jog_sessions += 1
            total_time_of_run += float(one_run)

    avg_time_of_all_runs = total_time_of_run / user_jog_sessions

    print(f"Average time of {avg_time_of_all_runs}, over {user_jog_sessions} runs")

def main():
    avgrun()

if __name__ == "__main__":
    main()
    
    

    