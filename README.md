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

# About the project
Gallery of Dreams is envisaged as an online shop where artists can sell their designs printed on a variety of products.  

## User Goals
- Easily navigate a readable, accessible website from any platform.
- Browse products by artist, design, and type of product.
- Once a purchase is chosen, make quick and secure payments.
- Have the option to register a user account, where order information can be quickly accessed and default delivery information can be stored.

## Owner Goals
- Present products to users in a clear, attractive manner.
- Increase user engagement by promoting artists' social media accounts.
- Have the ability to create, update, and delete artist and product data from the front end of the application.
- Process payments securely.

# Design

## Data Models
The data model of Gallery of Dreams is organised to describe artists, designs, "canvasses" (the types of product on which a design is printed), and products (individual combinations of design and canvas).  This model should allow users to restrict their view by the various categories, should they so wish.  If, for instance, users wish to browse all tote bags regardless of design, the data model should permit this easily.  

Each design and canvas must have its own description.  However, a description for each product is optional.  Each product can be described via concatenation of its design and canvas descriptions, without the site owner needing to write a product description manually.  Should an additional description be desired for any product, that option is available.  By contrast, individual images will need to be provided for each product, so that users can see exactly how a design will look when printed on a particular canvas.  Item price is associated with the canvas rather than the product, as (for instance) each mug will cost the same regardless of the design printed on it.

The artist model includes fields for the artists' social media profiles, to encourage connectivity and engagement.  This information is optional rather than obligatory, as not all artists may wish to use social media, or to engage with all platforms.

![Data model diagram.](/static/images/data_model.jpg)

