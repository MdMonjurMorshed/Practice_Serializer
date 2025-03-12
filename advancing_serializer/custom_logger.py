import logging
import time

logger = logging.getLogger("api-logger")  # Create a logger for API requests

class CustomLoggerMiddleware:
    """Middleware to log API request details."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # Record request start time

        response = self.get_response(request)  # Process the request

        execution_time = round(time.time() - start_time, 3)  # Calculate execution time

        # Extract request details
        status_code = response.status_code
        method = request.method
        endpoint = request.path
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")

        # Log the request details
        logger.info(f"{endpoint} | {method} | {status_code} | {execution_time}s | {user_agent}")

        return response