import subprocess


def run(ape_location, input_fasta):
    s = subprocess.run([ape_location, input_fasta], capture_output=True, text=True)
    return s.stdout
