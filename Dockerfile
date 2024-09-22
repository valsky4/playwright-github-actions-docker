# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required by Playwright
RUN apt-get update && \
    apt-get install -y wget gnupg libnss3 libxss1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 \
    libdrm2 libgbm1 libgtk-3-0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libxshmfence1 xdg-utils

# Install Playwright dependencies
RUN pip install pytest-playwright pytest-html

# Install Playwright browsers
RUN playwright install --with-deps

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port if you need to view reports via a web server (optional)
# EXPOSE 8000

# Command to run when the container starts
CMD ["pytest", "-m", "webtest", "--html=test-results/web-report.html", "--self-contained-html"]
