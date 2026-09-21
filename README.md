Citizen email classification dataset
## Project Overview
This project contains a labeled dataset of citizen emails related to CleanCity waste collection services.
The dataset is designed to be used for testing and evaluating an LLM-based email classification system. Each email is manually assigned to one of four categories:

* **Schedule Change**
* **Missed Pickup**
* **Complaint**
* **General Info**
The goal is to provide realistic and varied citizen messages that an AI classifier can use to identify the purpose of an incoming email.
---
## Dataset Information
The dataset is stored in:
```text
emails_labeled.csv
```
The CSV contains the following two columns:
| Column       | Description                             |
| ------------ | --------------------------------------- |
| `email_text` | The text/content of the citizen's email |
| `label`      | The category assigned to the email      |
The dataset contains **200 sample citizen emails**.
### Allowed Labels
Every email is assigned exactly one of the following labels:
```text
Schedule Change
Missed Pickup
Complaint
General Info
```
---
## Data Source
The dataset consists of **synthetically generated sample citizen emails** created for this coursework/project.
---
## Labeling Process
Each email was manually reviewed and assigned to one of the four predefined categories.
### 1. Schedule Change
Used when a citizen asks to change, reschedule, confirm, or find an alternative collection date.
Example:
```text
Can you change our garbage collection day from Monday to Wednesday?
```
Label:
```text
Schedule Change
```
### 2. Missed Pickup
Used when a scheduled waste collection did not happen.
Example:
```text
Our garbage was not collected yesterday. Could you please check the collection route?
```
Label:
```text
Missed Pickup
```
### 3. Complaint
Used when a citizen expresses dissatisfaction or reports a problem with the waste collection service.
Example:
```text
I am unhappy with the garbage collection service in our area because the bins are often left uncollected.
```
Label:
```text
Complaint
```
### 4. General Info
Used for general questions about waste collection services that do not specifically request a schedule change or report a missed pickup.
Example:
```text
What days is garbage collected in my neighborhood?
```
Label:
```text
General Info
```
---
## Dataset Structure
A simplified example of the CSV structure is:
```csv
email_text,label
"Can you change our garbage collection day from Monday to Wednesday?","Schedule Change"
"Our garbage was not collected yesterday.","Missed Pickup"
"I am unhappy with the garbage collection service in my area.","Complaint"
"What days is garbage collected in my neighborhood?","General Info"
```
---
## Data Variety
The emails were created with different wording and scenarios to avoid having every message look the same.

Examples include:

* Requests to change collection days
* Questions about alternative collection dates
* Reports of missed garbage collection
* Complaints about repeated service problems
* Questions about collection schedules
* Questions about collection rules and procedures
* Different locations and household situations
* Different levels of formality
* Short and longer citizen messages

This variety is intended to make the dataset more useful for testing an email classification system.
---
## Validation
The dataset was checked to ensure that:

* The CSV contains at least 200 email records.
* The required columns are present.
* Every email contains a label.
* Every label belongs to the four allowed categories.
* The email text and label are stored in separate CSV columns.
---
## Project Purpose
This dataset will be used to test an **AI Email Triage System for CleanCity Services**.

The future classifier can receive a citizen email and predict which category it belongs to:
```text
Citizen Email
      ↓
LLM Classifier
      ↓
Predicted Category
      ↓
Schedule Change
Missed Pickup
Complaint
General Info
```
The labeled dataset provides examples that can be used to evaluate whether the classifier correctly identifies the purpose of citizen emails.
---
## Limitations
The dataset is synthetic rather than collected from real CleanCity customer records. Therefore, it may not represent every type of language, spelling mistake, regional expression, or unusual situation found in real citizen emails.

No personally identifiable information or real private customer conversations were included.
---
## What Was Difficult
The main challenge was creating enough realistic and varied emails while keeping the four category labels consistent. Some messages could potentially fit more than one category, so each email was reviewed based on its primary purpose and assigned to the most appropriate predefined category.
---
## What Was Left Out
This task focuses only on creating and labeling the dataset. The LLM classification system, model evaluation, and automated email processing are not included in this dataset creation stage.
## Repository Contents
---
citizen-email-classification-dataset
|
├── emails_labeled.csv
|__ emails_validator.py
|___ README.md
