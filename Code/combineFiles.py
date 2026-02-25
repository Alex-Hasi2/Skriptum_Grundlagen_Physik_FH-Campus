# A script to insert the content of the latex .tex files into the main.tex file 
# At the locations in the main.tex file where there are \include{filename} commands, the content of filename.tex file should be inserted. 


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
        combined_content.append(line)
        if line.strip().startswith(r'\include{'):
            section_name = line.strip()[9:-1]  # Extract the section name
            section_file = os.path.join(main_folder, f"{section_name}.tex")
            if os.path.exists(section_file):
                print(f"Inserting content from {section_file}")
                with open(section_file, 'r') as sf:
                    section_content = sf.read()
                    # Insert comment % Start of <filename.tex> before the content and a comment % End of <filename.tex> after the content
                    combined_content.append(f"% ---- Start of {section_name}.tex\n") 
                    combined_content.append(section_content + '\n')
                    combined_content.append(f"% ---- End of {section_name}.tex\n")
            else:
                print(f"Warning: Section file {section_file} not found.")

    with open(output_file, 'w') as of:
        of.writelines(combined_content)


if __name__ == "__main__":
    main_file = 'main.tex'
    # main_folder = r'C:/Users/alexsc31/Documents_privat/FH Campus/Clinical_Engineering/GithubRepo/Skriptum_Grundlagen_Physik_FH-Campus/'
    main_folder = r'C:/Users/Alexa/Documents-Alex/FH Campus/Skriptum_Grundlagen_Physik_FH-Campus/'
    output_file = 'combined_main_2026-02-25.tex'

    
    combine_latex_files(main_folder, main_file, output_file)