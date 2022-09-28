| Method | URL                  | Input      | Output                                      | Notes                                            |
| ------ | -------------------- | ---------- | ------------------------------------------- | ------------------------------------------------ |
| GET    | users/               | -          | list of all user informations               |                                                  |
| GET    | myprofile/           | -          | profile for logged in user                  |                                                  |
| POST   | myprofile/           | profile    | input profile data informations             |                                                  |
| PATCH  | myprofile/           | -          | edit profile                                |                                                  |
| GET    | profile/id/          |            | profile of another user                     |                                                  |
| GET    | stickers/            | -          | list of cards for everyone                  | ?? could use /stickers-all                       |
| POST   | stickers/            | sticker    | new sticker                                 | creates a sticker                                |
| GET    | mystickers/          | -          | list of stickers for logged in user         |                                                  |
| GET    | stickers/following/  | -          | list of stickers from followed users        |                                                  |
| GET    | sticker/:id/         | -          | data for sticker with specified id          |                                                  |
| PATCH  | sticker/:id/         | card data  | update sticker                              | updates the sticker with specified id            |
| DELETE | sticker/:id/         | -          | -                                           | deletes sticker with specified id                |
| GET    | user/:id/stickers/   | -          | list of stickers for user with specified id | ?? change to stickers/user/id to keep consistent |
| POST   | user/<:id>/follow/   | -          | follow user with specified id               | ?? change to follow/user/id to keep constistent  |
| DELETE | user/<:id>/unfollow/ | -          | unfollow user with specified id             | ?? change to unfollow/user/id ...                |
| GET    | /folowing/           | -          | list of users followed by logged in user    |                                                  |
| POST   | /followers/          | user by id | list of users following logged in user      | add user as a friend                             |
