**Project Description:**
Create a weather forecast application that allows users to get current weather conditions and forecasts for a specific location using a weather API. This project will involve making API requests, processing JSON data, and presenting the information in a user-friendly way.

**Features:**

1. **User Input:**

   1. The user can enter the name of a city or provide latitude and longitude coordinates to get weather information for that location.
   2. The user should also have the option to save the requested results to a file. The filename does not matter, but ideally, the user should be able to pick the name of the file.

2. **API Integration:** Use [OpenWeather](https://openweathermap.org/api/geocoding-api) to fetch weather data for the specified location. They allow 1000 free API calls per day, so you should be able to test your application multiple times. You will need to sign up for a free account to get an API key.

3. **Data Parsing:** Process the JSON data received from the API response to extract relevant information such as current temperature, humidity, wind speed, and weather conditions. You can choose what kind of data you want to display to the user, but pick at least 3-4 relevant data points.

4. **Display:** Present the weather information to the user in a clear and organized manner. You can display the current conditions, as well as a forecast for the upcoming days. This is just a text-based application, so you don't need to worry about fancy graphics. You can use ASCII art or simple text formatting to make the output more readable.

5. ** Basic Error Handling:** Implement error handling to account for cases where the API request fails or the user provides invalid input.

6. **User-Friendly Interface:** This will be a CLI app.

Remember to review the documentation of the chosen API to understand how to structure your requests and handle the responses! You have a lot of freedom to choose what kind of data you actually want to show the user, so remember to pick things that are useful and interesting. Happy Coding!
