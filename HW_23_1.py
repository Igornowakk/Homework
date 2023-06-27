import re
import codecs

def delete_html_tags(html_file, result_file='cleaned_1.txt'):
    html = codecs.open(html_file, 'r', 'utf-8').readlines()
    cleaned_text = []
    for line in html:
            cleaned_text.append(re.sub('<.*?>', '', line))
    with open(result_file, "w") as output:
         output.write('\n'.join(cleaned_text))

    return cleaned_text


html_file = "draft.html"
print(delete_html_tags(html_file, result_file='cleaned_1.txt'))

