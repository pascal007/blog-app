# Django Blog App

This is a Django application for managing blog posts.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/pascal007/blog-app.git
    ```

2. Build the project using Docker Compose:

    ```bash
    docker-compose build
    ```

3. Start the project with Docker Compose:

    ```bash
    docker-compose up
    ```

4. Once the project is up, access it via the following URL:

    [http://localhost:10050](http://localhost:10050)

## API Endpoints

### User Management

- **Create User:**
  - **Endpoint:** `localhost:10050/api/v1/signup/`
  - **Method:** `POST`
  
- **Generate Token:**
  - **Endpoint:** `localhost:10050/api/v1/token/`
  - **Method:** `POST`

### Blog Posts

- **Access Posts:**
  - **Endpoint:** `localhost:10050/api/v1/post/`
  - **Method:** `GET`
  
- **Create Post:**
  - **Endpoint:** `localhost:10050/api/v1/post/`
  - **Method:** `POST`
  - **Payload:** `{"title": "string data", "content": "string data"}`
  
- **Delete Post:**
  - **Endpoint:** `localhost:10050/api/v1/post/<id>/`
  - **Method:** `DELETE`
  
- **Update Post:**
  - **Endpoint:** `localhost:10050/api/v1/post/<id>/`
  - **Method:** `PUT`
  - **Payload:** `{"title": "string data", "content": "string data"}`

