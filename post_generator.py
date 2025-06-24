from llm_helper import llm
from shots import shotPosts

def get_length(length):
    if length=="Short":
        return "1 to 5 lines"
    if length=="Medium":
        return "6 to 10 lines"
    if length=="Long":
        return "11 and more lines"

def get_prompt(length,language,tag):
    str_length = get_length((length))
    prompt = f''' generate a linkedin post using the below information. no preamble at all
        1. topic:{tag}z
        2.length:{length}
        3. language: {language}
        4. mimic the way humans think and write their posts like they are engaging with an audience 
        5. add relevant Hashtags and Emojis
        6. the script for the generated post should always match the language chosen

        '''
    shots_instance = shotPosts()
    examples = shots_instance.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i + 1}: \n\n {post_text}'

        if i == 1:  # Use max two samples
            break
    return prompt

def generate_post(length,language,tag):
    prompt=get_prompt(length,language,tag)
    response=llm.invoke(prompt)
    return response.content

if __name__=="__main__":
    print(generate_post("Medium", "Arabic", "Job Search"))