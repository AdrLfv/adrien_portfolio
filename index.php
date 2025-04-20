<?php
// This PHP wrapper allows running Flask-like applications on shared PHP hosting

// Define the base URL (adjust as needed for your Hostinger setup)
$base_url = "https://" . $_SERVER["HTTP_HOST"] . "/";

// Function to get the correct template file based on the URL path
function get_template_file($uri) {
    // Remove query parameters
    $uri = strtok($uri, '?');
    
    // Default to index
    if ($uri == "/" || $uri == "") {
        return "static_html/index.html";
    }
    
    // Clean the URI
    $uri = ltrim($uri, '/');
    
    // Project detail pages handling
    if (preg_match('/^project\/(\d+)$/', $uri, $matches)) {
        return "static_html/project_" . $matches[1] . ".html";
    }
    
    // Map routes to static HTML files
    $routes = [
        'about' => 'static_html/about.html',
        'cv' => 'static_html/cv.html',
        'contact' => 'static_html/contact.html'
    ];
    
    if (isset($routes[$uri])) {
        return $routes[$uri];
    }
    
    // File not found
    return "static_html/404.html";
}

// Get the URI
$request_uri = $_SERVER['REQUEST_URI'];
$uri_path = parse_url($request_uri, PHP_URL_PATH);

// Determine which file to serve
$file_to_serve = get_template_file($uri_path);

// Check if file exists
if (file_exists($file_to_serve)) {
    // Set content type based on file extension
    $extension = pathinfo($file_to_serve, PATHINFO_EXTENSION);
    switch ($extension) {
        case 'html':
            header('Content-Type: text/html');
            break;
        case 'css':
            header('Content-Type: text/css');
            break;
        case 'js':
            header('Content-Type: application/javascript');
            break;
        case 'json':
            header('Content-Type: application/json');
            break;
        default:
            header('Content-Type: text/plain');
    }
    
    // Serve the file
    include($file_to_serve);
} else {
    // File not found, return 404
    header("HTTP/1.0 404 Not Found");
    include("static_html/404.html");
}
?>
