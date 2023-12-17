# Specify the base image
FROM node:16

# Set the working directory in the Docker image
WORKDIR /backend

# Copy the application files to the working directory
COPY ./backend .

# Export port 3000
EXPOSE 4000

# Run the application
CMD ["node", "app.js"]