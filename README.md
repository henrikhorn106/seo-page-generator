# SEO Page Generator

A simple and efficient script for programmatically generating SEO-optimized web pages at scale. This tool helps create landing pages with targeted keywords, structured content, and proper meta tags to improve search engine visibility.

## Overview

The SEO Page Generator automates the creation of multiple web pages optimized for search engines. It's particularly useful for:

- Creating location-based landing pages
- Generating service-specific pages
- Building keyword-targeted content pages
- Scaling content production for SEO campaigns

## Features

- **Bulk Page Generation**: Create hundreds or thousands of pages from templates
- **Template-Based**: Use customizable HTML templates with placeholder variables
- **SEO Optimization**: Automatically generates meta titles, descriptions, and structured content
- **Keyword Integration**: Dynamically insert keywords and variations throughout pages
- **Scalable**: Generate pages efficiently with minimal manual intervention

## Installation

1. Clone the repository:
```bash
git clone https://github.com/henrikhorn106/seo-page-generator.git
cd seo-page-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the script with your configuration:

```bash
python generate_pages.py
```

### Configuration

Configure your page generation settings by editing the configuration file or passing parameters:

- **Templates**: Define HTML templates with placeholders
- **Keywords**: Specify target keywords and variations
- **Output Directory**: Set where generated pages will be saved
- **Meta Data**: Configure title patterns, descriptions, and other SEO elements

### Example

```python
# Example configuration
config = {
    'template': 'template.html',
    'keywords': ['service', 'location', 'industry'],
    'output_dir': 'generated_pages/',
    'title_pattern': '{service} in {location} | Company Name'
}
```

## Template Structure

Create HTML templates with placeholder variables:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <meta name="description" content="{{description}}">
</head>
<body>
    <h1>{{heading}}</h1>
    <p>{{content}}</p>
</body>
</html>
```

## Best Practices

- **Quality Over Quantity**: Focus on creating valuable, unique content
- **Avoid Duplicate Content**: Ensure each generated page has unique content
- **User Intent**: Design pages that serve real user needs, not just search engines
- **Regular Updates**: Keep content fresh and relevant
- **Compliance**: Follow search engine guidelines to avoid penalties

## Project Structure

```
seo-page-generator/
├── generate_pages.py       # Main script
├── templates/              # HTML templates
├── config/                 # Configuration files
├── data/                   # Input data (keywords, locations, etc.)
├── output/                 # Generated pages
└── requirements.txt        # Python dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Important Notes

⚠️ **SEO Best Practices**: This tool should be used responsibly. Creating low-quality or duplicate content can harm your website's search rankings. Always prioritize:
- Unique, valuable content
- User experience
- Compliance with search engine guidelines
- Ethical SEO practices

## License

This project is open source and available under the MIT License.

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

**Disclaimer**: This tool is intended for legitimate SEO purposes. Users are responsible for ensuring their generated content complies with search engine guidelines and provides genuine value to users.
