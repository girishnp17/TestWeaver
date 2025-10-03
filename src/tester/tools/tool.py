from crewai_tools import FileReadTool, DirectoryReadTool, CodeInterpreterTool

# Initialize your tools
file_reader = FileReadTool()
directory_reader = DirectoryReadTool()
code_interpreter = CodeInterpreterTool()