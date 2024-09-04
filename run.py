
import requests

# Define the login URL and payload with your username and password
login_url = "https://www.facebook.com/login.php"
payload = {
    'email': 'tariful404@gmail.com',
    'pass': 'mr.rakib hossen'
}

# Send the POST request to the login URL
with requests.Session() as session:
    response = session.post(login_url, data=payload)
    
    # Check if the login was successful by checking the response content
    if "login" in response.url:
        print("Login failed. Please check your username and password.")
    else:
        print("Login successful!")

    # Optionally, you can continue to interact with the session
    # to perform further requests while authenticated.