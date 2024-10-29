# run_docker.ps1

# Define variables
$imageName = "opencv_project"
$containerName = "opencv_container"

# Authentication
docker login

# Build the Docker image
docker build -t $imageName .

# Run the Docker container
docker run --name $containerName $imageName

# Check for errors
if ($LASTEXITCODE -ne 0) {
    Write-Host "There was an error running the container."
    exit 1
}

# Optionally, you can stop and remove the container afterward
docker stop $containerName
docker rm $containerName

Write-Host "Execution completed successfully!"