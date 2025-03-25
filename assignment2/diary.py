import traceback

try:
    #Open a file called diary.txt for appending
    with open("diary.txt", "a") as file:
        first_prompt = "What happened today?"
        subsequent_promt = "What else?"

        entry = input(first_prompt)
        first_prompt = subsequent_promt

        #In a loop,prompt the user for a line of input and write prompts
        while entry.lower() !="done for now":
            #As each line is received, write it to diary.txt, with a newline(\n) at the end.
            file.write(entry + "\n")
            entry = input(first_prompt)
        #When the special line "done for now" is received, close the file and exit the program
        file.write("done for now\n")

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()

    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
        

  








