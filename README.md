# **Vital Vision**

## Results

Video: https://youtu.be/dWTW6PaEXgk

Slides: https://bit.ly/3lJvONq

Squirtle Squad

Impact (50 Points Total)
Does the entry establish a clear challenge using their problem statement? (10 points)
Judge 1 : 4 / 10 points
Judge 2 : 5 / 10 points

Do they explain clearly which (Selected SDG) they chose for their solution and why? (10 points)
Judge 1 : 8 / 10 points
Judge 2 : 8 / 10 points

Does the team clearly describe three feedback points they received from real users and the steps they took to test them? (5 points)
Judge 1 : 0 / 5 points
Judge 2 : 0 / 5 points

Is there evidence of what the team learned and how the solution was iterated upon based on user feedback? (5 points)
Judge 1 : 0 / 5 points
Judge 2 : 1 / 5 points

Does the solution address the challenge (and problem statement) identified by the team? Does the team adequately describe the success of their solution using metrics, goals, and outcomes, or through cause and effect? (10 points)
Judge 1 : 4 / 10 points
Judge 2 : 3 / 10 points

Is there evidence of next steps? Does the team display a clear plan for future extension to a larger audience if they were to continue? (10 points)
Judge 1 : 4 / 10 points
Judge 2 : 1 / 10 points

Technology (10 Points Total)
Does the team clearly describe the following: architecture, high-level components, responsibility of each component, specific products and platform they implemented? Has the team clearly explained what Google technology they used and why? (5 points)
Judge 1 : 3 / 5 points
Judge 2 : 3 / 5 points

Does the solution implement all the technical components needed to solve the challenge? (5 points)
Judge 1 : 1 / 5 points
Judge 2 : 2 / 5 points

## Links

[Google Colab](https://colab.research.google.com/drive/1CBMeh-eQuJzMsjarn7zTWbgHaV-fGF-b?usp=sharing)

[pyVHR](https://github.com/phuselab/pyVHR)

[Paper 1](https://arxiv.org/abs/2110.13362)

[Paper 2](https://arxiv.org/abs/2111.11547)

[More Info](https://cameravitals.github.io/)

[Datasets](https://cameravitals.github.io/datasets.html)

[Public Dataset 1](https://ieee-dataport.org/open-access/ubfc-phys-2)

[Public Dataset 2](https://rice.app.box.com/s/noy6vn7k5g5bfvl9o6ekcjmgc9ng4yel/folder/77515207699)

[Project Inspiration](https://github.com/ajsteele/faceHR)

## Abstract

### About

The Vital Vision project aims to tackle the challenge of healthcare accessibility in remote and underdeveloped areas by utilizing facial hue changes as a means of detecting heart rate. This innovative solution provides a cost-effective and efficient way for healthcare professionals to monitor patients, including premature babies, whose delicate health requires constant monitoring. With Vital Vision, healthcare professionals can receive a constant stream of data and quickly respond in case of any health issues, improving patient outcomes and overall accessibility to quality healthcare in remote areas.

### Problem Statement

In remote and underdeveloped areas, there is a significant gap in access to quality healthcare services, leading to poor health outcomes for vulnerable populations. This problem is compounded by the lack of traditional healthcare monitoring methods, such as heart rate monitoring, available to these populations.

### Solution - Sustainable Development Goals

Vital Vision is described as a solution aimed at addressing the issue of healthcare accessibility in remote and underdeveloped areas. 

Vital Vision addresses Sustainable Development Goal 3 (SDG 3): Ensure healthy lives and promote well-being for all at all ages. This SDG specifically targets the need to ensure access to quality healthcare services and to improve health outcomes, especially for vulnerable and marginalized populations who may face barriers to accessing healthcare services. 

Moreover, Vital Vision also addresses Sustainable Development Goal 9 (SDG 9): Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation. By using innovative technology to monitor the heart rate of patients in remote areas, Vital Vision contributes to the goal of building resilient infrastructure and promoting sustainable industrialization in the healthcare sector. 

Furthermore, Vital Vision also addresses Sustainable Development Goal 17 (SDG 17): Strengthen the means of implementation and revitalize the global partnership for sustainable development. 

By providing a cost-effective and efficient solution for monitoring patients, Vital Vision helps to strengthen the means of implementation for providing quality healthcare services, and by partnering with healthcare professionals and organizations, it revitalizes the global partnership for sustainable development.

### Solution - Targets

- SDG 3: Target 3.8 "Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines and vaccines for all."

- SDG 9: Target 9.c "Significantly increase access to information and communications technology and strive to provide universal and affordable access to the Internet in least developed countries by 2020."

- SDG 17: Target 17.18 "By 2020, enhance capacity-building support to developing countries, including for least developed countries and small island developing States, to increase significantly the availability of high-quality, timely and reliable data disaggregated by income, gender, age, race, ethnicity, migratory status, disability, geographic location and other characteristics relevant in national contexts."

The specific goals and targets were chosen as they align with the aim of Vital Vision, which is to improve access to quality healthcare services and to improve health outcomes, especially for vulnerable and marginalized populations who may face barriers to accessing healthcare services. 

Additionally, the use of technology and connectivity also addresses the need to increase access to information and communication technology, and enhance capacity-building support to developing countries.

### Architecture

The architecture of our solution consists of several key components, each with its own specific responsibilities.

- Data Collection: Tasks include gathering necessary data from patients, such as images and videos of their facial hue changes, which will be used to determine their heart rate.

- Image Processing: Processes collected data, analyzing changes in facial hue to determine an accurate heart rate reading.

- Data Storage: Keeps processed data safe, including patient information, heart rate readings, and any other relevant medical information.

- Data Analysis: Analyzes stored data, looking for patterns and trends in heart rate readings, and provides insights to healthcare professionals.

- Machine Learning: Trains and deploys models used to accurately detect heart rate from facial hue changes.

- Mobile Application: Provides patients with a user-friendly interface, integrates with other components and informs healthcare professionals with real-time updates.

- Healthcare Integration: Integrates with healthcare systems, such as electronic health records, to ensure accuracy and up-to-date patient data.

Each component is designed to work together to provide a comprehensive and integrated solution.

### Implementation through Google Technologies

The following products and platforms were implemented for our solution. 

- Google AI - This advanced technology can play a vital role in analyzing the data collected from changes in facial hue, providing accurate and efficient heart rate readings for patients located in remote and underdeveloped areas.

- Google Colaboratory - This tool provides an environment for development and computing, streamlining the coding and testing process to ensure efficient results, similar to Jupyter Notebook.

- Google Cloud Healthcare API - This API is tailored to the healthcare industry, offering secure storage and processing of sensitive patient data.

- Google Cloud Machine Learning Engine - This technology can be used to train and deploy machine learning models, allowing for accurate heart rate detection based on changes in facial hue.

- Google Cloud Storage - With the capability to store vast amounts of data, such as images and videos captured from patients, this technology can be utilized for further analysis and processing.

- Google Firebase - A mobile application for patients can be developed using this technology, providing real-time updates to healthcare professionals and integrating seamlessly with the other Google technologies.

These technologies were chosen due to their integration with each other and the ease of use they provide in building a scalable and efficient solution. Their robust and secure architecture also ensures the privacy and security of sensitive patient information.