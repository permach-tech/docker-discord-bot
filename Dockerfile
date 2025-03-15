# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy bot script
COPY bot.py .

# Install dependencies
RUN pip install discord.py

# Set environment variable for token (use `docker run -e DISCORD_BOT_TOKEN=your_token`)
ENV DISCORD_BOT_TOKEN=""

# Run the bot
CMD ["python", "bot.py"]