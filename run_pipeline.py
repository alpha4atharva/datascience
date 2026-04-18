import os
import sys
import subprocess
import glob

def run_command(command, cwd=None):
    print(f"\n[RUNNING]: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd)
    if result.returncode != 0:
        print(f"\n[ERROR] Command failed with exit code {result.returncode}: {' '.join(command)}")
        sys.exit(result.returncode)
    print(f"[SUCCESS] Command completed.\n")

def main():
    # 1. Ensure we are running from the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # 2. Install dependencies from requirements.txt
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        print("====== INSTALLING REQUIREMENTS ======")
        run_command([sys.executable, "-m", "pip", "install", "-r", req_file])
    else:
        print(f"[WARNING] {req_file} not found. Skipping dependency installation.")

    # 3. Locate all numbered notebooks
    notebooks_dir = "notebooks"
    if not os.path.exists(notebooks_dir):
        print(f"[ERROR] Notebooks directory '{notebooks_dir}' not found!")
        sys.exit(1)
        
    notebooks = sorted(glob.glob(os.path.join(notebooks_dir, "0[1-8]_*.ipynb")))
    if not notebooks:
        print("[ERROR] No pipeline notebooks found (e.g., 01_data_cleaning.ipynb)!")
        sys.exit(1)
        
    print("====== PIPELINE IDENTIFIED ======")
    for idx, nb in enumerate(notebooks, 1):
        print(f"  {idx}. {os.path.basename(nb)}")
        
    # 4. Execute notebooks sequentially
    for nb in notebooks:
        print(f"\n{'='*60}")
        print(f"EXECUTING NOTEBOOK: {os.path.basename(nb)}")
        print(f"{'='*60}")
        
        # Execute the notebook using nbconvert
        # Executing in-place to update cell output in the actual notebook file
        run_command([
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=600",
            nb
        ])
        
    print("\n" + "="*60)
    print("ALL NOTEBOOKS EXECUTED SUCCESSFULLY!")
    print("PIPELINE COMPLETED.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
