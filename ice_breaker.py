
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import openai
import os
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
from third_parties.linkedin import scrape_linkedin_profile


LINKEDIN_PROFILE_URL = 'https://www.linkedin.com/in/dovifrances/'

openai.api_key = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1 - a short summary
        2 - two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=LINKEDIN_PROFILE_URL)

    print(chain.run(information=linkedin_data))

