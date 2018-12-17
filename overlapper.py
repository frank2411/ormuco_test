def check_overlap():
    start_line = int(input("Start number for first line: "))
    end_line = int(input("Ender number for first line: "))

    start_line_two = int(input("Start number for second line: "))
    end_line_two = int(input("Ender number for second line: "))

    # If some very funny guy tries to break the program
    # by inverting start and ending numbers I'll order them a second time

    if end_line < start_line:
        temp_start_line = start_line
        start_line = end_line
        end_line = temp_start_line

    if end_line_two < start_line_two:
        temp_start_line_two = start_line_two
        start_line_two = end_line_two
        end_line_two = temp_start_line_two

    # First overlap check. This check the second line start
    if start_line >= start_line_two <= end_line:
        print("LINES OVERLAP")
        return True

    # Second overlap check. This check the second line end
    if start_line >= end_line_two <= end_line:
        print("LINES OVERLAP")
        return True

    print("LINES DON'T OVERLAP")


if __name__ == "__main__":
    try:
        check_overlap()
    except ValueError:
        print("Not a valid integer was provided. Exiting")
