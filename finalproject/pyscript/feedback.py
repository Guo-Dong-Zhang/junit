def checkresult(_output):
    output = _output
    if("OK" in str(output)):
        list = str(output).split(" ")
        # print(list[-2])
        # print([int(i) for i in list[-2].split("(") if i.isdigit()][0])
        success_times = [int(i) for i in list[-2].split("(") if i.isdigit()][0]
        failure_times = 0


    else:

        list = str(output).split(" ")
        print(list[-4:])
        total = list[-4][0]
        print(total)
        failure_times = [int(i) for i in list[-1].split("\\") if i.isdigit()][0]
        print(failure_times)
        success_times = int(total) - failure_times

        print(success_times)

    return success_times, failure_times
