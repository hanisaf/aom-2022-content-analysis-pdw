# aom-2022-content-analysis-pdw
Companion code to presentation in session 158 https://2022.aom.org/meetings/virtual/BzaRqMzdWCsc9rnPh

To use the code:

- Install requirments `pip install -r requirments.txt`
- Create an OpenAI account and obtain a [developer key](https://beta.openai.com/account/api-keys)
- Paste the developer key in `step-1-upload-documents-to-gpt3.py` and `engine.py`
- Run `python step-1-upload-documents-to-gpt3.py` to upload the documents to GPT3
- Run `python dashboard.py` to run the interactive q/a dashboard

The data comes from [the serious sellers podcast](https://www.helium10.com/podcast/). You can try it with your own data as long it follows the same format.