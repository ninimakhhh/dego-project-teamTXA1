# DEGO Project - Team TXA1

## Executive Summary

This report outlines the results of a data governance audit performed on NovaCred’s credit application dataset, which contains 502 records. Acting as a Data Governance Task Force, we identified and addressed data quality issues, uncovered statistically significant bias, and evaluated the system’s compliance with the GDPR and the EU AI Act.

## Team Members

| Name | Number | Role | GitHub |
|------|------|------|--------|
| Ferdinand Misund | 71652 | Data Engineer | @ferdinandmisund |
| Alexandra Kriecherbauer | 70081 | Data Scientist | @AlexKbauer |
| Dalila Dores Vieira | 74454 | Governance Officer | @dalilaavieiraa |
| Nino Makharadze | 75057 | Product Lead | @ninimakhhh |


**Key Findings**

 * **Data Quality:** Six categories of issues were identified and remediated: duplicate records (2), inconsistent data types (income stored as a string), four variants of gender coding, inconsistent date formats, invalid values (negative credit history period, non-positive income, negative saving balance, irregular DI ratop, and invalid email addresses), and missing or incomplete entries across 13 columns.

 * **Bias:** The analysis reveals statistically significant disparities in credit approval outcomes across gender and age. Female applicants have a disparate impact (DI) ratio of 0.77, indicating an approval rate about 23% lower than male applicants, while applicants aged 25–34 show a DI of 0.676 relative to the 35–44 group. Both disparities are statistically significant and indicate systematic differences in outcomes. Proxy analysis suggests that some of the observed bias may be mediated through correlated variables - particularly ZIP code (a strong gender proxy) and credit history length (a strong age proxy). Intersectional analysis further shows that women aged 25-34 experience the most severe disadvantage (DI = 0.463), indicating that fairness risks are amplified when gender and age effects interact.

 * **Governance Gaps:** The dataset contains multiple categories of personally identifiable information (PII), including direct identifiers (e.g., full_name, ssn) and high-risk quasi-identifiers such as date_of_birth, gender, and zip_code. Under GDPR Art. 4(1) these attributes qualify as personal data, while behavioural and decision-related fields (e.g., spending_category, loan_approved) fall within profiling and automated decision-making considerations under Art. 4(4) and Art. 22. Risk assessment shows that several attributes require stronger protection measures - such as pseudonymisation, tokenisation, or generalisation - to reduce re-identification risk. In addition, the dataset structure reveals governance gaps related to transparency and compliance, including insufficient documentation of data processing, unclear retention practices, and limited mechanisms to justify or audit automated credit decisions. Strengthening data minimisation, retention policies, and privacy safeguards would improve regulatory compliance and enhance the overall transparency and accountability of the credit decision system.



## Structure

*  ‘ data /‘ - Contains the original raw_credit_applications.json., converted original file as csv - full_dataset_view.csv, and cleaned dataset after data quality assessments clean_dataset_view.csv

*  ‘ notebooks /‘ 
    - 01_data_quality.ipynb - A dedicated data quality assessment file evaluates the dataset across four key dimensions - completeness, consistency, validity, and accuracy - identifying and remediating issues such as duplicates, inconsistent formats and data types, invalid values, and missing fields.
    - 02-bias-analysis.ipynb - The bias analysis file examines algorithmic fairness through four components: Gender Disparate Impact, Age-Based Discrimination Patterns, Proxy Variable Analysis, and Interaction Effects Between Attributes, assessing disparities in approval outcomes and identifying potential proxy-driven bias.
    - 03_privacy_demo.ipynb - This file addresses the privacy and governance obligations triggered by the findings, noting that credit scoring is classified as a high-risk AI system under the EU AI Act (Annex III, No. 5b) and therefore must comply with both GDPR and AI Act requirements. It includes sections on Identification of Personal Data & Classification, Privacy Risk Mitigation, Pseudonymization, GDPR Compliance Mapping, Governance Gaps, and Governance Recommendations.

* ‘ reports /‘ - All output figures are automatically saved to the dictionary.

* ‘ src /‘ - Python source code



