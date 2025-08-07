# demo-llmrag-hostobot
A showcase of a simple LLM (chatGPT) + RAG (NeoJ) + MiddleBack/ETL (Python) about requesting in natural langage hospitals data.

To be able to run the application, you only need to have NEO4J IDs and an OpenAI Key and FILL THE .ENV FILE. (and have docker desktop running to run the run command).

To run the application :
>>> docker-compose up --build

Too see the local frontend running of the chatbot got to :
http://localhost:8000/docs#/
http://localhost:8501/




Example Questions

Which hospitals are part of the hospital network?
What’s the current wait time at Wallace-Hamilton Hospital?
At which hospitals are patients reporting issues related to billing or insurance?
What’s the average length in days for completed emergency visits?
How are patients describing the nursing team at Castaneda-Hardy?
What was the total amount billed to each payer during 2023?
What is the average charge for visits covered by Medicaid?
Which doctor has the shortest average visit duration?
What is the total billed amount for patient 789's hospital stay?
Which state saw the biggest percentage increase in Medicaid visits from 2022 to 2023?
What’s the average daily billing amount for patients with Aetna coverage?
How many patient reviews have been submitted from Florida?
For visits that include a chief complaint, what percentage also have a review?
What percentage of visits at each hospital include patient reviews?
Which physician has received the highest number of reviews for their visits?
What is the unique identifier for Dr. James Cooper?
Show all reviews associated with visits handled by physician 270 — include every one.
