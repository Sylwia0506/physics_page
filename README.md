# Physics Learning Platform

A web application for learning physics, featuring interactive content and exam preparation materials.

## Features

- Interactive physics topics
- Matura exam preparation materials
- Polish language support
- Mobile-responsive design

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/maths_page.git
cd maths_page
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

The application will be available at http://localhost:5000

## Production Deployment

This application is configured for production deployment on Render.com.

### Deployment Steps

1. Create an account on [Render](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service
4. Select your repository
5. Render will automatically detect the configuration from `render.yaml`

### Production Configuration

The application uses the following production settings:
- Gunicorn as the WSGI server
- 4 worker processes
- 4 threads per worker
- 120-second timeout
- Python 3.9.0

### Environment Variables

No additional environment variables are required for basic deployment.

## Project Structure

```
maths_page/
├── app.py              # Main application file
├── settings.py         # Application settings
├── requirements.txt    # Python dependencies
├── gunicorn_config.py  # Production server configuration
├── render.yaml         # Render deployment configuration
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
└── scraper.py         # Data scraping utilities
```

## Technologies Used

- Python 3.9+
- Flask
- Gunicorn
- HTML/CSS/JavaScript
- BeautifulSoup4 (for data scraping)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 