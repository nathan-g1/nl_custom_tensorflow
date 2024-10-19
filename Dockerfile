# Use the NVIDIA TensorFlow base image
FROM nvcr.io/nvidia/tensorflow:24.09-tf2-py3

# Set the working directory
WORKDIR /workspace

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888

# Set the default command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=afa95ad5cb07bc2b3f0d9b711cade7479362a3950bc4fe16"]

