import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import vertexai

PROJECT_ID = os.getenv("GCP_PROJECT")  # Your Google Cloud Project ID
LOCATION = os.getenv("GCP_REGION")  # Your Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Load environment variables from a.env file
load_dotenv()

# Configure the generative AI model with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model configuration for text generation
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Create a GenerativeModel instance with 'gemini-pro' as the model type
llm = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

def match_ingredients(user_ingredients, dietary_preferences=None):
    """
    Matches ingredients with recipes using Gemini Pro (if available).

    Args:
        user_ingredients (list): List of user-provided ingredients (lowercase and stripped).
        dietary_preferences (str, optional): User's dietary preferences (e.g., vegetarian, vegan).

    Returns:
        tuple: A tuple containing the recipe name and instructions (if found), otherwise None.
    """
    
    prompt_template = """Find a delicious recipe using these ingredients: {ingredients}. 
    {dietary_preferences_prompt}
    I want the response in a single structured format."""

    dietary_preferences_prompt = f"Considering dietary restrictions: {dietary_preferences}" if dietary_preferences else ""

    prompt = prompt_template.format(ingredients=", ".join(user_ingredients), dietary_preferences_prompt=dietary_preferences_prompt)

    response = llm.generate_content(prompt)

  # Parse the response from Gemini Pro to extract the matching recipe name and instructions (implementation depends on API response format)
    recipe = response.text
  # ... (code to parse response and extract recipe information)
    return recipe



st.set_page_config(page_title="Recipe Mixer", page_icon=":cooking:", layout="wide")

# Add a logo and name at the top left
logo_and_name = """
<style>
.logo-and-name {
  display: flex;
  align-items: left;
  justify-content: flex-start;
  padding: 5px;
  color: white;
  font-size: 15px;
  font-weight: bold;
  font-family: POPPINS;
}

.logo-and-name img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
</style>
<div class="logo-and-name">
  <img src="https://freepngimg.com/thumb/cooking/29649-2-cooking-picture.png" alt="Logo">
  Recipe<br>Mixer
</div>
"""
st.markdown(logo_and_name, unsafe_allow_html=True)

st.title("Recipe Mixer" + ":cooking:")
st.markdown('<style>h1{color: white; text-align: center; font-family:POPPINS; font-size: 48px;}</style>', unsafe_allow_html=True)

st.write("")

user_ingred = st.text_input("Enter your ingredients (comma-separated):", placeholder="e.g. chicken, rice, vegetables")

# Add dietary preference dropdown
dietary_options = st.selectbox("Dietary Preferences (Optional):", [None, "Vegetarian", "Vegan", "Gluten-Free"], index=0)

# Center the button
st.write('<style>div.row-widget.stButton > button {display: block; margin: auto;}</style>', unsafe_allow_html=True)
submit_button = st.button("Suggest me a recipe", key="suggest_button")

if submit_button:
    if user_ingred is not None:
        # Preprocess user ingredients
        user_ingredients_str = [ingredient.strip().lower() for ingredient in user_ingred.split(", ")]
        
        # Call match_ingredients once and assign results
        recipe =  match_ingredients(user_ingredients_str, dietary_preferences=dietary_options)

        if recipe:
            complete_recipe = f"\n{recipe}\n"
            st.write(complete_recipe.replace('\\n', '\n'))
        else:
            st.write("No Recipe Found 😔")

st.write("")

footer="""<style>
a:link, a:visited{
color: yellow;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: blue;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}

.footer p {
  font-size: 14px;
  margin-bottom: 0;
}
</style>
<div class="footer">
<p>Developed with ❤ by<a style='display: block; text-align: center;' href="https://github.com/Gitesh08" target="_blank">Hacker</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Change cursor
st.markdown('<style>body {cursor: url("https://freepngimg.com/thumb/spoon/2-spoon-png-image.png"), auto;}</style>', unsafe_allow_html=True)