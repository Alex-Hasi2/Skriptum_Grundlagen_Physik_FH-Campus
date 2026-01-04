# A script to insert the content of the latex .tex files into the main.tex file 
# At the locations in the main.tex file where there are \include{filename} commands, the content of filename.tex file should be inserted. 


import os

def combine_latex_files(main_folder, main_file, output_file):
    main_file_path = os.path.join(main_folder, main_file)
    with open(main_file_path, 'r') as mf:
        main_content = mf.readlines()

    combined_content = []
    for line in main_content:
        combined_content.append(line)
        if line.strip().startswith(r'\include{'):
            section_name = line.strip()[9:-1]  # Extract the section name
            section_file = os.path.join(main_folder, f"{section_name}.tex")
            if os.path.exists(section_file):
                with open(section_file, 'r') as sf:
                    section_content = sf.read()
                    combined_content.append(section_content + '\n')
            else:
                print(f"Warning: Section file {section_file} not found.")

    with open(output_file, 'w') as of:
        of.writelines(combined_content)


if __name__ == "__main__":
    main_file = 'main.tex'
    main_folder = r'C:/Users/alexsc31/Documents_privat/FH Campus/Clinical_Engineering/GithubRepo/Skriptum_Grundlagen_Physik_FH-Campus/'
    output_file = 'combined_main.tex'

    
    combine_latex_files(main_folder, main_file, output_file)