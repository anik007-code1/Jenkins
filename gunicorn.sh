#!/bin/bash

# Activate the Python virtual environment
source venv/bin/activate

# Navigate to the application directory
cd /var/lib/jenkins/workspace/django_cicd/app || exit 1

# Run Django migrations
if python3 manage.py makemigrations && python3 manage.py migrate; then
    echo "Migrations done"
else
    echo "Migrations failed!" >&2
    exit 1
fi

# Collect static files
if python3 manage.py collectstatic --no-input; then
    echo "Static files collected."
else
    echo "Collecting static files failed!" >&2
    exit 1
fi

# Navigate to the project directory
cd /var/lib/jenkins/workspace/django_cicd || exit 1

# Copy Gunicorn socket and service files
if sudo cp -rf gunicorn.socket /etc/systemd/system/ && sudo cp -rf gunicorn.service /etc/systemd/system/; then
    echo "Service files copied."
else
    echo "Failed to copy service files!" >&2
    exit 1
fi

# Reload the systemd manager configuration
if sudo systemctl daemon-reload; then
    echo "Systemd daemon reloaded."
else
    echo "Failed to reload systemd daemon!" >&2
    exit 1
fi

# Start Gunicorn
if sudo systemctl start gunicorn; then
    echo "Gunicorn has started."
else
    echo "Failed to start Gunicorn!" >&2
    exit 1
fi

# Enable Gunicorn to start on boot
if sudo systemctl enable gunicorn; then
    echo "Gunicorn has been enabled."
else
    echo "Failed to enable Gunicorn!" >&2
    exit 1
fi

# Restart Gunicorn (if necessary)
if sudo systemctl restart gunicorn; then
    echo "Gunicorn has been restarted."
else
    echo "Failed to restart Gunicorn!" >&2
    exit 1
fi

# Display the status of Gunicorn
sudo systemctl status gunicorn
