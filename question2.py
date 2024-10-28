def prompt_until_exit():
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        print(f"You entered: {user_input}")

# Calling the function
prompt_until_exit()
