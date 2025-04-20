from flask import Flask, render_template, url_for, abort
from datetime import datetime

app = Flask(__name__)

# Project data
projects = [
    {
        'id': 1,
        'title': 'Augmented Mirror',
        'description': 'An interactive augmented reality mirror that responds to user movements and gestures.',
        'image': 'old_project_1.gif',
        'long_description': 'The Augmented Mirror project is an interactive installation that uses computer vision to track user movements and create responsive visual effects. Users can interact with virtual elements that respond to their gestures, creating an engaging and playful experience.',
        'technologies': ['Augmented Reality', 'Computer Vision', 'Motion Tracking'],
        'github_link': '',
        'live_demo': '',
        'year': 2022,
        'content_sections': [
            {
                'type': 'text',
                'title': 'Project Overview',
                'content': 'The Augmented Mirror project is an interactive installation that uses computer vision to track user movements and create responsive visual effects. Users can interact with virtual elements that respond to their gestures, creating an engaging and playful experience.'
            },
            {
                'type': 'image',
                'title': 'Project Demo',
                'content': 'old_project_1.gif',
                'caption': 'A demonstration of the Augmented Mirror in action'
            },
            {
                'type': 'text',
                'title': 'Technical Challenges',
                'content': 'One of the main challenges was implementing real-time motion tracking that could respond to subtle movements while maintaining smooth visual effects. This required optimizing the computer vision algorithms and creating efficient rendering pipelines.'
            },
            {
                'type': 'youtube',
                'title': 'Video Presentation',
                'content': 'dQw4w9WgXcQ',  # YouTube video ID
                'caption': 'Video demonstration of the Augmented Mirror project'
            }
            # Add more sections as needed
        ]
    },
    {
        'id': 2,
        'title': 'Augmented Reality Communication',
        'description': 'A system that enhances communication through augmented reality interfaces and visual overlays.',
        'image': 'old_project_2.gif',
        'long_description': 'This project explores how augmented reality can enhance communication by providing visual context and information overlays. It includes features for remote collaboration, information sharing, and interactive presentations.',
        'technologies': ['Augmented Reality', 'Communication Systems', 'User Interface Design'],
        'github_link': '',
        'live_demo': '',
        'year': 2021,
        'content_sections': [
            {
                'type': 'text',
                'title': 'Project Overview',
                'content': 'This project explores how augmented reality can enhance communication by providing visual context and information overlays. It includes features for remote collaboration, information sharing, and interactive presentations.'
            },
            {
                'type': 'image',
                'title': 'System Interface',
                'content': 'old_project_2.gif'
            },
            {
                'type': 'text',
                'title': 'Key Features',
                'content': 'The system includes real-time annotation capabilities, spatial awareness for placing virtual objects in physical spaces, and intuitive gesture controls for manipulating digital content during presentations.'
            }
            # Add more sections as needed
        ]
    },
    {
        'id': 3,
        'title': 'Cairn Candle',
        'description': 'An innovative product design combining traditional candles with modern technology and aesthetics.',
        'image': 'old_project_3.gif',
        'long_description': 'Cairn Candle is a product design project that reimagines the traditional candle with a modern, minimalist aesthetic. The design draws inspiration from cairns - stacked stone formations used as landmarks - creating a unique and elegant lighting solution.',
        'technologies': ['Product Design', 'Industrial Design', '3D Modeling'],
        'github_link': '',
        'live_demo': '',
        'year': 2020,
        'content_sections': []
    },
    {
        'id': 4,
        'title': 'Dynamic Training in AR for Musical Practice',
        'description': 'An augmented reality application that helps musicians improve their skills through interactive training.',
        'image': 'old_project_4.gif',
        'long_description': 'This project uses augmented reality to create an immersive and interactive training environment for musicians. It provides real-time feedback, guided exercises, and visualization tools to enhance musical practice and learning.',
        'technologies': ['Augmented Reality', 'Audio Processing', 'Music Education'],
        'github_link': '',
        'live_demo': '',
        'year': 2019,
        'content_sections': []
    },
    {
        'id': 5,
        'title': 'Image Processing Software',
        'description': 'Advanced software for image analysis, processing, and enhancement with multiple specialized features.',
        'image': 'old_project_5.gif',
        'long_description': 'This image processing software provides powerful tools for analyzing and manipulating digital images. It includes features for filtering, enhancement, segmentation, and feature extraction, with applications in research, medical imaging, and creative work.',
        'technologies': ['Computer Vision', 'Software Development', 'Image Analysis'],
        'github_link': '',
        'live_demo': '',
        'year': 2019,
        'content_sections': []
    },
    {
        'id': 6,
        'title': 'Industrial Sorting Circuit and Robotic',
        'description': 'An automated system for industrial sorting using robotics, computer vision, and custom circuitry.',
        'image': 'old_project_6.gif',
        'long_description': 'This project combines robotics, computer vision, and custom electronic circuits to create an efficient industrial sorting system. It can identify, categorize, and sort various objects based on their visual characteristics and physical properties.',
        'technologies': ['Robotics', 'Computer Vision', 'Electronics'],
        'github_link': '',
        'live_demo': '',
        'year': 2018,
        'content_sections': []
    },
    {
        'id': 7,
        'title': 'Interactive Avatar with Pose Estimation',
        'description': 'A system that creates responsive digital avatars that mirror human movements using pose estimation.',
        'image': 'old_project_7.gif',
        'long_description': 'This project uses advanced pose estimation algorithms to create interactive digital avatars that respond to human movements in real-time. The system can track body positions and translate them into animated character movements with high accuracy.',
        'technologies': ['Motion Tracking', 'Computer Vision', 'Animation'],
        'github_link': '',
        'live_demo': '',
        'year': 2018,
        'content_sections': []
    },
    {
        'id': 8,
        'title': 'Interactive Musical Score',
        'description': 'A digital musical score system that responds to performers and enhances the musical experience.',
        'image': 'old_project_8.gif',
        'long_description': 'The Interactive Musical Score project reimagines traditional sheet music as a dynamic, responsive digital interface. It follows performers in real-time, providing adaptive visual cues and can adjust to tempo changes and improvisation.',
        'technologies': ['Audio Processing', 'User Interface Design', 'Music Technology'],
        'github_link': '',
        'live_demo': '',
        'year': 2017,
        'content_sections': []
    },
    {
        'id': 9,
        'title': 'Master Thesis',
        'description': 'Research work focused on innovative applications of augmented reality in educational contexts.',
        'image': 'old_project_9.gif',
        'long_description': 'This master thesis explores the potential of augmented reality technologies to transform educational experiences. The research includes theoretical frameworks, prototype development, and user studies to evaluate the effectiveness of AR-based learning tools.',
        'technologies': ['Augmented Reality', 'Educational Technology', 'Research Methods'],
        'github_link': '',
        'live_demo': '',
        'year': 2017,
        'content_sections': []
    },
    {
        'id': 10,
        'title': 'Miniature suspended tramway',
        'description': 'A scale model of an automated suspended tramway system with functional components.',
        'image': 'old_project_10.gif',
        'long_description': 'This engineering project involved designing and building a fully functional miniature suspended tramway system. It includes automated controls, scale infrastructure, and demonstrates principles of transportation engineering and mechatronics.',
        'technologies': ['Mechanical Engineering', 'Electronics', 'Scale Modeling'],
        'github_link': '',
        'live_demo': '',
        'year': 2016,
        'content_sections': []
    },
    {
        'id': 11,
        'title': 'Sign Language Recognition Module',
        'description': 'Software that recognizes and interprets sign language gestures using computer vision technology.',
        'image': 'old_project_11.gif',
        'long_description': 'This project uses machine learning and computer vision to recognize and interpret sign language gestures. The system can translate signs into text or speech in real-time, helping to bridge communication gaps between signing and non-signing individuals.',
        'technologies': ['Machine Learning', 'Computer Vision', 'Accessibility Technology'],
        'github_link': '',
        'live_demo': '',
        'year': 2015,
        'content_sections': []
    },
    {
        'id': 12,
        'title': 'Sign Language Video Game in Augmented Reality',
        'description': 'An educational game that teaches sign language through interactive augmented reality experiences.',
        'image': 'old_project_12.gif',
        'long_description': 'This innovative video game combines augmented reality with sign language education to create an engaging learning experience. Players interact with virtual characters using sign language gestures, receiving feedback and progressing through educational challenges.',
        'technologies': ['Augmented Reality', 'Game Development', 'Sign Language'],
        'github_link': '',
        'live_demo': '',
        'year': 2014,
        'content_sections': []
    },
]

# Context processor to make current year available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Routes
@app.route('/')
def index():
    # Sort projects by year in descending order (newest first)
    sorted_projects = sorted(projects, key=lambda x: x['year'], reverse=True)
    return render_template('index.html', projects=sorted_projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project/<int:project_id>')
def project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        abort(404)
    return render_template('project.html', project=project)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
