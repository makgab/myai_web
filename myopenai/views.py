# importing render and redirect
from django.shortcuts import render, redirect
# importing the openai API
import openai
import os
# import the generated API key from the secret_key file
# from .secret_key import API_KEY
API_KEY = "API_KEY"

# loading the API key from the secret_key file
openai.api_key = os.getenv( API_KEY )

# this is the home view for handling home page logic
def home(request):
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
    try:
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            prompt = request.POST.get('prompt')
            # making a request to the API 
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.6, max_tokens=150)
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            context = {
                'formatted_response': formatted_response,
                'prompt': prompt
            }
            # this will render the results in the home.html template
            return render(request, 'assistant/home.html', context)
        # this runs if the request method is GET
        else:
            # this will render when there is no request POST or after every POST request
            return render(request, 'assistant/home.html')

    # the except statement will capture any error
    except:
        # this will redirect to the 404 page after any error is caught
        return redirect('error_handler')


# this is the view for handling errors
def error_handler(request):
    return render(request, 'assistant/404.html')
