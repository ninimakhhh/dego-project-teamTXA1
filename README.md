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

 * **Bias:** The analysis reveals statistically significant disparities in credit approval outcomes across gender and age. Female applicants have a disparate impact ratio of 0.77, indicating an approval rate approximately 23% lower than male applicants (p < 0.001). Age shows a small but statistically significant positive association with approval (r = +0.12, p < 0.01), with the 25–34 cohort as the standout low-approval group (44.3% vs. 62–66% for middle-aged groups, χ² p = 0.003). Proxy analysis suggests these disparities are partly mediated through correlated variables — particularly ZIP code (a strong gender proxy) and credit history length (a strong age proxy). Intersectional analysis confirms that the overall gender disparity is largely driven by the 25–34 cohort, where women face the steepest disadvantage (23 pp gap, χ² p = 0.008, DI ≈ 0.59).

 * **Governance Gaps:** Assesses NovaCred's credit application dataset against GDPR and EU AI Act requirements, under which credit scoring is classified as a high-risk AI system (Annex III). All dataset columns are classified by PII type and re-identification risk, mapped to the GDPR articles they trigger, and assigned one of four treatment actions: deletion (direct identifiers), exclusion from model training (protected attributes and strong proxies), transformation before use (quasi-identifiers), or access-controlled retention for fairness auditing. The notebook closes by documenting eight structural governance gaps - including absent consent timestamps, missing audit trail fields, and no human oversight mechanism - each with its regulatory citation and recommended remediation.



## Structure

*  ‘ data /‘ - Contains the original raw_credit_applications.json., converted original file as csv - full_dataset_view.csv, and cleaned dataset after data quality assessments clean_dataset_view.csv

*  ‘ notebooks /‘ 
    - 01_data_quality.ipynb - A dedicated data quality assessment file evaluates the dataset across four key dimensions - completeness, consistency, validity, and accuracy - identifying and remediating issues such as duplicates, inconsistent formats and data types, invalid values, and missing fields.
    - 02-bias-analysis.ipynb - The bias analysis file examines algorithmic fairness through four components: Gender Disparate Impact, Age-Based Discrimination Patterns, Proxy Variable Analysis, and Interaction Effects Between Attributes, assessing disparities in approval outcomes and identifying potential proxy-driven bias.
    - 03_privacy_demo.ipynb - This file addresses the privacy and governance obligations triggered by the findings, noting that credit scoring is classified as a high-risk AI system under the EU AI Act (Annex III, No. 5b) and therefore must comply with both GDPR and AI Act requirements. It includes sections on Identification of Personal Data & Classification, Privacy Risk Mitigation, Pseudonymization, GDPR Compliance Mapping, Governance Gaps, and Governance Recommendations.

* ‘ reports /‘ - All output figures are automatically saved to the dictionary.

* ‘ src /‘ - Python source code



