from passlib.context import CryptContext
import requests
import random


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Generate():
     
    @staticmethod
    def random_color():
        # Generates random hex value for the color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

    @staticmethod
    def random_cat():
        # Generates link to random cat picture
        try:
            response = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5)
            return response.json()[0]['url']
        except Exception as e: # Api is down
            print(e)
            return "https://miramarvet.com.au/wp-content/uploads/2021/08/api-cat2.jpg"


    @staticmethod
    def hashed_password(password: str) -> str:
        return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)

