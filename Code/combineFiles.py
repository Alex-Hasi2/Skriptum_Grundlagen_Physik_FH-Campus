# A script to insert the content of the latex .tex files into the main.tex file
# At the locations in the main.tex file where there are \include{filename} commands, the content of filename.tex file should be inserted.


import argparse
import os


def combine_latex_files(main_folder, main_file, output_file):

    # Make sure that main.tex cannot be the output file
    if main_file == output_file:
        raise ValueError("The output file cannot be the same as the main file.")
    
    main_file_path = os.path.join(main_folder, main_file)
    with open(main_file_path, 'r', encoding='utf-8') as mf:
        main_content = mf.readlines()

    combined_content = []
    for line in main_content:
        if line.strip().startswith(r'\include{'):
            # Comment out the include statement
            combined_content.append('% ' + line)
            section_name = line.strip()[9:-1]  # Extract the section name
            section_file = os.path.join(main_folder, f"{section_name}.tex")
            if os.path.exists(section_file):
                print(f"Inserting content from {section_file}")
                with open(section_file, 'r', encoding='utf-8') as sf:
                    section_content = sf.read()
                    # Insert comment % Start of <filename.tex> before the content and a comment % End of <filename.tex> after the content
                    combined_content.append(f"% ---- Start of {section_name}.tex\n") 
                    combined_content.append(section_content + '\n')
                    combined_content.append(f"% ---- End of {section_name}.tex\n")
            else:
                print(f"Warning: Section file {section_file} not found.")
        else:
            combined_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as of:
        of.writelines(combined_content)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Combine a LaTeX main file with its \include{} files into one output file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/combineFiles.py
  python Code/combineFiles.py --main-folder "C:/Users/Alexa/Documents-Alex/FH Campus/Skriptum_Grundlagen_Physik_FH-Campus" --main-file main.tex --output-file combined_main.tex
  python Code/combineFiles.py --main-folder "C:/Project" --main-file main.tex --output-file combined_main.tex
""",
    )
    parser.add_argument(
        "--main-folder",
        default=r"C:/Users/Alexa/Documents-Alex/FH Campus/Skriptum_Grundlagen_Physik_FH-Campus/",
        help="Folder that contains the LaTeX files. Defaults to the current hardcoded path used by the script.",
    )
    parser.add_argument(
        "--main-file",
        default="main.tex",
        help="Main LaTeX file that contains the \include{} statements.",
    )
    parser.add_argument(
        "--output-file",
        default="combined_main_2026-02-28.tex",
        help="Output file to write the combined LaTeX document to.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    combine_latex_files(args.main_folder, args.main_file, args.output_file)


if __name__ == "__main__":
    main()