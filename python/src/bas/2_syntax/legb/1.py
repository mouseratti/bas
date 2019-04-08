# import builtins

global_variable = 2
global_list = []

LOCAL - ENCLOSED - GLOBAL - BUILTINS


def enclosed_function():
    enclosed_variable = 1
    global_list.append("enclosed_function")
    def function_set_5():
        global global_variable
        # nonlocal enclosed_variable
        # print("global_variable is {}; enclosed_variable is {}; local_variable is {}".format(
        #     global_variable,
        #     enclosed_variable,
        #     local_variable,
        #     )
        # )
        global_variable = 5
        enclosed_variable = 5
        local_variable = 5
        global_list.append("function_set_5")
        print("function_set_5: global_variable is {}; enclosed_variable is {}; local_variable is {}".format(
            global_variable,
            enclosed_variable,
            local_variable,
            )
        )
    function_set_5()
    print("enclosed_function: global_variable is {}; enclosed_variable is {}".format(
        global_variable,
        enclosed_variable,
        # local_variable,
        )
    )

enclosed_function()

print("global: global_variable is {}".format(global_variable))
print(global_list)