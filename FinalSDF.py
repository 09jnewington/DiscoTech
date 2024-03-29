import subprocess
import os
import glob

input_dir = r"pdb_files"  # Replace with your PDBQT files directory
output_file = r"final_sdf_output.sdf"  # Name of the output SDF file


def run():
    # Find all PDBQT files in the input directory
    pdbqt_files = glob.glob(os.path.join(input_dir, "*docked.pdbqt"))

    # Open the output file
    with open(output_file, "w") as sdf_output:
        # Loop through each PDBQT file and append to the SDF file
        for file in pdbqt_files:
            subprocess.run(["obabel", file, "-O", "temp.sdf"])
        
            # Read the converted file and append it to the output SDF file
            with open("temp.sdf", "r") as temp_sdf:
                sdf_output.write(temp_sdf.read())
                sdf_output.write("\n$$$$\n")  # SDF record separator

    # Remove the temporary SDF file
    os.remove("temp.sdf")

    print("Conversion complete. Output saved in:", output_file)

if __name__ == '__main__':
    run()
