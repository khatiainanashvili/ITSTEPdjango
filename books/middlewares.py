import time
import logging



logging.basicConfig(
    filename="requests.log", 
    level=logging.INFO,  
    format="%(asctime)s - %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time() 
        response = self.get_response(request)  
        end_time = time.time() 

        duration = end_time - start_time 

        log_message = f"Request URL: {request.path} | Processing Time: {duration:.4f} sec"
        logging.info(log_message) 
        
        return response
