import re
import codecs

def delete_html_tags(html_file, result_file='cleaned_2.txt'):
    html = codecs.open(html_file, 'r', 'utf-8').readlines()
    cleaned_text = []
    for line in html:
        cleaned_line = re.sub('<.*?>', '', line)
        if cleaned_line.strip():
            cleaned_text.append(cleaned_line)
    with open(result_file, "w") as output:
         output.write(''.join(cleaned_text))

    return cleaned_text


html_file = "draft.html"
print(delete_html_tags(html_file, result_file='cleaned_2.txt'))







