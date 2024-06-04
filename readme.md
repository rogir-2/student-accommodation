# UoL Student Accommodation
### Abstract
This project aims to aid University of Leicester (UoL) students in their move to independent housing by providing key insights into the rental market. Data was scraped from unihomes.co.uk using Python, processed and analysed with Excel, and summarised in PowerPoint. Insights reveal that Clarendon Park and Highfields offer a high concentration of properties, with varying rental prices. Students are advised on how to prioritise their housing search based on location, budget, and essential amenities. This analysis equips UoL students with the necessary information to effectively navigate the housing market and secure suitable, affordable accommodations.

### Keywords
Python, Excel, PowerPoint, ETL (Extract, Transform, Load), Data Scraping, Data Wrangling, Data Modelling, Data Visualisation, Storytelling, Project Management, Power Query, Power Pivot, M-Language, Presentation, Critical Thinking, Problem-Solving, Analytics, Continuous Learning, Star Schema, SCQA Framework, and Ad-Hoc Analysis 

## Problem Statement
Transitioning from university-provided to independent housing poses a daunting challenge for University of Leicester (UoL) students beyond their first year. While the institution reserves hall spaces primarily for freshers, returning students struggle to secure suitable, affordable accommodations near the university and essential amenities. To ensure a smooth transition to independent living, students urgently require current insights into the housing market.

## Project Objectives & Scope
Empower UoL students with comprehensive insights and actionable information to streamline their housing search and budgeting endeavours. By addressing key questions through meticulous data collection and analysis, the project will:

+ Compile data on available properties, encompassing types, and locations.
+ Identify high-density areas, assess the proximity and commute times near UoL.
+ Analyse rental price dynamics across diverse areas and property types.

## Deliverables
A **presentation** summarising key insights, recommending suitable areas, and rental prices.<br>
<a href="">Access & Download Presentation</a>

## Methodology
**Python**<br>
Utilised Python for data scraping and initial processing:

+ **Requests:** Sent HTTP requests to collect housing data from UniHomes.
+ **JSON:** Parsed and processed data received in JSON format.
+ **Pandas:** Performed pre-processing, transformation, and export of data.
+ **OS & Pathlib:** Handled file interactions within the operating system.

**Excel**<br>
Employed Excel for data transformation and visualisation to illustrate data trends and patterns:

+ **Power Query:** Extracted, transformed, and loaded scraped data.
+ **Power Pivot:** Modeled data and constructed star schema.
+ **Pivot Table:** Summarised and analysed data through aggregation and filtering.
+ **Pivot Chart:** Created dynamic charts to effectively visualise data insights.

**PowerPoint**<br>
Formulated a PowerPoint presentation to convey data insights in an engaging and comprehensible manner.

## Explore detailed chapters on the data analysis process
1. <a href="./stages/1.prepare/">Data Scraping</a>
2. <a href="./stages/2.clean.md">Data Wrangling</a>
4. <a href="./stages/3.model.md">Data Modelling</a>
5. <a href="./stages/4.analyse.md">Analysis & Visuals</a>

## Insights & So What?

Data reveals several Leicester neighbourhoods boast a high concentration of properties, with houses dominating the landscape over apartments. Clarendon Park and Highfields, both within a convenient 20-minute commute of the University (less than a mile away), offer a haven for students seeking a more affordable lifestyle. Renting a room in these areas typically falls below the city’s average weekly rent of £120, making them budget-friendly options. However, venturing towards the City Centre and Westcotes might present more attractive rental properties and amenities, though with a trade-off: longer travel times to campus<br>

**Action students can take:**

+ **Prioritise location:** if proximity to campus is crucial, focus on properties in the Clarendon Park and Highfields to save time and travel costs, enhancing your academic experience.

+ **Type of Property:** Decide between apartments, more prevalent in central areas, and houses, which tend to be cheaper but may be located further from the university.<br>

+ **Assess Amenities:** Determine the importance of amenities (e.g., furnished vs. unfurnished, utilities included) and choose properties that meet your needs.

## Limitations

+ **Lack of Historical Data:** The absence of historical pricing data limits the ability to analyse rental price trends over time, which could provide valuable insights for future projections and budgeting.

+ **Incomplete Property Types:** The dataset may not encompass all available property types, such as studio apartments or luxury accommodations, thereby limiting the scope and applicability of the analysis.

+ **Furnishing Details:** Missing information on whether properties are furnished or unfurnished hampers the ability to fully assess the value and suitability of different accommodations for students' needs.

+ **Neighborhood Information:** The analysis lacks contextual data on neighborhood safety, transportation options, and local amenities, which are crucial for making informed housing decisions.

+ **Agency Fees and Contract Details:** Information regarding agency fees, deposit requirements, and rental contract lengths is not included, which can significantly impact the total cost of renting and students' financial planning.

+ **Socioeconomic Data:** The absence of demographic information such as student income levels or family financial support limits the ability to understand and address socioeconomic factors influencing accommodation choices.