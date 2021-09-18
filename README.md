# VinProof

<img src="/static/Logo.png" alt="Logo"/>

<h1>##Spray Tool Calculator</h1>

<h4>About this app:</h4>
=======

A lot of vineyard growers struggle to keep updated records and a careful spray diary. Furthermore, it's quite common for people to incorrectly apply the wrong product or spray rate if they are out in the field. 

This app is designed to help growers calculate quickly and accurately the desired rates for their vineyard according to size, depending on what stage the vineyard is at in the season.

A common measure of vineyard development that is widely used is the <em>Modified E-L System by Coombe and Dry</em>See below: <br>

![E-L Modified Stage](http://https://www.awri.com.au/wp-content/uploads/grapegrowth.pdf)

This app uses this EL tool to determine what chemicals and rates are required for your vineyard based on size.

<h4>Planning & Design</h4>
=======

* Designed on Figma *

Wireframes
<a href="https://www.figma.com/file/RNoZZ8a1tHAC3suykHdfF5/VinProof?node-id=0%3A1" title="Vinproof">VinProof</a>

Notion 
<a href="https://www.notion.so/537298ba7ac748f1a4723cd7cdb48128?v=8b13014a410042dc96a032bb17a86ffe" title="Notion">Notion Planning</a>

This app was originally intended to be a soil asssessment but the access to API documentation was limited.

The app intends to allow users to add, edit, and delete vineyards and to calculate chemical rates and to use a weather API to determine if it is a good day to spray.

<h4>App Website</h4>
=======
<a href="https://vinproof.herokuapp.com/" title="Notion">Notion Planning</a>

<h4>Using the app on your server</h4>
=======

Open your terminal: <br>

i. Create a database called:

        <createdb vinproof_db>

ii. Enter in your databases according to the schema.sql file to enter the three tables:<br>

<ul>
    <li>vineyard</li>
    <li>users</li>
    <li>spray_program</li>
<br>

3. Enter the following code in your  terminal to activate your virtual environment:

        <python -m venv venv>
        <source venv/bin/activate>

4. Enter the following code into your  terminal:

        <pip install flask>
        <pip install psycopg2>

5. Run your app:

        <python app.py>

 
<h4>Roadblocks</h4>
=======

- find API documentation that is usable
- Time Management! Set goals to acquire the minimum requirements before adding any other dimensions
- CSS. This app is meant to be user friendly so ideally it would work across all media platforms

<h4>Future Improvements</h4>
=======

- Implement Weather API
- Another form field for images of the vineyard
- Fix edit fields to allow users to enter one parameter at a time
- Use some JS to edit forms more cleanly

<h4>Thank you</h4>
=======

Thank you to the team at GA for all your help with this project.