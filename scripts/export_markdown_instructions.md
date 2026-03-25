Export Markdown - Usage & prerequisites for `export_markdown.ps1`

Prerequisite
- Install Pandoc (Windows): https://pandoc.org/installing.html
  - Download the Windows installer (.msi/.exe) and install, or download `pandoc.exe` and place it in a local folder (for example `C:\tools\pandoc` or `%USERPROFILE%\bin`).

Add Pandoc to your PATH

- Manually: Open "Local Environment Variables" and add the folder containing `pandoc.exe` to the PATH variable.

- Temporary (current PowerShell session):

  $env:Path += ";C:\path\to\pandoc"

- Permanent (current user):

  [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\path\to\pandoc", "User")

  After updating the PATH, restart PowerShell or open a new terminal so the change takes effect.

Verify installation
- Run `pandoc --version` in PowerShell. You should see the installed pandoc version.

Using the script
- Run the script from the repository root in PowerShell. 

Example:
```PowerShell
  .\scripts\export_markdown.ps1 -SourcePath .\ddemm\mpt\docs\minimal_optional_infrastructure_req.md -Formats docx
```

- `-SourcePath` should point to the Markdown file to convert. `-Formats` specifies the output format(s) (e.g., `docx`, `pdf`, `html`).

Notes
- The script calls `pandoc` under the hood. Ensure `pandoc` is available on the PATH before running the script.
- For PDF output, additional tools (like a LaTeX distribution) may be required depending on your pandoc configuration.

If anything here should be expanded or adjusted to match environment specifics, tell me which item to update.
