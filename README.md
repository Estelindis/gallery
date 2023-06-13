# Gallery of Dreams - Project Portfolio 5 - E-commerce Applications
## by Siobhán Mooney

![Image of the site on various platforms.](/static/images/products.jpg)

### [Click here to view the deployed app.](https://gallery-of-dreams.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/gallery)

# Table of Contents:
1. [About the Project](#about-the-project)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [Design](#design)
    1. [Data Models](#data-models)
3. [Agile Development](#agile-development)
    1. [Data Models](#data-models)
4. [Security](#security)
    1. [Site Security](#site-security)
    2. [Secure Payments](#secure-payments)
5. [SEO & Marketing](#seo-&-marketing)
    1. [Marketing](#marketing)
    2. [Keywords](#keywords)
    3. [Facebook](#facebook)
    4. [Newsletter](#newsletter)
    5. [GDPR](#gdpr)
    6. [External Links](#external-links)
6. [Deployment](#deployment)
    1. [Forking the Repository on GitHub](#forking-the-repository-on-github)
    2. [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
    3. [Project setup](#project-setup)
    4. [Deploying to Heroku](#deploying-to-heroku)
7. [Acknowledgements](#acknowledgements)

# About the project
Gallery of Dreams is envisaged as an online shop where artists can sell their designs printed on a variety of products ("canvasses").  At present, the site remains a work in progress, hosting the work of just one artist.  The data model shows significant differentiation from the Code Institute Boutique Ado walkthrough, being designed with a view to strong central control.  With so many potential combinations of canvas plus design, the number of artworks can balloon quite quickly, so the ability to change many artworks with a single edit to one canvas or design is the guiding principle.  However, some other elements of the project, particularly the styling, have yet to be strongly differentiated from the walkthrough.

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


# Design

## Data Models
The data model of Gallery of Dreams is organised to describe artists, designs, "canvasses" (the types of product on which a design is printed), and artworks (individual combinations of design and canvas).  This model should allow users to restrict their view by the various categories, should they so wish.  If, for instance, users wish to browse all tote bags regardless of design, the data model should permit this easily.  

Each design and canvas must have its own description.  However, artworks do not have their own descriptions, but rather inherit various descriptive fields from the related models.  For instance,item price is associated with the canvas rather than the product, as (for instance) each mug will cost the same regardless of the design printed on it.  This ensures that if (for example) the price of the mug canvas is changed, the prices of all mug artworks are automatically changed, inheriting from the canvas.

The artist model includes fields for the artists' social media profiles, to encourage connectivity and engagement.  This information is optional rather than obligatory, as not all artists may wish to use social media, or to engage with all platforms.

Artworks can be created, updated, and deleted via front-end form.  Artists can be updated via front-end form.  Otherwise, new instances of the models from the artworks app can be created, read, updated, and deleted via the admin panel.  (There does exist a front-end view to delete artists, but as the site currently only has one artist it was deemed advisable to remove front-end links to this view, for now.)

It is to be desired that, eventually, all objects from the artworks app models - artists, canvasses, designs, and artworks - could be created, read, updated, and deleted via front-end forms.  Further future planned functionality would auto-filled elements of the artwork form based on the primary keys selected from other models.  The strength of this design is central control of various attributes without having to individually edit artworks.

![Data model diagram 1.](/static/images/data_model_1.jpg)
![Data model diagram 2.](/static/images/data_model_2.jpg)

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
- Apply database settings as needed.  If using the default SQLite settings to store data locally during development, no change to the base settings.py file will be required; but to write to a non-local database (e.g. for deployment to Heroku), other database settings will be needed.
- Create models as laid out in each models.py file of each app; then ```makemigrations``` (first performing a ```makemigrations --dry-run``` to check for mistakes); finally, ```migrate``` (again, after first performing ```migrate --plan``` to see which migrations will take place).
- Implement settings, templates, views, URLS, etc., following the guidance of the current repository.
- Create a directory for static files during development, with the understanding that alternative arragements will be required for static files when deploying to Heroku. 
- Set environment variables.  If using GitPod, variables can be accessed by clicking your user portrait in the top right of the screen, choosing User Settings from the dropdown, then choosing Variables in the list that appears on the right of the page.  To enable local debugging while preventing live deployment in a state of ```Debug=True```, create an environment variable called DEVELOPMENT and set this to True (noting that this variable will not be set when deploying to Heroku).  To handle Stripe payments, set up three further environment variables: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, and STRIPE_WH_SECRET.  These values must be kept secret and should be determined by your personal Stripe settings.

## Deploying to Heroku

- Log into Heroku (creating an account if needed).
- Click the "New" button from the dashboard, under the header in the top right corner.
- Choose "Create new app."
- Enter your application name, which has to be unique. Then select your region and click "Create App."
- From your project page, click the "Settings" tab and scroll to "Config Vars."
- Enter "PORT" in the KEY input field, then enter "8000" in the VALUE input field.
- Click the "Add" button to add the Convig Vars.
- On the same page, scroll to the buildpacks section and click "Add Buildpack."
- Add the Python and node.js buildpacks, ensuring that the Python buildpack is listed above the node.js buildpack.
- Go back to the tabs at the top of the page, then select the "Deploy" tab.
- Select the Github deployment method.
- Search for your repository name, then click the "Connect" button to link your repository.
- At the bottom of that page, select deployment type: Automatic or Manual. By pressing "Enable Automatic Deploys," the project will redeploy to Heroku every time it is pushed to GitHub. If Manual deployments are preferred, then choose a branch to deploy ("main" by default) and press "Deploy Branch."  In either case, there will be a short wait while the project is deployed.  
- Broadly speaking, manual deployment is preferred for this kind of project, so that DEBUG in settings.py can be set to True during development but False during deployment.


# Acknowledgements
The code present in the project so far follows the Boutique Ado walkthrough from the Code Institute, adapted for the different data models used in Gallery of Dreams.

![Gallery index.](/static/images/gallery_index.jpg)
![Artwork detail.](/static/images/artwork_detail.jpg)
![Artworks.](/static/images/artworks.jpg)
![Canvas.](/static/images/canvas.jpg)
![Designs.](/static/images/designs.jpg)

