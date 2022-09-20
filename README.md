# Create a social greeting card service

**IMPORTANT**: Please read this document closely. Many resources are linked within it. Before starting on your project, assemble a list of the tasks you think you need to do and discuss how you will tackle these together. The front-end will need to make some basic [wireframes](https://www.orbitmedia.com/blog/7-reasons-to-wireframe/#:~:text=for%20your%20website.-,Wireframes%20are%20simple%20black%20and%20white%20layouts%20that%20outline%20the,focusing%20on%20a%20site's%20structure).

Imagine a social network, like Twitter or Facebook. Imagine electronic greeting cards. Now imagine them together -- that's what you are building as a group in this project.

## Description & Overview

The social e-cards application lets users sign up, create greeting cards, and follow each other. A user can see cards shown from newest to oldest: they can see a collection of their own cards, a collection of cards by users they follow, and a colletion of all cards.

### Following

Note there is a big difference between the two major social platforms: on Twitter, relationships are one-way. If I follow you, you don't automatically follow me. On Facebook, relationships are two-way. You can choose which paradigm to use for this project, but if you make relationships two-way, they should be approved by the user to whom the relationship is being proposed (a "friend request," in Facebook terms.) _One-way relationships are easier and suggested._

### Cards and Customizable Options

Once a user is a member of your site, they can create "cards." You may choose to call these something else -- creative interpretation is always welcome! Think of a card as a visual message with customizable text, styling and images. As a group, you should decide on the customizable options, but there should be at least three. Some examples of customizable options you can offer users are:

- the card color (from a predefined list)
- the border style ([here is an article on making cool borders with CSS](https://amethystwebsitedesign.com/decorative-borders-with-only-css-and-no-images/))
- the font (from a predefined list; choose a set of fonts to bring in from [Google Fonts](https://fonts.google.com/))
- the text alignment
- an image to include (Note: uploading images to an API will require significantly more work. An recommended alternative is to use the [Unsplash API](https://unsplash.com/developers) on the front-end and store the image location (url) on the back-end.)
- an outer message and inner message -- the inner message would be shown with some sort of transition on click, like the front and interior of a greeting card

### "Pages"

Users should be able to see three screens of cards:
- a screen of cards from users they follow 
- a screen of their own cards
- and a screen of cards from all users 

Each collection should show a reasonable number of cards, sorted with the newest first, and allow the user to click to see more. 

If you would prefer to implement [an infinite scroll](https://www.smashingmagazine.com/2013/05/infinite-scrolling-lets-get-to-the-bottom-of-this/), go for it! The point is that the API should [paginate results](https://www.django-rest-framework.org/api-guide/pagination/).

### Design

As for how all of this should look, that is up to you! We are not providing wireframes, but your group should sit down and make decisions about what pages will be needed and what they will look like before you start writing code.

## 🌶️ Features

The above is a minimum set of features. You might want to add other features, and you should go for it if you have time. Some ideas:

- liking or favoriting cards
- comments or responses to cards
- directly sending cards to users
- draft cards (cards not yet shown that are still being created)

Be creative and make this project your own.

## Process

Your application is really two applications -- a back-end API written with Django REST Framework and a front-end React application. The back-end API should be deployed on [Heroku](https://heroku.com/) and the front-end app should be deployed on [Netlify](https://www.netlify.com/).

### Front-end development notes

During development of the front-end, you will want to be able to make requests before the API is complete. You can handle this in a few ways.

One way is to make functions or methods for all your API calls, but instead of having them actually make the calls at first, have them set the data you are expecting without actually making an API call. Another way is to use the provided exported mock API specification for [Mockoon](https://mockoon.com/), a tool that will run a mock server for you. In this case, you will want to be able to switch which server you use based on the environment your code is running in. [An API specification you can import into Mockoon is provided](social-cards-mockoon.json).

You can [read more about approaches to building your front-end before the API is done in this dev.to article](https://dev.to/momentum/how-to-build-a-front-end-app-before-you-have-an-api-3ai3).

**If you need to switch how you access your data based on environment**, [read this article on create-react-app-environments](https://medium.com/@tacomanator/environments-with-create-react-app-7b645312c09d). 

You _can_ work with your partner to get the back-end API running on your local machine, but you do not have to.

## Front-end spec suggestions

You can design your front-end to have whatever components you think are necessary. A suggested layout is below. A few notes: `Route` is from react-router, nesting shows what children each component might have, and several components are re-used under different routes. This is a non-exhaustive list and created from sketching on paper.

- App
  - Header
    - LoginControl
    - Menubar
  - Route /
    - CardList
      - Card - LikeButton
  - Route /all
    - CardList
      - Card
        - LikeButton
  - Route /me
    - Profile
    - CardList
      - Card
  - Route /me/edit
    - ProfileEditor
  - Route /person/:username
    - Profile
    - FollowButton
    - CardList
      - Card
        - LikeButton
  - Route /create-card
    - CardEditor
      - CardForm
      - CardPreview

### Authenticating from the front-end

Your back-end partner will show you how authentication works with Django REST Framework. What you will need to do is get an authentication token from the back-end (usually via POST to a URL like `/api/auth/token/login/`) and [store that token in localStorage](https://programmingwithmosh.com/react/localstorage-react/) for use on later requests.

## Back-end spec suggestions

You should use [djoser](https://djoser.readthedocs.io/en/latest/) and [token-based authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) to handle registration and login.

A suggested list of endpoints and what they should do are listed below:

| Method | URL               | Input      | Output                              | Notes                                              |
| ------ | ----------------- | ---------- | ----------------------------------- | -------------------------------------------------- |
| GET    | /cards/           | -          | list of cards from users you follow |                                                    |
| GET    | /cards/me/        | -          | list of cards you have made         | could use /cards/?list=mine or something like that |
| GET    | /cards/all/       | -          | list of cards for everyone          | could use /cards/?list=all                         |
| POST   | /cards/           | card data  | new card                            | creates a card                                     |
| GET    | /cards/:id/       | -          | data for card with specified id     |                                                    |
| PATCH  | /cards/:id/       | card data  | updated card                        | updates the card with specified id                 |
| DELETE | /cards/:id/       | -          | -                                   | deletes card with specified id                     |
| GET    | /friends/         | -          | list of all your "friends"          |                                                    |
| POST   | /friends/         | user by id | user info                           | add user as a friend                               |
| DELETE | /friends/:user_id | -          | -                                   | removes user with specified id from your friends   |

### CORS

CORS (Cross-Origin Resource Sharing) headers must be added to your responses for the front-end app to be able to interact with your API. [Read this blog post for more on how to set up CORS](https://www.stackhawk.com/blog/django-cors-guide). You will want to use [`django-cors-headers`](https://github.com/adamchainz/django-cors-headers) and set `CORS_ALLOW_ALL_ORIGINS = True`.
