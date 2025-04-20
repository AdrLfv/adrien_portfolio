import os
import re
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, BaseLoader
from app import projects

# Create static_html directory if it doesn't exist
static_html_dir = 'static_html'
if not os.path.exists(static_html_dir):
    os.makedirs(static_html_dir)

# Copy static assets to static_html directory
if os.path.exists('static'):
    static_dest = os.path.join(static_html_dir, 'static')
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree('static', static_dest)

# Define custom Jinja functions to replace Flask's helpers
class CustomEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(CustomEnvironment, self).__init__(*args, **kwargs)
        self.globals['url_for'] = self.url_for
    
    def url_for(self, endpoint, **kwargs):
        if endpoint == 'static':
            return f"static/{kwargs['filename']}"
        elif endpoint == 'index':
            return "index.html"
        elif endpoint == 'about':
            return "about.html"
        elif endpoint == 'cv':
            return "cv.html"
        elif endpoint == 'contact':
            return "contact.html"
        elif endpoint == 'project' and 'project_id' in kwargs:
            return f"project_{kwargs['project_id']}.html"
        return f"{endpoint}.html"

# Set up Jinja2 environment with custom functions
env = CustomEnvironment(loader=FileSystemLoader('templates'))

# Function to create static HTML files
def create_static_page(template_name, output_name, **kwargs):
    template = env.get_template(template_name)
    
    # Add current year to all templates
    if 'now' not in kwargs:
        kwargs['now'] = datetime.now()
    
    content = template.render(**kwargs)
    
    # Write to file
    output_path = os.path.join(static_html_dir, output_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

# Generate index page
create_static_page('index.html', 'index.html', projects=projects)

# Generate about page
create_static_page('about.html', 'about.html')

# Generate CV page
create_static_page('cv.html', 'cv.html')

# Generate contact page
create_static_page('contact.html', 'contact.html')

# Generate individual project pages
for project in projects:
    create_static_page('project.html', f'project_{project["id"]}.html', project=project)

# Generate 404 page
create_static_page('404.html', '404.html')

print("Static site generation complete!")
