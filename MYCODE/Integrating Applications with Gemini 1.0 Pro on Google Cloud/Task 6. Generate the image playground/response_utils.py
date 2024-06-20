def get_gemini_pro_vision_response(model: GenerativeModel, prompt_list, generation_config={}, stream=True):

    generation_config = {'temperature': 0.1,
                     'max_output_tokens': 2048
                     }

    responses = model.generate_content(prompt_list, generation_config = generation_config, stream=True)

    final_response = []
    for response in responses:
        try:
            final_response.append(response.text)
        except IndexError: 
            final_response.append("")
            continue
    return(" ".join(final_response))