# Spring 2024 Big Data: CSGY 6513-D

## Team Members
- Jiaxin Dong, NetID: jd5226
- Chenchen Guo, NetID: cg4421
- Mohammed Zakriah Ibrahim, NetID: mi2471

## Big Data Project Proposal

### Abstract

In the rapidly evolving job market of 2024, understanding the dynamics of job availability, industry demands, and skill requirements is crucial for both job seekers and employers. This project utilizes a comprehensive dataset containing 1.3 million job listings scraped from LinkedIn, augmented with detailed job skills information. Our goal is to gain insights into the current job market trends, identify skill gaps, and develop a job recommendation system. The dataset serves as a rich source of information on job titles, industries, companies, and required skills, providing an unprecedented opportunity to analyze and address the needs of the modern workforce.

### Statement

The project centers around several key objectives:
- **Job Market Analysis:** Conduct a thorough analysis using the dataset to identify trends in job titles and industries across different geographies.
- **Skills Mapping:** Map out the skills landscape, pinpointing the skills most frequently listed in job postings across various job categories.
- **Job Recommendation System Development:** Develop a sophisticated job recommendation system that matches job seekers with suitable positions based on their profiles, experiences, and skill sets.
- **Industry and Job Title Trends Exploration:** Explore patterns and correlations between job types, levels, and required skills across different industries to provide insights into qualifications needed for career advancement.
- **Education and Training Program Guidance:** Inform educational and training programs by identifying current skill gaps.

### Objectives

1. **Exploratory Data Analysis (EDA) on Job Market Data:** Perform comprehensive exploratory data analysis to uncover underlying patterns, detect anomalies, and gain insights into the job market dynamics.
2. **Skills Mapping:** Leverage the skills data within the dataset to identify in-demand skills across different sectors.
3. **Job Recommendation System Development:** Create a sophisticated job recommendation system with scoring search algorithms.
4. **Industry and Job Title Trends Analysis:** Identify emerging trends spotlighting growth sectors and roles.
5. **Temporal Trends Analysis:** Evaluate job listings frequency over different time frames to identify trends and optimize search strategies.
6. **Geographical Data Analysis in Job Markets:** Analyze geographical data to understand regional employment trends and demographic impacts on job availability.
7. **Correlation Analysis Between Job Skills and Job Titles:** Investigate the direct relationships between job skills and job titles.

### Methodology & Technology

- **Data Cleaning and Preprocessing:** Ensure dataset accuracy and usability, handling missing data, normalizing job titles, and categorizing skills.
- **Statistical Analysis and Search Algorithms:** Utilize statistical methods and develop scoring search algorithms.
- **Visualization and Deployment:** Create visualizations and a web-based GUI client-side app for easier access.

### Technologies Used
- Python 3.10+
- Pandas
- PySpark
- Jupyter Notebook
- Matplotlib
- Seaborn
- Streamlit

### Data Source
- **Dataset:** [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024/data)
- **Size:** 2GB
- **Records:** 1,296,000

# Quick Setup Guide

## Installation Instructions

### Step 1: Install Required Packages

First, install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

If Python reports any missing modules, please install each required module separately.

### Step 2: Download and Setup Data

Download the necessary data file from the provided link and extract it into the specified directory:

```plaintext
Download Link: [Google Drive Data File](https://drive.google.com/file/d/1UjCRQ7ZeF79miKzDM74Fwgon8fYEdiFh/view?usp=drive_link)
```

Please extract the downloaded file to the following location:

```
/Project/data
```

### Step 3: Configure Batch Files

Navigate to the `/Project` directory where you will find two `.bat` files. You will need to modify these files by changing the line:

```plaintext
call conda activate streamlit
```

to:

```plaintext
call conda activate your/conda/env/
```

After making this change, double-click the `.bat` file to initiate the project.

## Running the Project Through Conda

For direct execution through Conda, follow these steps:

```bash
conda create -n yourenvname python=3.10
conda activate yourenvname
pip install -r requirements.txt
streamlit run ./Project/web.py
```

### Troubleshooting

If you encounter errors such as "no module named xxxxxx", please install the additional modules separately.
