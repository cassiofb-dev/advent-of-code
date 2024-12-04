import os, sys, glob, subprocess

class SolutionRunner:
    def __init__(self, enable_benchmark=False):
        self.ran_commands = []
        self.enable_benchmark = enable_benchmark

    def write_output(self, program_path: str, output: str):
        output_file = open(f"{program_path}.log", "wb")
        output_file.write(output)
        output_file.close()

        results_file = open("run_solutions.log", "a")
        results_file.write("----------------------------------------------------------------\n")
        results_file.write(f"Program: {program_path}\n")
        results_file.write(f"Output: {output}\n")
        results_file.close()

    def run_c(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["gcc", "-o", f"{program_path}.bin", program_path])

        command = [f"{program_path}.bin"]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_rust(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["rustc", "-o", f"{program_path}.bin", program_path])

        command = [f"{program_path}.bin"]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_java(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["javac", program_path])

        class_path = program_path[:program_path.rfind('/')]

        command = [
            "java",
            "-cp",
            class_path,
            "Main",
        ]

        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_python(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        command = ["python", program_path]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_javascript(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        command = ["node", program_path]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_benchmark(self):
        if len(self.ran_commands) < 1: return

        output = subprocess.check_output([
            "hyperfine",
            "--shell=none",
            "--warmup",
            "100",
            "--runs",
            "100",
            *self.ran_commands,
            "--export-markdown",
            "run_solutions.md",
        ])

    def run(self):
        open("run_solutions.log", "w").close()

        path_list = glob.glob(os.getcwd() + "/editions/**", recursive=True)
        for path in path_list:
            if os.path.isfile(path) == False: continue

            if path.endswith("c"):
                self.run_c(path)
            elif path.endswith("rs"):
                self.run_rust(path)
            elif path.endswith("java"):
                self.run_java(path)
            elif path.endswith("py"):
                self.run_python(path)
            elif path.endswith("js"):
                self.run_javascript(path)

        if self.enable_benchmark:
            self.run_benchmark()

def main():
    enable_benchmark = len(sys.argv) > 1 and sys.argv[1] == "benchmark"

    solutionRunner = SolutionRunner(enable_benchmark=enable_benchmark)
    solutionRunner.run()

if __name__ == "__main__":
    main()
