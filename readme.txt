Need to build Neo4J graph first and copy the key in the .env at :
https://console-preview.neo4j.io/projects/b4b12d7d-e00f-4a4a-9c24-8f0b2f7a34b3/instances


docker-compose up --build

http://localhost:8000/docs#/
http://localhost:8501/


https://console-preview.neo4j.io/projects/b4b12d7d-e00f-4a4a-9c24-8f0b2f7a34b3/instances
MATCH (p:Patient)
RETURN p LIMIT 5;

MATCH (p:Patient)-[h:HAS]->(v:Visit)
WHERE v.id = 56
RETURN v,h,p;

MATCH (p:Patient)-[h:HAS]->(v:Visit)<-[t:TREATS]-(ph:Physician)
WHERE v.id = 56
RETURN v,p,ph


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