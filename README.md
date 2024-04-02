## Recipe Mixer
> Recipe Mixer is an AI-powered web application that encourages culinary exploration through recipe remixing. Users can input a recipe or list ingredients they have on hand, and the application utilizes the Gemini Pro model to suggest alternative ingredients based on flavor profiles and user preferences, including dietary restrictions.

### Why use Recipe Mixer?
Recipe Mixer is a user-friendly web application that helps you find delicious recipes based on the ingredients you have on hand. Whether you're a busy parent, a cooking enthusiast, or someone with dietary restrictions, Recipe Mixer makes meal planning easy and enjoyable.
All you need to do is input the ingredients you have in your kitchen and specify any dietary preferences you may have, such as vegetarian or gluten-free. Recipe Mixer then suggests personalized recipe options that match your input. It even offers alternative ingredient suggestions and can adapt recipes to different cultural cuisines, so you can explore new flavors and cooking styles.
With Recipe Mixer, you no longer have to worry about what to cook for dinner or how to use up leftover ingredients. It's like having a personal chef at your fingertips, ready to inspire you with creative and delicious meal ideas.

### Features:
- Ingredient Matching: Users can input a list of ingredients they have on hand, and the application suggests recipes based on those ingredients.
- Dietary Preferences: Users can specify dietary preferences such as vegetarian, vegan, or gluten-free, and the suggested recipes take these preferences into account.
- Alternative Ingredient Suggestions: The application suggests alternative ingredients based on flavor profiles and dietary preferences, allowing users to experiment with different ingredients.
- Cultural Adaptation: The suggested recipes can be adapted to different cultural cuisines, promoting culinary exploration and diversity.

### Dependencies:
- Gemini Pro LLM: Natural language processing model for text classification.
- Streamlit: Web application framework for building interactive web applications.
- Google Generative AI: Integrates advanced AI capabilities into the application.
- python-dotenv: python-dotenv is a Python library that allows you to read environment variables from .env files.
- langchain.llms: langchain.llms is a library used to interact with language models, particularly for text generation tasks.

### Installation:

Clone the repository:
```
git clone https://github.com/Gitesh08/recipe-mixer.git
```

Navigate to the project directory:
```
cd cd recipe-mixer
```

Create a Python virtual environment:
```
python -m virtualenv . 
```

Activate venv:
```
.\scripts\activate
```

Install the required dependencies:
```
pip install -r requirements.txt
```
Ensure all dependencies are installed.

Set up environment variables by creating a .env file and adding your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

Run the Streamlit application:
```
streamlit run app.py
```

### Usage
- Input your ingredients: Enter a list of ingredients you have on hand, separated by commas.
- Specify dietary preferences (optional): Select your dietary preferences from the dropdown menu.
- Click the "Suggest me recipe" button to receive recipe suggestions.
- Explore alternative ingredient suggestions and recipe options.
- Enjoy experimenting with different recipes and ingredients!


### Contributing :handshake:
Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or submit a pull request.


### License
This project is licensed under the MIT License.
