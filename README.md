
# bookry 

---

Bookry is a simple App for tracking the books you have read.

##Preview
_Images follow_

## Tech Stack
* React.js
* FastApi
* OpenLibrary.org API (Get book data)

## TODO
- [x] Create/Setup Database
- [x] Code Dao's
- [x] Test Database
- [ ] Create Login/Register Page
- [ ] JWT Login
- [ ] Make first Register/Login
- [ ] Search for books through the OpenLibrary.org API

## Setup
### First clone this repo
```bash
git clone https://github.com/NikWindup/bookry .
```
### Install all python dependencies
```bash
python -m pip install -r requirements.txt
```
### Change into api directory
```bash
cd api
```
### Create the database and the tables inside of the api directory
```bash
python -m SetupDB
```
### Start the fastapi server
```bash
fastapi run main.py
```
If you are a developer run
```bash
fastapi dev main.py
```
### Change into frontend directory
```bash
cd ..
cd frontend
```
### Install the dependencies for the frontend
```bash
npm install
```
### Start the frontend server
```bash
npm run dev
```
