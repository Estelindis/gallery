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
3. [SEO & Marketing](#seo-&-marketing)
    1. [Marketing](#marketing)
    2. [Keywords](#keywords)
    3. [Facebook](#facebook)
    4. [Newsletter](#newsletter)
    5. [GDPR](#gdpr)
4. [Acknowledgements](#acknowledgements)

# About the project
Gallery of Dreams is envisaged as an online shop where artists can sell their designs printed on a variety of products ("canvasses").  At present, the site remains a work in progress, hosting the work of just one artist.  The data model shows significant differentiation from the Code Institute Boutique Ado walkthrough, being designed with a view to strong central control.  With so many potential combinations of canvas plus design, the number of artworks can balloon quite quickly, so the ability to change many artworks with a single edit to one canvas or design is the guiding principle.  However, some other elements of the project, particularly the styling, have yet to be strongly differentiated from the walkthrough.

## User Stories: User Goals
- Easily navigate a readable, accessible website from any platform: done.
- Browse products by artist, design, and type of product: done.
- Once a purchase is chosen, make quick and secure payments: done.
- Have the option to register a user account, where order information can be quickly accessed and default delivery information can be stored: done.

## User Stories: Owner Goals
- Present products to users in a clear, attractive manner: done.
- Increase user engagement by promoting artists' social media accounts: done.
- Have the ability to create, update, and delete artist and product data from the front end of the application: done.
- Use centralised methods to apply wide-ranging edits to related canvasses and designs, which will be inherited by all related artworks: done.
- Process payments securely: done.

# Design

## Data Models
The data model of Gallery of Dreams is organised to describe artists, designs, "canvasses" (the types of product on which a design is printed), and artworks (individual combinations of design and canvas).  This model should allow users to restrict their view by the various categories, should they so wish.  If, for instance, users wish to browse all tote bags regardless of design, the data model should permit this easily.  

Each design and canvas must have its own description.  However, artworks do not have their own descriptions, but rather inherit various descriptive fields from the related models.  For instance,item price is associated with the canvas rather than the product, as (for instance) each mug will cost the same regardless of the design printed on it.  This ensures that if (for example) the price of the mug canvas is changed, the prices of all mug artworks are automatically changed, inheriting from the canvas.

The artist model includes fields for the artists' social media profiles, to encourage connectivity and engagement.  This information is optional rather than obligatory, as not all artists may wish to use social media, or to engage with all platforms.

Artworks can be created, updated, and deleted via front-end form.  Artists can be updated via front-end form.  Otherwise, new instances of the models from the artworks app can be created, read, updated, and deleted via the admin panel.  (There does exist a front-end view to delete artists, but as the site currently only has one artist it was deemed advisable to remove front-end links to this view, for now.)

It is to be desired that, eventually, all objects from the artworks app models - artists, canvasses, designs, and artworks - could be created, read, updated, and deleted via front-end forms.  Further future planned functionality would auto-filled elements of the artwork form based on the primary keys selected from other models.  The strength of this design is central control of various attributes without having to individually edit artworks.

![Data model diagram 1.](/static/images/data_model_1.jpg)
![Data model diagram 2.](/static/images/data_model_2.jpg)

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

# Acknowledgements
The code present in the project so far follows the Boutique Ado walkthrough from the Code Institute, adapted for the different data models used in Gallery of Dreams.

![Gallery index.](/static/images/gallery_index.jpg)
![Artwork detail.](/static/images/artwork_detail.jpg)
![Artworks.](/static/images/artworks.jpg)
![Canvas.](/static/images/canvas.jpg)
![Designs.](/static/images/designs.jpg)

