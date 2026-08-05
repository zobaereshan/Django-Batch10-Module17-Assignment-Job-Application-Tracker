from datetime import datetime


class RequestLoggerMiddleware:
    """
    Custom middleware that logs the timestamp, HTTP method, and requested
    path of every incoming request to the console.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        print("---------------------------------")
        print(f"Time   : {timestamp}")
        print(f"Method : {request.method}")
        print(f"Path   : {request.path}")
        print("---------------------------------")

        response = self.get_response(request)
        return response
