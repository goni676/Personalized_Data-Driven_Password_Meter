# Personalized Data-Driven Password Meter
Due to size limitations, the source code can be found [HERE](https://drive.google.com/file/d/1VRcfzOMCP8umvjfgPeT-CHRRhqzPX7KT/view?usp=share_link).
* Country-based personalized data-driven password meter, based on [PESrank model](https://github.com/lirondavid/PESrank).
* repository link: https://github.com/goni676/spp_password_meter

## Installation
* Unzip PPESrank-master into a directory of your choise.
* Run:
  ```bash
  pip install -r requirements.txt
  ```
## Run the Python Server
* In the terminal or command prompt, navigate to your project folder and run the Python server:
  ```bash
  python app.py
  ```
* You should see output indicating that the Flask development server is running.
  Here's an example of what the terminal output might look like:
  ```bash
   * Serving Flask app "app" (lazy loading)
   * Environment: development
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```
## Accessing the Flask Application
* Once you see this output, your Flask server is up and running and ready to handle incoming HTTP requests.
* To access the Flask application, open a web browser and enters the URL of the application in the address bar.
  This URL typically consists of the host and port where your Flask server is running (e.g., http://127.0.0.1:5000/ or http://localhost:5000/).

## Flask Application Illustration
In the following [video](https://app.usebubbles.com/rcwAKvEDhag61BCBnMADBR), you can witness the process of entering the password "Chelsea" within a country that lacks a corresponding model, initially set to 'Argentina' as the selected country. Subsequently, the video showcases the resulting score after changing the country to the UK, with 'Chelsea' recognized as one of the frequently used passwords.



