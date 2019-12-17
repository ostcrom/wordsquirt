from os.path import expanduser

HTML_HEAD_TEMPLATE = """
<html>
    <head>
        <title>WordSquirt Cheat Sheet</title>
    </head>
</html>
<body>
<h1>Cheat Sheet</h1>
"""

HTML_FOOT_TEMPLATE = """
</body>
</html>
"""

class CheatSheetGenerator():
    def __init__(self, output_location):
        self.output_location = output_location
        self.html_body = ""

    def add_entry(self, trigger, expansion):
        new_entry = f"""
        <h3>{trigger}</h3>
        <pre>{expansion}</pre>
        <hr>
        """
        self.html_body = self.html_body + new_entry

    def write_output(self):
        file_handle = open(self.output_location, "w")
        file_handle.write(HTML_HEAD_TEMPLATE)
        file_handle.write(self.html_body)
        file_handle.write(HTML_FOOT_TEMPLATE)
        file_handle.close()
