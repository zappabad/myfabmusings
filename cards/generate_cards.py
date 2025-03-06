import os
import json
from jinja2 import Environment, FileSystemLoader

BASE_DIR = 'editions'
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'output'

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template('cards_template.html')

def collect_card_data(base_dir):
    editions = []
    for edition_name in sorted(os.listdir(base_dir)):
        edition_path = os.path.join(base_dir, edition_name)
        if os.path.isdir(edition_path):
            edition = {
                'name': edition_name.replace('_', ' '),
                'icon': os.path.join(edition_path, 'icon.png'),
                'cards': []
            }
            for file in sorted(os.listdir(edition_path)):
                if file.lower().endswith('.json'):
                    with open(os.path.join(edition_path, file), 'r') as f:
                        card = json.load(f)
                        edition['cards'].append(card)
            editions.append(edition)
    return editions

if __name__ == "__main__":
    data = collect_card_data(BASE_DIR)
    rendered_html = template.render(editions=data)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, 'index.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f"HTML generated successfully: {output_file}")
