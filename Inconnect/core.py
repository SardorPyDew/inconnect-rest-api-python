import logging
import requests

class PyInconnect:
    API_URL = "https://api.inconnect.uz/api/rest-api/"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        self.logger = self.__setup_logger()
    
    def __setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(levelname)-8s [%(asctime)s]  %(message)s'))
        logger.addHandler(ch)
        return logger
    
    def __send_request(self, endpoint, method='POST', data=None, params=None):
        url = f"{self.API_URL}{endpoint}"
        print(url)
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params)
            else:
                response = requests.post(url, headers=self.headers, json=data)
                
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            return {"error": str(e)}

    def send_email(self, name, from_email, to_email, subject, message):
        if not all([name, from_email, to_email, subject, message]):
            return {"error": "Missing required fields"}

        email_data = {
            "name": name,
            "from_email": from_email,
            "to_email": to_email,
            "subject": subject,
            "message": message
        }

        return self.__send_request('send/', 'POST', email_data)

    def send_email_with_template(self, from_email, from_name, to_email, subject, template_id, variables):
        if not all([from_email, from_name, to_email, subject, template_id]):
            return {"error": "Missing required fields"}

        email_data = {
            'from': {'email': from_email, 'name': from_name},
            'to': [{'email': to_email}],
            'subject': subject,
            'template': {'id': template_id, 'variables': variables}
        }
        return self.__send_request('send_template/', 'POST', email_data)

    def get_emails(self, limit=10, offset=0, date_from=None, date_to=None, sender=None, recipient=None):
        params = {
            'limit': limit,
            'offset': offset,
            'date_from': date_from,
            'date_to': date_to,
            'sender': sender,
            'recipient': recipient
        }
        return self.__send_request('emails/', 'GET', params=params)

    def get_email_by_id(self, email_id):
        if not email_id:
            return {"error": "Empty email ID"}
        return self.__send_request(f"emails/{email_id}", 'GET')

    def add_to_unsubscribe_list(self, emails):
        if not emails:
            return {"error": "Empty email list"}
        return self.__send_request('unsubscribe/', 'POST', {'emails': emails})

    def remove_from_unsubscribe_list(self, emails):
        if not emails:
            return {"error": "Empty email list"}
        return self.__send_request('unsubscribe/', 'DELETE', {'emails': emails})

    def get_ip_list(self):
        return self.__send_request('ips/', 'GET')

    def get_allowed_domains(self):
        return self.__send_request('domains/', 'GET')

    def add_domain(self, email):
        if not email:
            return {"error": "Empty email"}
        return self.__send_request('domains/', 'POST', {'email': email})

    def verify_domain(self, email):
        if not email:
            return {"error": "Empty email"}
        return self.__send_request(f'domains/{email}/verify', 'GET')
