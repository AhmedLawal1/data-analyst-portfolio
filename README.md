# Data-Analyst-Portfolio
A portfolio of data analysis projects and dashboards by Ahmed Lawal.


## Power BI Product Dashboard

<p>Project Objective

  Stakeholder wanted a dashboard report that solely focuses on Case Units, monitoring the top 120 products being brought by our members solely. It will be updated will new data monthly.</p>
  
<p>KPIs:
  
-	Product Ranking: A table which will allow us to see how the products are performing i.e. a product ranked 5th last month may move up to 1st for the current month. Possible use of arrows to indicate the products movements in table. (Top 120 Products)

-	Product Tracking: A line graph which will allow us to see the historic and up-to-date performance of products.
 
-	 Other Features: Further breakdown of products into categories i.e. Frozen, Ambient, Chilled & Non-Food. Some members have purchased smaller business that suppliers have data from, so I was required to aggregate the unit as part of the parent member.</p>

Power BI Dashboard:

<a href='https://github.com/AhmedLawal1/data-analyst-portfolio/blob/main/Dashboard/Overview%20Page.png'> Overview Page</a>   
<a href='https://github.com/AhmedLawal1/data-analyst-portfolio/blob/main/Dashboard/Ranking%20Page.png'> Product Ranking Page</a>


## Prediction Model Build
<p>Project Objective

  I was approached by the Head Of Finance to predict next years sales figures, identify trends, patterns and potential drops. The reason behind this is because this task is outsourced, then further worked on by the head of finance and presented to the board during Q3. </p>
  
<p>Process: 

- Meeting with Head Of Finance. Find out if there are any serious changes happening in the next year that they may know i.e. a new a member in the group.
- Gather sales data (at least past 3 years)
- Do analysis such as "Seasonal Decompose", ADF Fuller Test, etc. To see the underlying pattern of the data.
- Research prediction models that will perform best for each member. <p>

This is the prediction model for one of the members in Jupiter Notebook:
<a href='https://github.com/AhmedLawal1/data-analyst-portfolio/blob/main/Dashboard/Prediction%20Model(PD).ipynb'> Model</a>

Outcome: 

Unbeknown to me The Head Of Finance had made his own predictions using Excel. With the confirmation of the Head Of Finance my prediction was presented to the board. The reason was because my prediction picked up a steep decline in a member, and the figures given were closer to what had been agreed. 


## SQL Server Sales Report

<p>Project Objective

  Create a new sales report directly from the businesses server as previous sales report was pulling from the incorrect source </p>

<p>Process & Requirements

  - My first step was to set a meeting with our server/database provider and understand how the data is collected and stored.
  - I then started looking into each table using Microsoft SQL Server Management Studio. At this point I brought in the head of sales to validate the data I plan to use as my source.
  - Once confirmed I wrote up my SQL query and exported the report.</p>

SQL Qurey:
<a href='https://github.com/AhmedLawal1/data-analyst-portfolio/blob/main/Dashboard/db_connect.py'> Page 1</a>

Footnote: 
    Later on I plan to connect the server direct to Power BI, creating visuals and custom DAX measures for further insight and analysis.
    
