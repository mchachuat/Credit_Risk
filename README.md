# Credit Risk Default Prediction

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

A machine learning project to predict the probability of borrower default based on financial and demographic features.

## 🚀 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run WebApp](#run-webapp)
- [Project Structure](#project-structure)
- [License](#license)

---

## Project Overview

Credit default prediction is critical for financial institutions to mitigate risks and make informed lending decisions. In this project, we develop a random forest machine learning model to predict the default rate of borrowers using a publicly available credit risk dataset.

Key objectives:

- Explore and preprocess the data
- Engineer relevant features
- Train random forest model
- Develop a web interface
- Provide reproducible code and documentation

---

## Dataset

We use the **Credit Risk Dataset** from Kaggle:

> Credit Risk Dataset by laotse – https://www.kaggle.com/datasets/laotse/credit-risk-dataset?resource=download

The dataset includes anonymized records of loan applications and borrower information, along with a binary target variable indicating default.

---

## Features

The following features are used to predict borrower default:

| Feature                     | Description                                          |
|-----------------------------|------------------------------------------------------|
| **Age**                     | Age of the borrower in years                         |
| **Annual Income**           | Borrower's annual income (in USD)                    |
| **Home Ownership**          | Ownership status (e.g., Mortgage, Rent, Own)         |
| **Employment Length**       | Number of years employed                             |
| **Loan Intent**             | Purpose of the loan (e.g., debt consolidation)       |
| **Loan Grade**              | Credit grade assigned to the loan (A, B, C, …)       |
| **Loan Amount**             | Requested loan amount (in USD)                       |
| **Interest Rate**           | Annual interest rate on the loan (%)                 |
| **Percent Income**          | Loan amount as a percentage of annual income (%)     |
| **Historical Default**      | Binary indicator: past default history               |
| **Credit History Length**   | Length of credit history in years                    |

Target variable: **`Default`** (0 = no default, 1 = default)

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mchachuat/Credi_Risk.git
   cd Credi_Risk

2. **Unzip the pre-trained model**:
   ```bash
   unzip model/model.pkl.zip -d model/

## Usage

### Run WebApp

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py

### Project Structure



### License

This project is licensed under the MIT License.


