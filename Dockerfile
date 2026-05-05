# Use official Odoo image as base
FROM odoo:16.0

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
USER root
RUN apt-get update && apt-get install -y \
    git \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy module to addons directory
COPY . /mnt/extra-addons/to_do_odoo_task

# Install Python requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set working directory
WORKDIR /mnt/extra-addons/to_do_odoo_task

# Return to odoo user
USER odoo

# Expose port
EXPOSE 8069 8072

# Run Odoo
CMD ["odoo", "--addons-path=/mnt/extra-addons"]
