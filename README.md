# Stickers

## Routes that don't require authentication

### GET `stickers/`

List all public stickers

### POST `auth/token/login`

```json
{
  "username": "donkey",
  "password": "waffles"
}
```

## Routes that require authentication

### GET `/users/`

**restricted to admin users only**

List all users

---

### GET `/profile/<int:pk>/`

Detail for one user (getting the information using the pk for the user)

---

### PATCH/PUT/DELETE `/profile/<int:pk>/`

Edit or delete for one user (getting the information using the pk for the user)

---

### GET `/stickers/`

List all your stickers

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

### GET `/stickers/following/`

Show stickers for users followed by logged in user

---

