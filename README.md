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
3. [Acknowledgements](#acknowledgements)

# About the project
Gallery of Dreams is envisaged as an online shop where artists can sell their designs printed on a variety of products ("canvasses").  At present, the site remains a work in progress, hosting the work of just one artist.  The data model shows significant differentiation from the Code Institute Boutique Ado walkthrough, being designed with a view to strong central control.  With so many potential combinations of canvas plus design, the number of artworks can balloon quite quickly, so the ability to change many artworks with a single edit to one canvas or design is the guiding principle.  However, some other elements of the project, particularly the styling, have yet to be strongly differentiated from the walkthrough.

## User Goals
- Easily navigate a readable, accessible website from any platform.
- Browse products by artist, design, and type of product.
- Once a purchase is chosen, make quick and secure payments.
- Have the option to register a user account, where order information can be quickly accessed and default delivery information can be stored.

## Owner Goals
- Present products to users in a clear, attractive manner.
- Increase user engagement by promoting artists' social media accounts.
- Have the ability to create, update, and delete artist and product data from the front end of the application.
- Use centralised methods to apply wide-ranging edits to related canvasses and designs, which will be inherited by all related artworks.
- Process payments securely.

# Design

## Data Models
The data model of Gallery of Dreams is organised to describe artists, designs, "canvasses" (the types of product on which a design is printed), and artworks (individual combinations of design and canvas).  This model should allow users to restrict their view by the various categories, should they so wish.  If, for instance, users wish to browse all tote bags regardless of design, the data model should permit this easily.  

Each design and canvas must have its own description.  However, artworks do not have their own descriptions, but rather inherit various descriptive fields from the related models.  For instance,item price is associated with the canvas rather than the product, as (for instance) each mug will cost the same regardless of the design printed on it.  This ensures that if (for example) the price of the mug canvas is changed, the prices of all mug artworks are automatically changed, inheriting from the canvas.

The artist model includes fields for the artists' social media profiles, to encourage connectivity and engagement.  This information is optional rather than obligatory, as not all artists may wish to use social media, or to engage with all platforms.

![Data model diagram 1.](/static/images/data_model_1.jpg)
![Data model diagram 2.](/static/images/data_model_2.jpg)

# Acknowledgements
The code present in the project so far follows the Boutique Ado walkthrough from the Code Institute, adapted for the different data models used in Gallery of Dreams.

![Artwork detail.](/static/images/artwork_detail.jpg)
![Designs.](/static/images/designs.jpg)
![Artworks.](/static/images/artworks.jpg)
![Canvas.](/static/images/canvas.jpg)

