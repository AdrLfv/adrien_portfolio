import os
import re
import shutil
import glob
from bs4 import BeautifulSoup

# Dossier contenant les anciens projets
old_portfolio_dir = 'portfolio_old'
# Dossier où stocker les images des projets
projects_image_dir = 'static/images/projects'

# Créer le dossier des images de projets s'il n'existe pas
if not os.path.exists(projects_image_dir):
    os.makedirs(projects_image_dir)

# Liste pour stocker les données des projets
projects_data = []

# Fonction pour extraire le titre du projet depuis le nom de fichier
def extract_title_from_filename(filename):
    # Enlever le préfixe "Adrien LEFEVRE - " et l'extension ".html"
    title = filename.replace("Adrien LEFEVRE - ", "").replace(".html", "")
    return title

# Fonction pour trouver l'image principale d'un projet
def find_main_image(project_files_dir):
    # Chercher les images GIF et PNG
    image_files = glob.glob(os.path.join(project_files_dir, "*.gif"))
    if not image_files:
        image_files = glob.glob(os.path.join(project_files_dir, "*.png"))
    if not image_files:
        image_files = glob.glob(os.path.join(project_files_dir, "*.jpg"))
    
    # Prendre la plus grande image (en taille de fichier)
    if image_files:
        return max(image_files, key=os.path.getsize)
    return None

# Fonction pour extraire la description du projet
def extract_description(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Chercher les paragraphes qui pourraient contenir la description
    paragraphs = soup.find_all('p')
    
    # Prendre le premier paragraphe non vide comme description courte
    short_description = ""
    for p in paragraphs:
        text = p.get_text().strip()
        if text and len(text) > 20:  # Ignorer les paragraphes trop courts
            short_description = text
            break
    
    # Prendre tous les paragraphes pour la description longue
    long_description = ""
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            long_description += text + "\n\n"
    
    return short_description, long_description

# Parcourir les fichiers HTML des projets
project_files = glob.glob(os.path.join(old_portfolio_dir, "*.html"))

for i, project_file in enumerate(project_files, start=1):
    project_filename = os.path.basename(project_file)
    project_title = extract_title_from_filename(project_filename)
    
    # Lire le contenu du fichier HTML
    with open(project_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extraire la description
    short_desc, long_desc = extract_description(html_content)
    
    # Trouver l'image principale
    project_files_dir = project_file.replace(".html", "_files")
    main_image = find_main_image(project_files_dir)
    
    # Nom de fichier pour l'image dans le nouveau portfolio
    image_filename = f"old_project_{i}.{main_image.split('.')[-1]}" if main_image else "placeholder.jpg"
    
    # Copier l'image dans le dossier des projets
    if main_image:
        shutil.copy2(main_image, os.path.join(projects_image_dir, image_filename))
    
    # Déterminer les technologies utilisées (fictives pour l'instant)
    technologies = []
    if "AR" in project_title or "Augmented" in project_title:
        technologies.append("Augmented Reality")
    if "Mirror" in project_title:
        technologies.append("Computer Vision")
    if "Musical" in project_title or "Music" in project_title:
        technologies.append("Audio Processing")
    if "Recognition" in project_title:
        technologies.append("Machine Learning")
    if "Industrial" in project_title or "Robotic" in project_title:
        technologies.append("Robotics")
    if "Software" in project_title:
        technologies.append("Software Development")
    if "Avatar" in project_title or "Pose" in project_title:
        technologies.append("Motion Tracking")
    
    # Ajouter des technologies génériques si nécessaire
    if not technologies:
        technologies = ["Python", "C++", "Computer Vision"]
    
    # Créer l'entrée pour ce projet
    project_entry = {
        'id': i,
        'title': project_title,
        'description': short_desc[:150] + "..." if len(short_desc) > 150 else short_desc,
        'image': image_filename,
        'long_description': long_desc,
        'technologies': technologies,
        'github_link': '',  # À remplir manuellement plus tard
        'live_demo': '',    # À remplir manuellement plus tard
    }
    
    projects_data.append(project_entry)

# Générer le code Python pour mettre à jour app.py
projects_code = "# Project data\nprojects = [\n"

for project in projects_data:
    projects_code += "    {\n"
    projects_code += f"        'id': {project['id']},\n"
    projects_code += f"        'title': '{project['title']}',\n"
    
    # Échapper les apostrophes et les sauts de ligne dans les descriptions
    description = project['description'].replace("'", "\\'").replace("\n", " ")
    long_description = project['long_description'].replace("'", "\\'").replace("\n", " ")
    
    projects_code += f"        'description': '{description}',\n"
    projects_code += f"        'image': '{project['image']}',\n"
    projects_code += f"        'long_description': '{long_description}',\n"
    projects_code += f"        'technologies': {project['technologies']},\n"
    projects_code += f"        'github_link': '{project['github_link']}',\n"
    projects_code += f"        'live_demo': '{project['live_demo']}',\n"
    projects_code += "    },\n"

projects_code += "]\n"

# Écrire le code dans un fichier temporaire
with open('new_projects.py', 'w', encoding='utf-8') as f:
    f.write(projects_code)

print(f"Importation terminée ! {len(projects_data)} projets ont été importés.")
print("Les données des projets ont été écrites dans 'new_projects.py'.")
print("Vous pouvez maintenant copier ce contenu dans app.py pour remplacer la liste de projets existante.")
print("N'oubliez pas de générer le site statique avec 'python generate_static_site.py' après avoir mis à jour app.py.")
