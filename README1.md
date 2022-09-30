# Stickers

## https://team-shrek-e-stickers-backend.herokuapp.com

## Routes require authentication

### GET `stickers/`

List all public stickers

### POST `auth/token/login`

```json
{
  "username": "admin",
  "password": "kittykat2"
}
```

## Routes require authentication

### GET `/users/`

**restricted to admin users only** TODO-permissions

List all users

---

### GET/PATCH/DELETE `/myprofile/`

profile for logged in user
update, edit delete

---

### POST/PATCH/PUT/DELETE `/profile/<int:pk>/`

Detail for one user (getting the information using the pk for the user)
Edit or delete for one user (pk for the user)

---

### GET/POST `/mystickers/`

List stickers for logged in user (pk for the user)

---

### GET/POST `/stickers/`

List of all stickers
create new sticker

---

### GET/PATCH/PUT/DELETE `/stickers/<int:pk>/`

Detail about one sticker
update or delete sticker

---

### GET `/stickers/following/` # not yet available

List of stickers from users followed by logged in user

---

### POST `/user/<int:pk>/follow/`

Follow/unfollow a user (pk for the user to follow)

---

### DELETE `/user/<int:pk>/unfollow/`

Follow/unfollow a user (pk for the user to follow)

---

### GET `/following/`

List of who the logged in user is following

---

### GET `/followed-by/`

List of who is following the logged in user

---
