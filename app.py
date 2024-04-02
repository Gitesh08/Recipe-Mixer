import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables from a .env file
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
    recipe_instructions = response.text
  # ... (code to parse response and extract recipe information)
    return recipe
    

st.set_page_config(page_title="Recipe Mixer")

st.title("Recipe Mixer" + ":sunglasses:")
st.markdown('<style>h1{color: orange; text-align: center; font-family:POPPINS}</style>', unsafe_allow_html=True)

st.text(" \n")
st.text(" \n")
st.text(" \n")

user_ingred = st.text_input("Enter your ingredients (comma-separated):")

# Add dietary preference dropdown
dietary_options = st.selectbox("Dietary Preferences (Optional):", [None, "Vegetarian", "Vegan", "Gluten-Free"])

submit_button = st.button("Suggest me recipe")
user_ingredients = user_ingred.split(", ")


if submit_button:
    if user_ingred is not None:
    # Preprocess user ingredients
        user_ingredients_str = [ingredient.strip().lower() for ingredient in user_ingred.split(", ")]
        
        # Call match_ingredients once and assign results
        recipe =  match_ingredients(user_ingredients_str, dietary_preferences=dietary_options)
        #recipe_instructions = match_ingredients(user_ingredients, dietary_preferences=dietary_options)

        if recipe:
            complete_recipe = f"\n{recipe}\n"
            st.write(complete_recipe.replace('\\n', '\n'))
        else:
            st.write("No Recipe")
    
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")

footer="""<style>
a:link , a:visited{
color: yellow;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: Bottom;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by<a style='display: block; text-align: center;' href="https://github.com/Gitesh08" target="_blank">Gitesh Mahadik</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
