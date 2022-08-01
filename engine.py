import openai
openai.api_key = "Insert your API key here"

def answer(query):
    return openai.Answer.create(
        search_model="curie", 
        model="davinci", 
        question=query, 
        file="file-msv3AzlK3iLXoKLVB7hDQ0SZ", 
        examples_context="When you deploy Oracle Analytics Cloud, you complete some initial setup steps, and then Oracle takes care of most service management, patching, backup and restore, and other maintenance tasks. You determine the size of your service when you set up the service and you can increase or decrease capacity if your requirements change. Oracle Analytics Cloud offers two sizing options, you can specify the number of Oracle Compute Units (OCPUs) you want to deploy or how many people you expect to use the service.", 
        examples=[["What are the sizing options offered by Oracle Analytics Cloud?", "You can specify the number of Oracle Compute Units (OCPUs) you want to deploy or how many people you expect to use the service."]], 
        max_rerank=200,
        max_tokens=100,
        return_metadata=True,
        stop=["<|endoftext|>"]
    )    