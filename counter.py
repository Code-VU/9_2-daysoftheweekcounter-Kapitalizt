def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")    # end assignment
    fhand = open(file_name)

    day_counts = dict()
    for line in fhand:
        
        words = line.split()
        if len(words) < 2:
            continue
        if words[0] != 'From':
            continue
        #print(line) 
        day = words[2]
        for word in words:
            if word != day:
                continue
            day_counts[word] = day_counts.get(word,0) + 1
            
    print(day_counts)

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## countDayOfTheWeek()