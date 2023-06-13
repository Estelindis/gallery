# Gallery of Dreams - Project Portfolio 5 - E-commerce Applications
## by Siobhán Mooney

![Image of the site on various platforms.](/static/images/products.jpg)

### [Click here to view the deployed app.](https://gallery-of-dreams.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/gallery)

# Table of Contents:
1. [About the Project](#about-the-project)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [Visual Design](#visual-design)
    1. [Wireframes](#wireframes)
    2. [Screenshots](#screenshots)
3. [Data Design](#data-design)
    1. [Data Model](#data-model)
    2. [CRUD Functionality for Custom Models](#crud-functionality-for-custom-models)
4. [Agile Development](#agile-development)
5. [Security](#security)
    1. [Site Security](#site-security)
    2. [Secure Payments](#secure-payments)
6. [SEO & Marketing](#seo-&-marketing)
    1. [Marketing](#marketing)
    2. [Keywords](#keywords)
    3. [Facebook](#facebook)
    4. [Newsletter](#newsletter)
    5. [GDPR](#gdpr)
    6. [External Links](#external-links)
7. [Testing](#testing)
8. [Deployment](#deployment)
    1. [Forking the Repository on GitHub](#forking-the-repository-on-github)
    2. [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
    3. [Project setup](#project-setup)
    4. [Deploying to Heroku](#deploying-to-heroku)
9. [Acknowledgements](#acknowledgements)
    1. [Code Inspiration](#code-inspiration)
    2. [Technologies](#technologies)
    3. [Thanks](#thanks)

# About the project
Gallery of Dreams is envisaged as an online shop where artists can sell their designs printed on a variety of products ("canvasses").  At present, the site hosts the work of just one artist: Janka Latečková.  In the site as currently presented, Janka functions the flagship artist; the case for adding more artists will be proven, or disproven, by how successfully her work is showcased.  
The data model of Gallery of Dreams is designed with a view to strong central control.  With so many potential combinations of canvas plus design, the number of artworks could balloon quite quickly, so the ability to change many artworks with a single edit to one canvas or design is the guiding principle.  However, some other elements of the project, particularly the styling, could be more strongly differentiated from the Code Institute's Boutique Ado walkthrough.

## User Goals
- Easily navigate a readable, accessible website from any platform.
- Browse artworks by artist, design, and canvas.
- Once a purchase is chosen, make quick and secure payments.
- Have the option to register a user account, where order information can be quickly accessed and default delivery information can be stored.

## Owner Goals
- Present artworks to users in a clear, attractive manner.
- Increase user engagement by promoting artists' social media accounts.
- Have the ability to create, update, and delete data from the front end of the application.
- Use centralised methods to apply wide-ranging edits to canvasses and designs, which will be inherited by all related artworks.
- Process payments securely.

# Visual Design

## Wireframes
Visually, Gallery of Dreams was planned to follow the styling of Boutique Ado in a broad sense, while adding a few elements of custom flair (e.g. a distinctive logo).  
- More custom styling, while highly desirable, was treated as a stretch goal, to be pursued if time permitted after implementing and documenting the site's essential features.
- Broadly, in the final product, the degree of custom styling implemented was less than what was initially desired.
- With more time, the sharp button and field style would have been changed to a rounded style; a less stark (though still minimalistic) colour scheme would have been employed; and some key visual elements would have been repositioned.

Mobile wireframes:

![Mobile wireframes.](/static/images/wireframes_mobile.jpg)

Desktop wirefame: home page.

![Desktop home wireframe.](/static/images/wireframe_home_desktop.jpg)

Desktop list wirefame: artwork list.

![Desktop wireframe.](/static/images/wireframe_list_desktop.jpg)

Desktop detail wirefame: artwork detail.

![Desktop wireframe.](/static/images/wireframe_art_detail_desktop.jpg)

## Screenshots
The wireframes above can be compared to screenshots from the deployed site.

![Gallery index.](/static/images/gallery_index.jpg)
![Artwork detail.](/static/images/artwork_detail.jpg)
![Artworks.](/static/images/artworks.jpg)
![Canvas.](/static/images/canvas.jpg)
![Designs.](/static/images/designs.jpg)

# Data Design

## Data Model
As well as its custom models, Gallery of Dreams employs the following unaltered models from the Boutique Ado walkthrough: Order; OrderLineItem; and UserProfile.  The unaltered UserProfile model permits logged-in users to read and update their profiles.  All further commentary in this Data Model section concerns the project's four custom models.

The data model for the custom models of Gallery of Dreams is organised to describe artists, designs, canvasses, and artworks.  The main strength of this data model is central control of various artwork attributes without having to individually edit artworks.
- Artists are the persons responsible for original drawings and paintings. 
- Designs are the original drawings and paintings themseves.
- Canvasses are the types of products on which designs are printed.  
- Artworks are individual combinations of design and canvas.

The artist model includes fields for the artists' social media profiles, to encourage connectivity and engagement.  This information is optional rather than obligatory, as not all artists may wish to use social media, or to engage with all platforms.

Each design and canvas must have its own description.  However, artworks do not have their own descriptions, but rather inherit various descriptive fields from related models.  For instance, artwork price is inherited from the canvas rather than being directly associated with the artwork.  This means that, for example, each mug will cost the same regardless of the design printed on it.  Continuing this example: if the price of the mug canvas is changed, the prices of all mug artworks are automatically changed, inheriting from the canvas.  

See the entity relationship diagram, and the images depicting full model details, for further information:

![Entity Relationship Diagram.](/static/images/erd.jpg)
![Data model diagram 1.](/static/images/data_model_1.jpg)
![Data model diagram 2.](/static/images/data_model_2.jpg)

## CRUD Functionality for Custom Models

Artworks can be viewed/read by all users.  However, artworks can only be created, updated, and deleted by superusers.  Superusers can additionally create and update artists, canvasses, and designs from the front end.  

Front-end create functionality is handled via "Gallery Curation," accessed from the Account dropdown while a superuser is logged in.

Front-end editing and deleting is accessed via various list and detail views.  
- Clicking "All Artworks" in the Artwork dropdown shows all artworks, each displaying an edit link and a delete link if a superuser is logged in.  (Note: manually inputting an edit or delete link will not provide edit or delete functionality to non-superusers.)
- Similarly, "By Design" in the Design Dropdown and "By Canvas" in the Canvas dropdown list the designs and canvasses, each with an edit link if a superuser is logged in.
- Additionally, the flagship artist's detail page, accessed by clicking "About Janka L" in the Artist dropdown, displays an edit link if a superuser is logged in.
- While front-end deletion functionality is provided for artworks, it is consciously not provided for other model objects. This limitation is intended as a protective feature. If an artwork is deleted accidentally, it can be recreated easily. It is less easy to recreate a canvas or design, as many artworks depend on them for inherited data. Additionally, when only one artist is featured on the site so far, it would seem foolhardy to permit the easy deletion of that artist. 
- If needed, deletion functionality for artists, designs, and canvasses can be accessed via the admin panel, where it is expected that any deletions would be more clearly intentional on the part of the superuser.

# Agile Development
The [GitHub kanban board for Gallery of Dreams](https://github.com/users/Estelindis/projects/1) describes an agile development process on the basis of user stories.  Stories are categorised according to epics/milestones, development priority, and completion status.

- Once tasks were identified, issues were added to the "to do" column.
- All issues were labelled "must have" or "could have."  As not every imagined feature can generally be completed with a project's timeframe, it is important to work on tasks in order of priority.
- For tasks in development, the corresponding issues could be moved to the "in progress" column.
- Once sufficient content had been developed and tested to address tasks, the corresponding issues could be moved to the "done" column.  

|Link | Title | User Story | Epic/Milestone | Priority | Done? |
|---------|---------|---------|---------|---------|---------|
|[1](https://github.com/Estelindis/gallery/issues/1)|Clear site purpose|As a site user, I can instantly identify the purpose of the site so that I can know if the site interests me without wasting time.|General Site Use|Must have|Yes|
|[2](https://github.com/Estelindis/gallery/issues/2)|Site deployment|As a site user, I can access the site at its public URL so that I can view the site.|General Site Use|Must have|Yes|
|[3](https://github.com/Estelindis/gallery/issues/3)|Registration|As a site user, I can quickly and easily register with a verifiable email so that my details can be saved in my personal profile.|General Site Use|Must have|Yes|
|[4](https://github.com/Estelindis/gallery/issues/4)|Log in/out|As a site user, I can quickly and easily log in or out so that I can access my profile functionality (e.g. view order history, edit standard delivery info).|General Site Use|Must have|Yes|
|[7](https://github.com/Estelindis/gallery/issues/7)|Recover password|As a site user, I can quickly and easily reset my password so that I can retain access to my profile, even if I forget my password.|General Site Use|Must have|Yes|
|[5](https://github.com/Estelindis/gallery/issues/5)|View artist|As a site user, I can view artist details so that I can learn more about the artist and access related social media.|Browsing and Shopping|Could have|Yes|
|[6](https://github.com/Estelindis/gallery/issues/6)|View artwork list|As a site user, I can view a list of artworks so that I can choose which artworks I might buy.|Browsing and Shopping|Must have|Yes|
|[8](https://github.com/Estelindis/gallery/issues/8)|View artwork details|As a site user, I can view individual artwork details so that I can differentiate between artworks in finer detail.|Browsing and Shopping|Must have|Yes|
|[9](https://github.com/Estelindis/gallery/issues/9)|Search artworks|As a site user, I can search artworks by keyword so that I can quickly and easily find a specific item, or type of item.|Browsing and Shopping|Must have|Yes|
|[10](https://github.com/Estelindis/gallery/issues/10)|Sort by price|As a site user, I can sort artworks by price so that I can quickly and easily find items that meet my shopping criteria (i.e. within a certain price range).|Browsing and Shopping|Must have|Yes|
|[15](https://github.com/Estelindis/gallery/issues/15)|Sort by canvas & design|As a site user, I can sort artworks by canvas or design so that I can experience the choice of alternative sorting methods (not just sort by price).|Browsing and Shopping|Could have|Yes|
|[11](https://github.com/Estelindis/gallery/issues/11)|Filter artworks|As a site user, I can filter artworks (e.g. by canvas) so that I can browse the specific types of items that interest me (e.g. only art prints).|Browsing and Shopping|Must have|Yes|
|[12](https://github.com/Estelindis/gallery/issues/12)|Add artworks to bag|As a site user, I can easily add the items I want, in the quantity I want, to my bag so that I can enjoy a smooth purchasing experience.|Bag and Checkout|Must have|Yes|
|[13](https://github.com/Estelindis/gallery/issues/13)|View purchase total|As a site user, I can easily view my purchase total at any time so that I can avoid over-spending.|Bag and Checkout|Must have|Yes|
|[14](https://github.com/Estelindis/gallery/issues/14)|View order summary|As a site user, I can easily view a summary of my order so that I can see exactly what I would be buying, and paying, if I went to the check out now.|Bag and Checkout|Must have|Yes|
|[16](https://github.com/Estelindis/gallery/issues/16)|Enter payment info|As a site user, I can easily enter payment information so that I can check out quickly and smoothly.|Bag and Checkout|Must have|Yes|
|[17](https://github.com/Estelindis/gallery/issues/17)|Secure transaction|As a site user, I can complete a secure transaction using a trusted payment method so that I can be confident that my payment information is safe when buying from this site.|Bag and Checkout|Must have|Yes|
|[18](https://github.com/Estelindis/gallery/issues/18)|Order confirmation|As a site user, I can receive an order confirmation so that I can retain a record of my purchase.|Bag and Checkout|Must have|Yes|
|[19](https://github.com/Estelindis/gallery/issues/19)|Add artworks|As a superuser, I can create an artwork via the front end so that I can add new items to the shop without needing the admin panel.|Admin|Must have|Yes|
|[20](https://github.com/Estelindis/gallery/issues/20)|Update artworks|As a superuser, I can update an artwork via the front end so that I can edit shop items without needing the admin panel.|Admin|Must have|Yes|
|[21](https://github.com/Estelindis/gallery/issues/21)|Delete artworks|As a superuser, I can delete an artwork via the front end so that I can remove items from the shop without needing the admin panel.|Admin|Must have|Yes|
|[22](https://github.com/Estelindis/gallery/issues/22)|Create canvasses & designs|As a superuser, I can create a canvas or a design via the front end so that I can add canvasses or designs to the shop without needing the admin panel.|Admin|Could have|Yes|
|[23](https://github.com/Estelindis/gallery/issues/23)|Create canvasses & designs|As a superuser, I can edit a canvas or a design via the front end so that I can modify canvasses or designs without needing the admin panel.|Admin|Could have|Yes|

# Security

## Site Security
Gallery of Dreams implements role-based login and registration functionality.
- Views that should only be accessible when a user is logged in are secured via the "@login_required" decorator. 
 If non-logged-in users attempt to access these views, either by clicking a site link or by typing a URL directly into the address bar, they are redirected to the login page.
- Views whose functions should only be accessible to superusers include a superuser check.  If logged-in users who are not superusers attempt to access these functions, e.g. by typing an artwork edit URL directly into the address bar, they receive an error message and are redirected to the front page.

## Secure Payments
Payments on Gallery of Dreams are handled via Stripe, utilising secure payment tools.

# SEO & Marketing

## Marketing

When developing Gallery of Dreams, I asked myself the following questions:

**Who are your users?**
- People who like fan art, particularly from the fantasy genre.
- Fans of fantasy literature, particularly the works of JRR Tolkien (along with connected films and TV).
- Fans of hobbies adjacent to the fantasy genre, particularly tabletop and live-action roleplaying.
- People who like well-made fan art, regardless of genre.
- People who like art prints, including homeware printed with art.
- People who want to buy gifts for the above groups of people.

**On which online platforms & social media would you find many of your users?**
- DeviantArt (where the flagship artist has a strong presence).
- Pinterest (which consistently turns up frequently in searches related to the flagship artist).
- Etsy (where the flagship artist sells commissions and other bespoke items; this is complimentary to our shop, not a competitor).
- Facebook.
- Instagram.
- Twitter.

**What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?**
- Many users enjoy looking at art online and would also like to have a piece of art in their home.
- Many other users, appreciating that their family and friends are fans of art, would like to purchase art-printed items as gifts.
- Gallery of Dreams can offer special value to users by offering a curated selection of items based on genre and aesthetic, as well as focusing on particular artists.

**Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?**
- Periodic discount codes could be offered via newsletter.

**What are the goals of your business?**
- Gallery of Dreams is inspired by sites like RedBubble, which sells art-printed items from a huge range of artists.  However, because RedBubble has so many artists, designs, and products, it is saturated.  Saturation makes it difficult for artists to stand out.  It is also hard for shoppers to find exactly what they want.  By comparison, Gallery of Dreams would offer a more curated experience.  While Gallery of Dreams would not serve as many users as RedBubble, it would offer a more pleasant experience for shoppers seeking items with a fantasy art aesthetic, which in turn would offer benefits to featured artists.
- For the above reasons, Gallery of Dreams operates on a business-to-customer model in terms of selling art to customers, and arguably on a business-to-business model to a lesser extent, if independent artists are seen as small business owners.  

**Which marketing strategies would offer the best ways to meet those goals - free to low cost, or purchased advertising?**
- As a comparatively small business, Gallery of Dreams would focus on social media rather than paid advertising.
- The flagship artist has a strong social media presence. Linking to these platforms where she is present would increase user engagement.

## Keywords

While developing Gallery of Dreams, I engaged in substantial keyword research via [wordtracker.com](https://www.wordtracker.com) and Google search.  In the case of Google, auto-complete was often helpful in guiding searches towards common topics.
Of the various keywords chosen, some are employed throughout the site and on linked social media, while others are employed as meta keywords in page heads.  As keyword "spam" in page heads is broadly to be avoided, head keywords are employed in cases where a set of keywords provides good search results but doesn't fit particularly well in natural readable text.

**Keywords chosen**
- "character art" - strong results with low competition; related image searches are in keeping with the fantasy aesthetic of Gallery of Dreams.  Particularly strong potential for engagement with people who might use artworks to represent characters in their RPGs, who then get attached to that artwork and want to own related printed items.
- "tolkien fan art" - gives fewer results than "tolkien art"; however, the results are more relevant.
- "tolkien artists" - results are relevant to the site aesthetic; fans of notable Tolkien artists like Alan Lee and John Howe will find a similar art style in the site's flagship artist, who lists these artists among her inspirations.
- "art prints" - a very high volume of searches, with substantial competition; as Gallery of Dreams literally sells art prints, however, the use of these words is unavoidable.
- "fantasy art prints" - a smaller volume of searches than "art prints," but more relevant; naturally includes "art prints" when part of natural readable text.
- "wall art gifts" - also a smaller volume of searches than "art gifts" (particularly as Gallery of Dreams does not only sell wall art), yet, overall, still more relevant.  However, simply including "wall art gifts" in readable site text naturally includes "art gifts" in the same phrase, and this set of words returns less relevant results.  As such, a possibility is to include "wall art gifts" in page heads.
- "jankalart" - the username most commonly employed today by the flagship artist; this will also be represented as Janka L.  This will appear as part of several social media links.
- "jankolas" - the username formerly employed by the flagship artist, which still turns up in a lot of searches (particularly on Pinterest).  It doesn't make sense to include an old username in user-readable text, as this might dilute the artist's current branding, but the old username can still be employed judiciously in page heads.  (Note: a quick comparison between the 2009 version of the flagship artist's DeviantArt page via the Internet Archive and her DeviantArt page today does not seem to imply that use of the old username is problematic in terms of how the artist self-identifies.)

**Notable keywords not chosen**
- "tolkien art" - as Tolkien created many illustrations, this returns a lot of art by Tolkien himself rather than fan art inspired by his works.
- "art gifts" - this is too broad; results tend to include a lot of art supplies.
- "geek art" - this is also too broad; results include a ride range of intellectual properties not relevant to the aesthetic of Gallery of Dreams.
- "stores like redbubble" - returns a lot of list-style articles, in which our shop might benefit from being included; but a good proportion of these seem to be spam (AI-generated, in some cases), which would be counter-productive.  Additionally, mentioning RedBubble explicitly might encourage users of Gallery of Dreams to browse on RedBubble rather than with us.

## Facebook

Gallery of Dreams has its own Facebook page, which is linked in the footer of the index page.  (This footer is not present when browsing the store, to remove distractions while shopping.)

![FB 1.](/static/images/fb_page_01.jpg)
![FB 2.](/static/images/fb_page_02.jpg)

## Newsletter

Gallery of Dreams has newsletter sign-up functionality embedded in the footer of the index page, enabled by MailChimp.

## GDPR

A link to the privacy policy of Gallery of Dreams is present in the footer of the index page, via the user shield icon.

## External Links

All external links are directly connected to Gallery of Dreams, linking to social media for the shop or its flagship artist.  These links function as unpaid marketing, harnessing the power of the internet's "word of mouth."
- No external links are paid or distrusted (which would require a "nofollow" relationship attribute).
- No external links are sponsored or compensated (which would require a "sponsored" relationship attribute).

# Testing

Placeholder text.

# Deployment

## Forking the Repository on GitHub

1. Log in to GitHub and locate the GitHub Repository that you want to fork.
2. In the upper right of the repository, click the "Fork" button.
3. A copy of the repository will now be available within your repositories.

## Cloning the Repository on GitHub

1. In the upper section of the repository, click the dropdown named "Code."
2. In the "Clone" section, choose "HTTPS" if it is not already selected, then copy the URL.
3. Open a bash terminal in your IDE of choice.
4. Change the current working directory to the location you want for the cloned directory.
5. Type "git clone" and paste the URL copied from GitHub.
6. After pressing Enter, the clone of your repository will be created.

## Project Setup

The following steps are provided as an alternative to cloning the repository. As project development is an extensive process, for the most part these steps provide an outline only.
- Create a Python project in a virtual environment, using your IDE of choice.
- Copy requirements.txt from this Gallery of Dreams repository into your project directory.  Then, in the bash terminal, use the command ```pip install -r requirements.txt``` to install all required packages for Gallery of Dreams.  (Alternatively, install the packages manually, as listed in the requirements file in this Gallery of Dreams repository.  Start with Django, applying the version shown in requirements.txt.  Use the command ```pip install django==3.2 ```.  Then install each other listed package, paying attention to version.  Once done, create your own new requirements file via ```pip freeze > requirements.txt```.  This process should result in a requirements file identical to the one in this repository.)
- As Django documentation is extensive and well-written, [follow official documentation](https://docs.djangoproject.com/en/3.2/intro/tutorial01/) to start your Django project via the ```django-admin startproject``` command.  In the case of Gallery of Dreams, the base project is called ```gallery```.  A subfolder will automatically be created with the same name as your Django project.
- Create each app using the ```manage.py startapp``` command.  The apps for Gallery of Dreams are as follows: artworks; bag; checkout; home; profiles.
- Implement project settings, following the guidance of the current repository.  Default SQLite settings store data locally during development.  Additionally, variables are in place supporting a non-local database when deploying to Heroku.  To enable this non-local database on Heroku's end, environment variables will need to be set in Heroku, as outlined in the Heroku deployment guide below.
- Set environment variables.  If using GitPod, variables can be accessed by clicking your user portrait in the top right of the screen, choosing User Settings from the dropdown, then choosing Variables in the list that appears on the right of the page.  To enable local debugging while preventing live deployment in a state of ```Debug=True```, create an environment variable called DEVELOPMENT and set this to True (noting that this variable will not be set when deploying to Heroku).  To handle Stripe payments, set up three further environment variables: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, and STRIPE_WH_SECRET.  These values must be kept secret and should be determined by your personal Stripe settings.
- Create models as laid out in each models.py file of each app; then ```makemigrations``` (first performing a ```makemigrations --dry-run``` to check for mistakes); finally, ```migrate``` (again, after first performing ```migrate --plan``` to see which migrations will take place).
- Implement templates, views, URLS, etc., following the guidance of the current repository.
- Create a directory for static files during development, with the understanding that alternative arragements will be required for static files when deploying to Heroku. 

## Deploying to Heroku

- Log into Heroku (creating an account if needed).
- Click the "New" button from the dashboard, under the header in the top right corner.
- Choose "Create new app."
- Enter your application name, which has to be unique. Then select your region and click "Create App."
- From your project page, click the "Settings" tab and scroll to "Config Vars."  You will need to create variables, as follows; in each case, click the "Add" button to add the variable.
1. Key = "PORT"; Value = "8000". 
2. Key = "SECRET_KEY"; Value = [your django secret key].
3. For your non-development database (vs. SQLite for local development): Key = "DATABASE_URL"; Value = [your DB url, e.g. Postgres database url from Elephant SQL].
4. To send real verification emails: Key = "EMAIL_HOST_USER" and Value = [your email address; free email from Gmail is suggested]; also, Key = "EMAIL_HOST_PASS" and Value = [app password for the associated Gmail account; [see documentation](https://support.google.com/accounts/answer/185833?hl=en)].
5. To use Stripe, as in this project: Keys = "STRIPE_PUBLIC_KEY", "STRIPE_SECRET_KEY", "STRIPE_WH_SECRET"; Values = [your secret Stripe settings].
6. To use AWS, as in this project: Key = "USE_AWS" and Value = "True".  Also add secret settings, as follows: Keys = "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"; Values = [your secret AWS settings]. 
- On the same page, scroll to the buildpacks section and click "Add Buildpack."
- Add the Python buildpack.
- Go back to the tabs at the top of the page, then select the "Deploy" tab.
- Select the Github deployment method.
- Search for your repository name, then click the "Connect" button to link your repository.
- At the bottom of that page, select deployment type: Automatic or Manual. By pressing "Enable Automatic Deploys," the project will redeploy to Heroku every time it is pushed to GitHub. If Manual deployments are preferred, then choose a branch to deploy ("main" by default) and press "Deploy Branch."  In either case, there will be a short wait while the project is deployed.  

# Acknowledgements

## Code Inspiration
The code present in the project so far follows the Boutique Ado walkthrough from the Code Institute, adapted for the custom data models used in Gallery of Dreams.  As Boutique Ado was used as scaffolding with which to build Gallery of Dreams, [Chris Z](https://github.com/ckz8780) deserves acknowledgement for his inspiring code leadership.

## Technologies
- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com)
- [Elephant SQL](https://www.elephantsql.com/)
- [Amazon Web Services](https://aws.amazon.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com)
- [GitHub](https://github.com/)

## Thanks
This project was completed during a time of challenges and opportunities, including illness and a new job.  For patient tolerance of the ups and downs of my circumstances, I owe utmost thanks to Code Institute staff, particularly Student Care.  The facilitator of our msletb-nov-2021 cohort, Kasia, deserves a special mention.  I also wish to thank my mentor Darío, the members of my cohort, my new work colleagues, and my family and friends.
