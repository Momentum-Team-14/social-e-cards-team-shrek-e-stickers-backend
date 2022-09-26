# Stickers

## Routes that don't require authentication

### GET `stickers/`

List all public stickers

### POST `auth/token/login`

```json
{
  "username": "admin",
  "password": "kittykat2"
}
```

## Routes that require authentication

### GET `/users/`

**restricted to admin users only** TODO-permissions

List all users

---

### GET `/profile/<int:pk>/`

Detail for one user (getting the information using the pk for the user)

---

### PATCH/PUT/DELETE `/profile/<int:pk>/`

Edit or delete for one user (pk for the user)

---

### GET `/user/<int:pk>/stickers`

List stickers for logged in user (pk for the user)

---

### GET `/stickers/`

List of all stickers

---

### POST `/stickers/`

Create a new stickers

---

### GET `/stickers/<int:pk>/`

Detail about one sticker

---

### PATCH/PUT/DELETE `/stickers/<int:pk>/`

Update or delete a specific sticker

---

### GET `/stickers/following/` # not yet available

List of stickers from users followed by logged in user

---

### POST/PATCH/PUT `/user/<int:pk>/follow/`

Follow/unfollow a user (pk for the user)

---

### GET `/following/`

List of who the logged in user is following

---

### GET `/followed-by/`

List of who is following the logged in user

---
