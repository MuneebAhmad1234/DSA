def activity_selection(activities):
    """
    Function to select the maximum number of non-overlapping activities.
    :param activities: List of tuples where each tuple represents (start_time, end_time)
    :return: List of selected activities
    """
    # Sort activities based on their end times
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    # Iterate through the activities and select non-overlapping ones
    for start, end in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end

    return selected_activities


if __name__ == "__main__":
    print("Activity Selection Problem")
    print("Enter activities as pairs of start and end times (e.g., 1 3). Type 'done' to finish input.")

    activities = []
    while True:
        user_input = input("Enter activity (start end): ").strip()
        if user_input.lower() == "done":
            break
        try:
            start, end = map(int, user_input.split())
            if start < 0 or end < 0 or start >= end:
                print("Invalid activity. Start time must be less than end time, and both must be non-negative.")
                continue
            activities.append((start, end))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

    if not activities:
        print("No activities provided. Exiting.")
    else:
        selected = activity_selection(activities)
        print("Selected activities:", selected)
