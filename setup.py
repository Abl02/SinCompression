#! /bin/python3

import psutil
import argparse
from multiprocessing import Process
from ffcompress import DISPATCHER_P, DISPATCHER_N, exit


class bcolors:
    HEADER = "\33[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Main:
    def __init__(self, args) -> None:
        print(DISPATCHER_P, DISPATCHER_N)
        self.env_loop()

    def env_input(self):
        return input(
            bcolors.HEADER + "▰▰▰▰" + bcolors.OKBLUE + "▰▰▰▰ >> " + bcolors.ENDC
        )

    def clear_process(self, process_list):
        for p in process_list:
            try:
                # Use psutil to get the process by PID
                psutil_proc = psutil.Process(p.pid)
                # Check if the process is a zombie
                if psutil_proc.status() == psutil.STATUS_ZOMBIE:
                    print(f"Process PID {p.pid} is a zombie.")
                    p.join()
                else:
                    print(
                        f"Process PID {p.pid} is running with status: {psutil_proc.status()}"
                    )
            except psutil.NoSuchProcess:
                print(f"Process PID {p.pid} has already terminated.")
                process_list.remove(p)

    def env_loop(self):
        running = True
        proc = []
        while running:
            cinput = self.env_input().split()  # Input array
            for i in range(len(cinput)):
                if cinput[i].isdigit():
                    cinput[i] = int(cinput[i])
                elif cinput[i].lower() in ["true", "t"]:
                    cinput[i] = True
                elif cinput[i].lower() in ["false", "f"]:
                    cinput[i] = False
            if not cinput:
                cinput = [""]
            if cinput[0] in DISPATCHER_P:  # if Input0 is a known command then start it
                command = DISPATCHER_P[cinput[0]]
                arg = cinput[1:]
                print(command, arg)
                p = Process(target=command, args=(arg))
                p.start()
                proc.append(p)

            elif cinput[0] in DISPATCHER_N:
                command = cinput[0] + "("
                for e in cinput[1:]:
                    if isinstance(e, str):
                        command += '"' + e + '"'
                    else:
                        command += str(e)
                    command += ","
                command += ")"
                print(command)
                eval(command, {"__builtins__": None}, DISPATCHER_N)

            elif cinput[0] == "exit" or cinput[0] == "x":
                for p in proc:
                    p.kill()
                exit()
                running = False

            self.clear_process(proc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example script for using argparse.")
    parser.add_argument("--idk", type=int, help="show the help")

    args = parser.parse_args()

    Main(args)
