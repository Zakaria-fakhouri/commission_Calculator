import threading

def input_integer(value):
    while True:
        try:
            userinput = int(input(f"Enter {value}: "))
            return userinput
        except ValueError:
            print("Please Enter an Integer")
            continue
def arrangement_test():
        global limit_list
        if limit_list[x - 1] >= limit_list[x]:
            print("Worng arrangement")
            limit_list.pop()
            return False
        else:
            return True
def input_values(search,search_list):
    done = False
    while not done:
        value = input_integer(f"{search}")
        search_list.append(value)
        if x > 0 and search == "limit":
            done = arrangement_test()
        else:
            done = True
def final_outcome():
    global x
    final_outcome = 0
    y = len(limit_list)
    while x != 0:
        if x == y:
            final_outcome += limit_list[0] * pro_list[0]
        else:
            final_outcome += pro_list[x] * (limit_list[x] - limit_list[x - 1])
        x -= 1
    return final_outcome
def maximum_funk(numb):
    done = False
    while not done:
        try:
            Maximum = (input("Enter a Maximum Provision(If you dont want one press 'N'): "))
            if Maximum == "N" or int(Maximum) >= numb:
                print("End Provision: " + str(numb))
            elif int(Maximum) < numb:
                print("End Provision: " + str(Maximum))
            print("----------------------------")
            done = True
        except ValueError:
            print("Geben sie entweder eine Zahl oder 'N' ein")

def threader(task,split=6):
    threads = [threading.Thread(target=task, args=(task_id,)) for task_id in range(1, split)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    pro_list = []
    limit_list = [-1,0]
    x = 0
    Customer = input_integer("Sum of Customer")
    while limit_list[x-1] < Customer:
        if x == 0 :
            limit_list.clear()
        input_values("limit",limit_list)
        input_values("Provision",pro_list)
        print("----------------------------")
        x += 1
    threader(maximum_funk(final_outcome()),x)
