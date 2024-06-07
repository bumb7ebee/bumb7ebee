# src/main.py
from datetime import datetime
import pytz
import re

README_PATH = "README.md"
TIME_TEMPLATE='<p align="center">This <i>README</i> file is generated <b>every 3 hours</b>!<br>Last refresh: {}</p>'

def prepare_template(time):
    global TIME_TEMPLATE
    TIME_TEMPLATE = TIME_TEMPLATE.format(time)

def refresh_contents(old_content, new_content):
    r = re.compile(r'<!\-\- TIME:START \-\->((.|\n)*)<!\-\- TIME:END \-\->', re.DOTALL)
    new_content_formated = '<!-- TIME:START -->\n{}\n<!-- TIME:END -->'.format(new_content)
    return r.sub(new_content_formated, old_content)

def main():
    timeZ_Ist = pytz.timezone('Europe/Istanbul')
    dt_Ist = datetime.now(timeZ_Ist)
    dtf_Ist = dt_Ist.strftime('%A, %b %-d, %H:%M (GMT%z)')

    prepare_template(dtf_Ist)

    with open(README_PATH, 'r', encoding='utf-8') as fr:
        readme = fr.read()

    readme_new = refresh_contents(readme, TIME_TEMPLATE)

    with open(README_PATH, mode="w", encoding="utf-8") as fw:
        fw.write(readme_new)

if __name__ == "__main__":
    main()
