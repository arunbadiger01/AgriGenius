import os
import re

html_file = r"c:\Users\Hp\Downloads\cybersecurity_project.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

css_match = re.search(r"<style>\s*(.*?)\s*</style>", content, re.DOTALL)
if css_match:
    css = css_match.group(1)
    with open(r"c:\Users\Hp\Downloads\style.css", "w", encoding="utf-8") as f:
        f.write(css)
    content = re.sub(r"<style>.*?</style>", '<link rel="stylesheet" href="style.css">', content, flags=re.DOTALL)

js_match = re.search(r"<script>\s*(.*?)\s*</script>", content, re.DOTALL)
if js_match:
    js = js_match.group(1)
    with open(r"c:\Users\Hp\Downloads\script.js", "w", encoding="utf-8") as f:
        f.write(js)
    content = re.sub(r"<script>.*?</script>", '<script src="script.js"></script>', content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)
